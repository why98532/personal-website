"""
Part 3: 按公众号作者汇总观点
基于关键词匹配（利好/风险/看多/看空/中性）提取观点，按作者聚合

数据来源：
  1. 优先从 wechat_links.txt 读取链接，用 requests + BeautifulSoup 抓取
  2. 抓取失败时回退到模拟数据
"""

import json
import os
import re
import time
from datetime import datetime
from typing import Optional, Dict, List

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

# 关键词 → 观点标签映射
KEYWORD_SENTIMENT = {
    "利好": "看多", "机会": "看多", "增长": "看多", "突破": "看多", "爆发": "看多",
    "反弹": "看多", "走强": "看多", "牛市": "看多", "看好": "看多", "加仓": "看多",
    "风险": "看空", "下跌": "看空", "压力": "看空", "回调": "看空", "走弱": "看空",
    "熊市": "看空", "减仓": "看空", "警惕": "看空", "泡沫": "看空",
    "不确定": "中性", "观望": "中性", "震荡": "中性", "分化": "中性", "盘整": "中性",
}

# 模拟公众号文章数据（抓取失败时的回退）
MOCK_ARTICLES = [
    {
        "author": "张三-财经观察",
        "title": "AI板块再迎政策利好，算力赛道持续爆发",
        "content": "国务院发布AI产业指导意见，利好算力和大模型企业。AI板块迎来重大发展机会，建议重点关注算力基础设施。短期内芯片出口管制有一定风险，但国产替代趋势不变。",
    },
    {
        "author": "李四-投资笔记",
        "title": "新能源车销量超预期，锂电产业链值得关注",
        "content": "1月新能源车上险量环比增长15%，超出市场预期。锂电上游材料价格企稳回升，龙头企业订单饱满。中长期来看，新能源车增长趋势明确，但短期需注意竞争加剧带来的价格压力。",
    },
    {
        "author": "张三-财经观察",
        "title": "光伏行业寒冬未过，硅片企业面临深度调整",
        "content": "光伏组件价格持续下跌，行业开工率仅60%。硅片环节产能过剩严重，短期内看不到价格企稳迹象。对于光伏板块，建议投资者规避风险，等待行业出清信号。",
    },
    {
        "author": "王五-科技前沿",
        "title": "人形机器人量产在即，产业链迎来爆发期",
        "content": "特斯拉Optimus机器人即将量产，国内机器人产业链订单有望爆发。汇川技术、埃斯顿等核心零部件企业将直接受益。这是一个重要突破，建议积极布局。",
    },
    {
        "author": "赵六-市场分析",
        "title": "光伏板块底部信号不明，维持谨慎观望",
        "content": "光伏板块虽然估值处于历史低位，但基本面仍未见底。市场处于震荡分化阶段，投资者应保持观望态度。短期不确定性较大，不建议盲目抄底。",
    },
]


def _read_links() -> list[str]:
    """从 wechat_links.txt 读取公众号文章链接"""
    path = os.path.join(DATA_DIR, "wechat_links.txt")
    links = []
    if not os.path.exists(path):
        return links
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and line.startswith("http"):
                links.append(line)
    return links


def _fetch_article(url: str) -> Optional[dict]:
    """尝试用 requests + BeautifulSoup 抓取单篇文章，失败返回 None"""
    try:
        import requests
        from bs4 import BeautifulSoup

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        # 微信文章标题通常在 #activity-name 或 #js_article h1
        title_el = (
            soup.select_one("#activity-name")
            or soup.select_one(".rich_media_title")
            or soup.select_one("h1")
        )
        title = title_el.get_text(strip=True) if title_el else "未知标题"

        # 正文在 #js_content 或 .rich_media_content
        content_el = (
            soup.select_one("#js_content")
            or soup.select_one(".rich_media_content")
        )
        content = content_el.get_text(strip=True) if content_el else ""

        # 作者在 #js_name 或 .rich_media_meta_text
        author_el = (
            soup.select_one("#js_name")
            or soup.select_one(".rich_media_meta_nickname")
        )
        author = author_el.get_text(strip=True) if author_el else "未知作者"

        if not content:
            return None  # 没抓到正文，回退模拟数据

        return {
            "author": author,
            "title": title,
            "content": content[:3000],  # 截取前3000字符做关键词分析
            "source_link": url,
            "fetched": True,
        }
    except Exception:
        return None


def _extract_sentiment(content: str) -> str:
    scores = {"看多": 0, "看空": 0, "中性": 0}
    for kw, label in KEYWORD_SENTIMENT.items():
        count = content.count(kw)
        scores[label] += count
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "中性"


def _extract_core_opinion(content: str) -> str:
    """从文章正文中提取最核心的一句观点（关键词匹配得分最高的句子）"""
    sentences = re.split(r'[。！？\n]', content)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 8]
    if not sentences:
        return content[:80] + "..." if len(content) > 80 else content

    best_sentence = ""
    best_score = -1
    for s in sentences:
        score = sum(1 for kw in KEYWORD_SENTIMENT if kw in s)
        # 短句优先（但不是太短），有观点的句子更好
        if score > best_score or (score == best_score and len(s) < len(best_sentence)):
            best_score = score
            best_sentence = s

    if not best_sentence:
        best_sentence = sentences[0]

    return best_sentence[:100] + ("..." if len(best_sentence) > 100 else "")


def fetch() -> dict:
    links = _read_links()
    articles = []
    fetched_count = 0
    mock_count = 0

    if links:
        print(f"  [article_analysis] 读取到 {len(links)} 个链接，开始抓取...")
        for i, url in enumerate(links):
            print(f"    [{i+1}/{len(links)}] {url[:60]}...", end=" ")
            result = _fetch_article(url)
            if result:
                articles.append(result)
                fetched_count += 1
                print("OK (抓取成功)")
            else:
                # 回退到模拟数据
                if i < len(MOCK_ARTICLES):
                    mock = MOCK_ARTICLES[i].copy()
                    mock["source_link"] = url
                    mock["fetched"] = False
                    articles.append(mock)
                    mock_count += 1
                    print("FAIL (使用模拟数据)")
                else:
                    print("FAIL (跳过)")
            time.sleep(0.5)  # 请求间隔，避免被封
    else:
        print("  [article_analysis] 未找到链接文件，使用全部模拟数据")
        for mock in MOCK_ARTICLES:
            a = mock.copy()
            a["source_link"] = ""
            a["fetched"] = False
            articles.append(a)
            mock_count += 1

    print(f"  [article_analysis] 结果: 抓取 {fetched_count} 篇, 模拟 {mock_count} 篇")

    # 按作者聚合
    author_map: dict[str, list[dict]] = {}
    for art in articles:
        sentiment = _extract_sentiment(art["content"])
        core = _extract_core_opinion(art["content"])
        entry = {
            "article_title": art["title"],
            "sentiment": sentiment,
            "core_opinion": core,
            "source_link": art.get("source_link", ""),
            "fetched": art.get("fetched", False),
        }
        author_map.setdefault(art["author"], []).append(entry)

    authors = []
    for name, arts in author_map.items():
        sentiments = [a["sentiment"] for a in arts]
        dominant = max(set(sentiments), key=sentiments.count) if sentiments else "中性"
        authors.append({
            "author_name": name,
            "article_count": len(arts),
            "dominant_sentiment": dominant,
            "articles": arts,
        })

    return {
        "title": "按公众号作者汇总观点",
        "authors": authors,
        "fetch_stats": {
            "total_links": len(links),
            "fetched": fetched_count,
            "mock": mock_count,
        },
    }


if __name__ == "__main__":
    import pprint
    pprint.pprint(fetch())
