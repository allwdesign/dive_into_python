from portfolio import Portfolio

INIT_VALUE = 10_000
CURRENT_VALUE = 15_000
STOCKS = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
PRICES = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
CURRENT_PRICES = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}


portfolio = Portfolio(STOCKS, PRICES, INIT_VALUE, CURRENT_VALUE)

print('Initial stocks and their quantity:')
for stock, quantity in portfolio.stocks.items():
    print(f'Stock: {stock}. Quantity: {quantity}. '
          f'Price per stock: {PRICES[stock]}')

print(f'Total value of a stock portfolio: '
      f'{portfolio.calculate_portfolio_value(CURRENT_PRICES)}')

print(f'Init value: {INIT_VALUE}. Current value: {CURRENT_VALUE}.')
print(f'The interest yield of the portfolio: '
      f'{portfolio.calculate_portfolio_return()}%')

print(f"The most profitable stock in portfolio: "
      f"{portfolio.get_most_profitable_stock(CURRENT_PRICES)}")
