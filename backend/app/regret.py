"""Regret statistics: plain, explainable group stats (no ML until there is enough data)."""
from collections import defaultdict

MIN_SAMPLES = 3


def time_bucket(hour: int | None) -> str:
    if hour is None:
        return "unknown"
    return "late_night" if hour >= 22 or hour < 5 else "daytime"


def regret_stats(rows: list[dict], min_samples: int = MIN_SAMPLES) -> dict:
    """rows: [{'category': str, 'hour': int|None, 'rating': 'worth_it'|'meh'|'regret'}]"""
    groups: dict[tuple, list[str]] = defaultdict(list)
    for r in rows:
        groups[(r["category"], time_bucket(r.get("hour")))].append(r["rating"])

    stats = {}
    for (category, bucket), ratings in groups.items():
        if len(ratings) < min_samples:
            continue  # not enough data: stay quiet instead of over-claiming
        stats[(category, bucket)] = {
            "n": len(ratings),
            "regret_rate": round(ratings.count("regret") / len(ratings), 2),
        }
    return stats


def warning_for(category: str, hour: int | None, rows: list[dict], threshold: float = 0.6) -> str | None:
    stats = regret_stats(rows).get((category, time_bucket(hour)))
    if stats and stats["regret_rate"] >= threshold:
        pct = int(stats["regret_rate"] * 100)
        return f"You regretted {pct}% of your last {stats['n']} {category} purchases at this time of day."
    return None
