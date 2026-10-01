import os
from fastapi import FastAPI
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .db import init_db
from .simulator import hours_of_life, simulate_purchase

app = FastAPI(title="Hindsight API")


@app.get("/firebase-config")
def firebase_config() -> dict:
    return {
        "apiKey": os.environ.get("FIREBASE_API_KEY", ""),
        "authDomain": "hindsight-ff311.firebaseapp.com",
        "projectId": "hindsight-ff311",
        "storageBucket": "hindsight-ff311.firebasestorage.app",
        "messagingSenderId": "672088526093",
        "appId": "1:672088526093:web:3e19698058a2a19b773444",
    }


@app.on_event("startup")
def startup() -> None:
    init_db()


class SimulateRequest(BaseModel):
    price: float = Field(gt=0)
    projected_month_end_balance: float
    goal_monthly_contribution: float = Field(ge=0)
    monthly_income: float = Field(gt=0)
    work_hours_per_month: float = Field(default=160, gt=0)
    category_budget_remaining: float | None = None


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/hours-of-life")
def hours(price: float, monthly_income: float, work_hours_per_month: float = 160) -> dict:
    return {"hours": hours_of_life(price, monthly_income, work_hours_per_month)}


@app.post("/simulate")
def simulate(req: SimulateRequest) -> dict:
    return simulate_purchase(**req.model_dump()).__dict__

app.mount("/", StaticFiles(directory=Path(__file__).parent.parent / "static", html=True), name="static")