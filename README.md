# Hindsight

**An expense tracker that shows what a purchase really costs *before* you make it.**

Most money apps give you hindsight after the money is gone. Hindsight gives it to you up front: every price becomes hours of your working life, and a simulator shows what the purchase does to your month and your savings goal.

**Live demo:** https://hindsight-4w7d.onrender.com

> The demo runs on a free plan, so the first load after a quiet spell can take a minute while it wakes up.

---

## What it does

| Feature | What you get | Status |
|---|---|---|
| **Hours of Life** | Any price converted into hours of your working month | Live |
| **Future Me simulator** | Month-end balance after the purchase, and how far it pushes back your savings goal | Live |
| **Regret Score** | Rate purchases a few days later; the app learns which categories and times of day you regret | Logic and tests done, UI in progress |
| **Smart import** | Upload a bank CSV and auto-categorize transactions | Planned |

## How the numbers work

All money math is plain, deterministic Python (no AI does arithmetic), so results are predictable and testable.

- **Hours of Life** = `price ÷ (monthly income ÷ working hours per month)`
- **Future Me simulator:**
  - *Free cash* = projected month-end balance − monthly savings goal contribution
  - A purchase is paid from free cash first. Only the **shortfall** delays your goal:
  - *Goal delay (months)* = `shortfall ÷ monthly goal contribution`
- **Regret statistics** use simple group rates (per category and time of day) with a minimum sample size, so the app stays quiet instead of over-claiming when data is thin.

## Tech stack

- **Backend:** Python, FastAPI, Pydantic
- **Frontend:** a single HTML/CSS/JS page served by the same FastAPI app (no build step)
- **Database:** SQLite schema for users, transactions, budgets, goals and regret ratings
- **Tests:** pytest
- **Hosting:** Render, auto-deployed from `main`

## API

Interactive docs are at `/docs` on the live app.

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/hours-of-life` | Convert a price to hours of work |
| POST | `/simulate` | Run the Future Me simulation |

Example request:

```json
POST /simulate
{
  "price": 8000,
  "projected_month_end_balance": 6000,
  "goal_monthly_contribution": 5000,
  "monthly_income": 40000
}
```

Example response:

```json
{
  "month_end_before": 6000,
  "month_end_after": -2000,
  "goal_delay_months": 1.4,
  "budget_remaining_after": null,
  "hours_of_life": 32
}
```

## Run it locally

```bash
git clone https://github.com/paarthmishra-git/hindsight.git
cd hindsight/backend

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac / Linux

pip install -r requirements.txt pytest
pytest                        # run the tests
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000.

## Project structure

```
hindsight/
├── README.md
└── backend/
    ├── requirements.txt
    ├── app/
    │   ├── main.py         # FastAPI routes + serves the frontend
    │   ├── simulator.py    # Hours of Life and Future Me math
    │   ├── regret.py       # Regret statistics and warnings
    │   └── db.py           # SQLite schema
    ├── static/
    │   └── index.html      # The frontend
    └── tests/
        └── test_core.py
```

## Design decisions

- **Deterministic core.** The financial math lives in code, not in a language model, so it is exact and testable. An LLM is planned only for categorizing messy bank data and phrasing explanations.
- **One service.** FastAPI serves both the API and the page, so the whole app deploys as a single unit.
- **Honest insights.** Regret warnings need a minimum number of ratings before they appear.

## Roadmap

- [x] Hours of Life and Future Me simulator
- [x] Regret statistics with tests
- [x] Responsive frontend, light and dark mode
- [x] Deployed with auto-deploy on push
- [ ] Regret check-in flow (rate a purchase a few days later)
- [ ] CSV import with automatic categorization
- [ ] Accounts and persistent storage
- [ ] Demo mode with sample data
