import pytest
from app.simulator import hours_of_life, simulate_purchase
from app.regret import regret_stats, warning_for


def test_hours_of_life():
    # 40,000/month over 160 hrs = 250/hr -> 500 costs 2 hrs
    assert hours_of_life(500, 40000, 160) == 2.0


def test_hours_of_life_rejects_bad_input():
    with pytest.raises(ValueError):
        hours_of_life(500, 0)


def test_purchase_within_free_cash_does_not_delay_goal():
    r = simulate_purchase(2000, 10000, 5000, 40000)
    assert r.goal_delay_months == 0
    assert r.month_end_after == 8000


def test_purchase_beyond_free_cash_delays_goal():
    # free cash = 6000 - 5000 = 1000; price 8000 -> shortfall 7000 -> 1.4 months
    r = simulate_purchase(8000, 6000, 5000, 40000)
    assert r.goal_delay_months == 1.4


def test_regret_needs_min_samples():
    rows = [{"category": "gadgets", "hour": 23, "rating": "regret"}] * 2
    assert regret_stats(rows) == {}


def test_regret_warning_fires():
    rows = [{"category": "food", "hour": 23, "rating": "regret"}] * 4 + [
        {"category": "food", "hour": 23, "rating": "worth_it"}
    ]
    assert "80%" in warning_for("food", 23, rows)
    assert warning_for("food", 13, rows) is None
