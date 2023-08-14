from hw6.work_with_stocks import portfolio as p

INIT_VALUE = 10_000
CURRENT_VALUE = 15_000
STOCKS = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
PRICES = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
CURRENT_PRICES = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

print('Initial stocks and their quantity:')
for stock, quantity in STOCKS.items():
    print(f'Stock: {stock}. Quantity: {quantity}. '
          f'Price per stock: {PRICES[stock]}')

print(f'Total value of a stock portfolio: '
      f'{p.calculate_portfolio_value(STOCKS, PRICES)}')

print(f'Init value: {INIT_VALUE}. Current value: {CURRENT_VALUE}.')
print(f'The interest yield of the portfolio: '
      f'{p.calculate_portfolio_return(INIT_VALUE, CURRENT_VALUE)}%')

print(f"The most profitable stock in portfolio: "
      f"{p.get_most_profitable_stock(STOCKS, CURRENT_PRICES)}")
