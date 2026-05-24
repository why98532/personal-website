#!/usr/bin/env python3
"""
公众号舆情监控系统（硬编码原型版）
===============================
功能：
  1. 近一周市场重大事件摘要
  2. 当前热度前10大板块及其标的现状
  3. 按公众号作者汇总观点
  4. 前五大细分板块建议（标注一致性）

输出：
  - 控制台打印
  - output/report.json
  - output/report.txt
"""

import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from fetchers import market_events, hot_sectors, article_analysis, sector_advice

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def generate_report() -> dict:
    print("=" * 60)
    print("  公众号舆情监控系统 v0.1 (硬编码原型)")
    print(f"  运行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Part 1
    print("\n" + "─" * 50)
    result1 = market_events.fetch()
    print(f"\n  [1/4] {result1['title']}")
    print(f"  综合舆情倾向: {result1['overall_sentiment']}")
    for e in result1["events"]:
        print(f"    {e['date']}  {e['event'][:45]}...  [{e['sentiment']}]")

    # Part 2
    print("\n" + "─" * 50)
    result2 = hot_sectors.fetch()
    print(f"\n  [2/4] {result2['title']}")
    for s in result2["sectors"]:
        sign = "+" if s["avg_change_pct"] >= 0 else ""
        print(f"    #{s['rank']:2d}  {s['sector_name']:　<8s}  均涨跌 {sign}{s['avg_change_pct']:.2f}%  [{s['trend']}]")
        for st in s["representative_stocks"]:
            sgn = "+" if st["change_pct"] >= 0 else ""
            print(f"          {st['code']} {st['name']}  {st['price']:.2f}  ({sgn}{st['change_pct']:.1f}%)")

    # Part 3
    print("\n" + "─" * 50)
    result3 = article_analysis.fetch()
    print(f"\n  [3/4] {result3['title']}")
    for a in result3["authors"]:
        print(f"\n    【{a['author_name']}】(共{a['article_count']}篇，倾向: {a['dominant_sentiment']})")
        for art in a["articles"]:
            print(f"      - {art['article_title']}  [{art['sentiment']}]")

    # Part 4 — 动态匹配 Part 3 的真实作者
    print("\n" + "─" * 50)
    result4 = sector_advice.fetch(authors=result3.get("authors", []))
    print(f"\n  [4/4] {result4['title']}")
    for r in result4["recommendations"]:
        tag = r["consistency_note"]
        print(f"    #{r['rank']}  {r['name']}({r['parent_sector']})  [{r['advice_icon']}] {r['advice']}")
        print(f"          理由: {r['reason']}")
        if tag:
            print(f"          {tag}")

    print("\n" + "=" * 60)
    print("  报告生成完毕。输出文件: output/report.json, output/report.txt")
    print("=" * 60)

    fetch_stats = result3.get("fetch_stats", {})
    total = fetch_stats.get("total_links", 0)
    fetched = fetch_stats.get("fetched", 0)
    mock = fetch_stats.get("mock", 0)
    if fetched > 0:
        source_desc = f"抓取 {fetched} 篇 / 模拟 {mock} 篇 (共 {total} 个链接)"
    else:
        source_desc = "mock (硬编码模拟数据)"

    return {
        "meta": {
            "title": "公众号舆情监控报告",
            "version": "0.1.0",
            "generated_at": datetime.now().isoformat(),
            "data_source": source_desc,
            "total_links": total,
            "fetched_count": fetched,
            "mock_count": mock,
        },
        "part1_market_events": result1,
        "part2_hot_sectors": result2,
        "part3_author_opinions": result3,
        "part4_sector_advice": result4,
    }


def save_report(report: dict):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    json_path = os.path.join(OUTPUT_DIR, "report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"  [JSON] {json_path}")

    txt_path = os.path.join(OUTPUT_DIR, "report.txt")
    with open(txt_path, "w", encoding="utf-8") as f:

        def w(line=""):
            f.write(line + "\n")

        w(f"公众号舆情监控报告")
        w(f"生成时间: {report['meta']['generated_at']}")
        w(f"数据来源: {report['meta']['data_source']}")
        w("=" * 60)

        r1 = report["part1_market_events"]
        w(f"\n[1/4] {r1['title']}")
        w(f"综合舆情倾向: {r1['overall_sentiment']}")
        for e in r1["events"]:
            w(f"  {e['date']}  {e['event']}  [{e['sentiment']}]")

        r2 = report["part2_hot_sectors"]
        w(f"\n[2/4] {r2['title']}")
        for s in r2["sectors"]:
            sign = "+" if s["avg_change_pct"] >= 0 else ""
            w(f"  #{s['rank']:2d} {s['sector_name']}  均涨跌{sign}{s['avg_change_pct']}% [{s['trend']}]")
            for st in s["representative_stocks"]:
                sgn = "+" if st["change_pct"] >= 0 else ""
                w(f"      {st['code']} {st['name']} {st['price']:.2f} ({sgn}{st['change_pct']:.1f}%)")

        r3 = report["part3_author_opinions"]
        w(f"\n[3/4] {r3['title']}")
        for a in r3["authors"]:
            w(f"  【{a['author_name']}】(共{a['article_count']}篇, 倾向: {a['dominant_sentiment']})")
            for art in a["articles"]:
                w(f"    - {art['article_title']} [{art['sentiment']}]")

        r4 = report["part4_sector_advice"]
        w(f"\n[4/4] {r4['title']}")
        for rec in r4["recommendations"]:
            w(f"  #{rec['rank']} {rec['name']}({rec['parent_sector']}) [{rec['advice_icon']}] {rec['advice']}")
            w(f"    理由: {rec['reason']}")
            if rec["consistency_note"]:
                w(f"    {rec['consistency_note']}")

        w("\n--- 报告结束 ---")

    print(f"  [TXT]  {txt_path}")


def main():
    report = generate_report()
    save_report(report)
    return report


if __name__ == "__main__":
    main()
