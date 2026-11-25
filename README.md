# Expense Tracker API

![CI](https://github.com/BrandonCarp/expense-tracker-api/actions/workflows/ci.yml/badge.svg)

A REST API for tracking personal expenses by category, with strict per-user data isolation.

## Stack

Python 3.13, FastAPI, SQLAlchemy, PostgreSQL 16, Docker Compose, pytest, ruff, GitHub Actions.

## Running locally

```
git clone https://github.com/BrandonCarp/expense-tracker-api.git
cd expense-tracker-api
cp .env.example .env     # fill in your values
docker compose up
```

The API serves on `http://localhost:8000`. Interactive docs at `/docs`.

## Tests

```
python -m pytest
```

Or against the built image, which also verifies a clean dependency install:

```
docker compose run --rm --no-deps api python -m pytest
```

## Design decisions

1. Categories are per-user, not global — `categories.user_id`.
2. Money is `Numeric(12, 2)`, never a float. Floats lose cents.
3. An expense carries a business date (`DATE`, no time) and every table carries `created_at` as `TIMESTAMPTZ` for system time. They answer different questions.
4. Amount, category and date are required; description is optional. Rows stay editable after creation.
5. v1 deletes are permanent. Deleting a user removes their expenses and categories, enforced by the database rather than application code. A soft-delete flag is v2.
6. Every expense has a category. Each user gets an "Uncategorized" category at signup, and deleting a category reassigns its expenses there rather than orphaning them.
7. That reassignment can't be expressed as a foreign key action, so it lives in the delete endpoint as reassign-then-delete in one transaction. The foreign key uses `ondelete="RESTRICT"` as a backstop: if the application logic ever fails, the database refuses the delete instead of losing data.
8. Category names are unique per user, not globally — two people can both have "Gas".
9. `DATABASE_URL` is read in exactly one place and raises at import if it's missing, so a misconfigured environment fails at startup instead of mid-query.

## What's next

An analysis layer that reads income, recurring bills and spending history and produces a savings plan — deterministic math in code, with the model used for judgment rather than arithmetic.