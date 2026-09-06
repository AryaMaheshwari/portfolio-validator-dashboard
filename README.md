# 📊 Portfolio Validator & Dashboard

An interactive dashboard that tracks a stock portfolio while making bad data impossible to sneak in — built to learn and apply Pydantic's data validation alongside a Streamlit visual layer.

## The problem

Manually tracked portfolios (spreadsheets, quick scripts) have no real guardrails — a typo'd negative share count or a zero price can silently corrupt calculations. This project enforces valid data at the model level, before it ever enters the system.

## Features

- Add holdings through a simple form (ticker, shares, purchase price, current price)
- **Automatic validation** — shares and prices must be positive; invalid entries are rejected with a clear error message instead of corrupting the data or crashing the app
- **Computed fields** — current value, gain/loss, and gain/loss % are calculated live from the underlying data, never manually set or able to drift out of sync
- Live metric cards: total portfolio value, number of holdings
- Interactive pie chart showing allocation by holding
- Full holdings list with per-position gain/loss shown at a glance (🟢/🔴)

## Tech stack

- **Python**
- **Pydantic** — data validation, computed fields, nested models
- **Streamlit** — interactive web dashboard
- **Plotly** — interactive pie chart

## How it's structured

- `models.py` — `Holding` (a single position, with field-level validation and computed properties for value/gain/loss) and `Portfolio` (holds a list of `Holding` objects, with its own computed total value and an allocation breakdown method)
- `app.py` — the Streamlit interface: a form for adding holdings, validation error handling, metric cards, and the pie chart/holdings list

## What I learned building this

- **Field-level validation** (`Field(gt=0)`) — Pydantic rejects invalid data automatically based on declared constraints, without writing manual `if` checks for every rule
- **Computed fields** (`@computed_field` + `@property`) — values like gain/loss are calculated fresh every time from the source data, rather than being separately stored and risking going out of sync
- **Nested models** — a `Portfolio` containing a list of full `Holding` objects, each with its own independent validation and computed logic
- Wrapping validation errors (`ValidationError`) in a try/except so the UI shows a clean message instead of crashing

## Running it locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/portfolio-validator-dashboard.git
cd portfolio-validator-dashboard

# Create and activate a virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install streamlit plotly pydantic

# Run the app
streamlit run app.py
```

## Live demo

[Add your Streamlit Community Cloud link here once deployed]

## Screenshot

![Portfolio Validator Dashboard](screenshot.png)

*(Add your dashboard screenshot to the repo and update the filename above if needed)*

## What's next

- Persist portfolio data between sessions (JSON or a small database)
- Add historical price tracking and a performance-over-time chart
- Support editing/removing existing holdings
