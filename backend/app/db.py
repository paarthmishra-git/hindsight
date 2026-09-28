import os
import sqlite3

DB_PATH = os.getenv("DB_PATH", "hindsight.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    monthly_income REAL NOT NULL,
    work_hours_per_month REAL NOT NULL DEFAULT 160
);
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    date TEXT NOT NULL,          -- ISO date
    hour INTEGER,                -- 0-23, used for time-of-day patterns
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT
);
CREATE TABLE IF NOT EXISTS budgets (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    category TEXT NOT NULL,
    monthly_limit REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    name TEXT NOT NULL,
    target REAL NOT NULL,
    saved REAL NOT NULL DEFAULT 0,
    monthly_contribution REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS regret_ratings (
    id INTEGER PRIMARY KEY,
    transaction_id INTEGER UNIQUE NOT NULL REFERENCES transactions(id),
    rating TEXT NOT NULL CHECK (rating IN ('worth_it', 'meh', 'regret')),
    rated_at TEXT NOT NULL
);
"""


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_conn() as conn:
        conn.executescript(SCHEMA)
