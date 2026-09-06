import streamlit as st
import plotly.express as px
from pydantic import ValidationError
from models import Holding, Portfolio

st.title("📊 Portfolio Validator & Dashboard")

if "portfolio" not in st.session_state:
    st.session_state.portfolio = Portfolio()

portfolio = st.session_state.portfolio

with st.form("add_holding_form"):
    ticker = st.text_input("Ticker (e.g. AAPL)")
    shares = st.number_input("Shares", step=1.0)
    purchase_price = st.number_input("Purchase Price ($)", step=1.0)
    current_price = st.number_input("Current Price ($)", step=1.0)
    submitted = st.form_submit_button("Add Holding")

    if submitted:
        try:
            new_holding = Holding(
                ticker=ticker,
                shares=shares,
                purchase_price=purchase_price,
                current_price=current_price
            )
            portfolio.holdings.append(new_holding)
            st.success(f"Added {ticker}!")
        except ValidationError as e:
            st.error(f"Invalid entry — please check your inputs:\n{e}")

col1, col2 = st.columns(2)
col1.metric("Total Portfolio Value", f"${portfolio.total_value:,.2f}")
col2.metric("Number of Holdings", len(portfolio.holdings))

if portfolio.holdings:
    allocation = portfolio.allocation_by_ticker()
    fig = px.pie(values=list(allocation.values()), names=list(allocation.keys()), title="Allocation by Holding")
    st.plotly_chart(fig)

    st.subheader("Your Holdings")
    for h in portfolio.holdings:
        gain_color = "🟢" if h.gain_loss >= 0 else "🔴"
        st.write(f"**{h.ticker}** — {h.shares} shares @ ${h.current_price} | Value: ${h.current_value:,.2f} | {gain_color} ${h.gain_loss:,.2f} ({h.gain_loss_percent}%)")