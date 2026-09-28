"""Deterministic finance math. The LLM never does arithmetic; it only explains these results."""
from dataclasses import dataclass


def hours_of_life(price: float, monthly_income: float, work_hours_per_month: float = 160) -> float:
    """How many working hours a purchase costs."""
    if monthly_income <= 0 or work_hours_per_month <= 0:
        raise ValueError("income and work hours must be positive")
    hourly_rate = monthly_income / work_hours_per_month
    return round(price / hourly_rate, 1)


@dataclass
class SimulationResult:
    month_end_before: float
    month_end_after: float
    goal_delay_months: float
    budget_remaining_after: float | None
    hours_of_life: float


def simulate_purchase(
    price: float,
    projected_month_end_balance: float,
    goal_monthly_contribution: float,
    monthly_income: float,
    work_hours_per_month: float = 160,
    category_budget_remaining: float | None = None,
) -> SimulationResult:
    """
    Free cash = projected month-end balance minus the planned goal contribution.
    A purchase is paid from free cash first; only the shortfall delays the goal.
    """
    free_cash = projected_month_end_balance - goal_monthly_contribution
    shortfall = max(0.0, price - free_cash)
    delay = shortfall / goal_monthly_contribution if goal_monthly_contribution > 0 else 0.0

    return SimulationResult(
        month_end_before=projected_month_end_balance,
        month_end_after=projected_month_end_balance - price,
        goal_delay_months=round(delay, 2),
        budget_remaining_after=(
            category_budget_remaining - price if category_budget_remaining is not None else None
        ),
        hours_of_life=hours_of_life(price, monthly_income, work_hours_per_month),
    )
