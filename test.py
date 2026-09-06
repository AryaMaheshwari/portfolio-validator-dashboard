from models import Holding, Portfolio

h1 = Holding(ticker="AAPL", shares=10, purchase_price=150, current_price=180)
h2 = Holding(ticker="TSLA", shares=5, purchase_price=200, current_price=190)

portfolio = Portfolio(holdings=[h1, h2])

print(portfolio.total_value)
print(portfolio.allocation_by_ticker())
print(h1.gain_loss, h1.gain_loss_percent)

# Now test that validation actually catches a bad input
try:
    bad_holding = Holding(ticker="XXX", shares=-5, purchase_price=100, current_price=100)
except Exception as e:
    print("Validation caught it:", e)