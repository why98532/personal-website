"""
Part 1: 近一周市场重大事件摘要
数据来源：mock_market_data.json（可扩展为从新浪财经/东方财富爬取）
"""

import json
import os
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def _load_mock_events() -> list[dict]:
    path = os.path.join(DATA_DIR, "mock_market_data.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("market_events", [])


def _filter_recent_week(events: list[dict]) -> list[dict]:
    cutoff = datetime.now() - timedelta(days=7)
    recent = []
    for e in events:
        try:
            d = datetime.strptime(e["date"], "%Y-%m-%d")
            if d >= cutoff:
                recent.append(e)
        except ValueError:
            recent.append(e)
    return recent


def _sentiment_label(s: str) -> str:
    return {"bullish": "看涨", "bearish": "看跌", "neutral": "中性"}.get(s, s)


def _overall_sentiment(events: list[dict]) -> str:
    bulls = sum(1 for e in events if e["sentiment"] == "bullish")
    bears = sum(1 for e in events if e["sentiment"] == "bearish")
    if bulls > bears:
        return "看涨 (偏多)"
    elif bears > bulls:
        return "看跌 (偏空)"
    return "中性 (震荡)"


def _shift_to_recent(events: list[dict]) -> list[dict]:
    """将模拟数据中的固定日期平移为近7天的日期"""
    if not events:
        return events
    today = datetime.now().date()
    base_date = None
    for e in events:
        try:
            d = datetime.strptime(e["date"], "%Y-%m-%d").date()
            if base_date is None or d > base_date:
                base_date = d
        except ValueError:
            pass
    if base_date is None:
        return events
    delta = today - base_date
    result = []
    for e in events:
        try:
            d = datetime.strptime(e["date"], "%Y-%m-%d").date()
            new_date = (d + delta).strftime("%Y-%m-%d")
            result.append({**e, "date": new_date})
        except ValueError:
            result.append(e)
    return result


def fetch() -> dict:
    mock_events = _load_mock_events()
    shifted = _shift_to_recent(mock_events)
    events = _filter_recent_week(shifted)
    return {
        "title": "近一周市场重大事件摘要",
        "events": [
            {"date": e["date"], "event": e["event"], "sentiment": _sentiment_label(e["sentiment"])}
            for e in events
        ],
        "overall_sentiment": _overall_sentiment(events),
    }


if __name__ == "__main__":
    import pprint
    pprint.pprint(fetch())
