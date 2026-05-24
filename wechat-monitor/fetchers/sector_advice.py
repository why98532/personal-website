"""
Part 4: 前五大细分板块建议（标注一致性）
基于热力板块拆分的细分方向，给出增持/持有/减持建议
动态匹配 Part 3 的真实作者观点，若建议方向与某作者倾向一致则标注

数据来源：mock_market_data.json + 动态传入的作者观点
"""

import json
import os
from typing import Optional, List, Dict

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

# 建议方向 ↔ 作者观点倾向映射
ADVICE_TO_SENTIMENT = {"增持": "看多", "持有": None, "减持": "看空"}


def _load_sub_sectors() -> list[dict]:
    path = os.path.join(DATA_DIR, "mock_market_data.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("sub_sectors", [])


def _advice_icon(advice: str) -> str:
    return {"增持": "BUY", "持有": "HOLD", "减持": "SELL"}.get(advice, advice)


def _match_author(advice: str, authors: List[dict]) -> str:
    """在作者列表中找与建议方向一致的作者名"""
    target = ADVICE_TO_SENTIMENT.get(advice)
    if not target:
        return ""
    for a in authors:
        if a.get("dominant_sentiment") == target:
            return a["author_name"]
    return ""


def fetch(authors: Optional[List[dict]] = None) -> dict:
    if authors is None:
        authors = []

    items = _load_sub_sectors()
    # 按倾向分组：看多/看空 作者列表，循环分配确保均匀覆盖
    bullish_authors = [a["author_name"] for a in authors if a.get("dominant_sentiment") == "看多"]
    bearish_authors = [a["author_name"] for a in authors if a.get("dominant_sentiment") == "看空"]
    bull_idx = 0
    bear_idx = 0

    results = []
    for i, item in enumerate(items, 1):
        ca = ""
        target = ADVICE_TO_SENTIMENT.get(item["advice"])
        if target == "看多" and bullish_authors:
            ca = bullish_authors[bull_idx % len(bullish_authors)]
            bull_idx += 1
        elif target == "看空" and bearish_authors:
            ca = bearish_authors[bear_idx % len(bearish_authors)]
            bear_idx += 1

        entry = {
            "rank": i,
            "name": item["name"],
            "parent_sector": item["parent"],
            "advice": item["advice"],
            "advice_icon": _advice_icon(item["advice"]),
            "reason": item["reason"],
        }
        if ca:
            entry["consistency_note"] = f"[与作者{ca}一致]"
        else:
            entry["consistency_note"] = ""
        results.append(entry)

    return {
        "title": "前五大细分板块建议（标注一致性）",
        "recommendations": results,
    }


if __name__ == "__main__":
    import pprint
    pprint.pprint(fetch())
