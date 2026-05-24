"""
Part 2: 当前热度前10大板块及其标的现状
数据来源：mock_market_data.json（可扩展为 akshare 实时数据）
"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def _load_mock_sectors() -> list[dict]:
    path = os.path.join(DATA_DIR, "mock_market_data.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("sectors", [])


def _format_stock(s: dict) -> str:
    sign = "+" if s["change_pct"] >= 0 else ""
    return f"{s['code']} {s['name']}  {s['price']:.2f}  ({sign}{s['change_pct']:.1f}%)"


def fetch() -> dict:
    sectors = _load_mock_sectors()

    result = []
    heat_rank = 1
    for sec in sectors:
        stocks = sec.get("stocks", [])
        avg_change = sum(s["change_pct"] for s in stocks) / len(stocks) if stocks else 0
        sign = "+" if avg_change >= 0 else ""
        result.append({
            "rank": heat_rank,
            "sector_name": sec["name"],
            "representative_stocks": [{"code": s["code"], "name": s["name"], "price": s["price"], "change_pct": s["change_pct"]} for s in stocks],
            "avg_change_pct": round(avg_change, 2),
            "trend": "上涨" if avg_change > 0 else ("下跌" if avg_change < 0 else "持平"),
        })
        heat_rank += 1

    return {
        "title": "当前热度前10大板块及其标的现状",
        "sectors": result,
    }


if __name__ == "__main__":
    import pprint
    pprint.pprint(fetch())
