# Hindsight

An expense tracker that shows what a purchase really costs **before** you make it, and learns from what you regret.

## Core features
- **Future Me simulator:** month-end balance, budget and goal impact of a planned purchase
- **Hours of Life:** every price expressed as hours of your work
- **Regret Score:** post-purchase check-ins feed warnings into future simulations

## Design decisions
- All money math is deterministic Python; the LLM only categorizes transactions and phrases explanations
- Regret insights use plain group statistics with a minimum sample size, and stay quiet when data is thin

## Run
```bash
cd backend
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload
```

## Roadmap
- [x] Schema, simulator, hours of life, regret stats, tests
- [ ] Auth + CSV import + AI categorization
- [ ] Dashboard (React + Recharts)
- [ ] Regret check-in flow
- [ ] Demo mode with seeded data, deploy
