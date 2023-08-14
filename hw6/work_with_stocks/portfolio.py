"""Calculation of financial indicators of a stock portfolio

"""
_initial_portfolio_prices = dict()


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    """Calculating the total value of a stock portfolio.

    Example:
        In:
            stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
            prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
        Out:
            16410,25
    :param stocks: dict, where the keys: stock symbols (e.g. 'AAPL'),
        and values the number of shares of each symbol.
    :param prices: dictionary where the keys are stock symbols, and
        values - the current price of each share.
    :return: float. The total value of a stock portfolio based on the
        number of shares and their current prices.
    """
    global _initial_portfolio_prices
    _initial_portfolio_prices.update(prices)

    return sum(list(
        map(lambda x, y: x * y, stocks.values(), prices.values())))


def calculate_portfolio_return(initial_value: float,
                               current_value: float) -> float:
    """Calculation of the return on a stock portfolio.

    Example:
        In:
            10000.0
            15000.0
        Out:
            50%
    :param initial_value: float. The initial value of the stock
        portfolio.
    :param current_value: float. The current value of the stock
        portfolio.
    :return: float. The function should return the interest yield of the
        portfolio.
    """
    return (current_value - initial_value) / 100


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    """Determining the most profitable stock.

    Example:
        In:
            stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
            prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
        Out:
            MSFT

    :param stocks: dict. Dictionary with stocks and their quantity.
    :param prices: dict. Dictionary with stocks and their current prices.
    :return: str. The stock symbol (key) that has the highest profit
        compared to its initial cost.
    """
    global _initial_portfolio_prices

    # {'AAPL': 5.0, 'GOOGL': 100.0, 'MSFT': 500.0}
    profits = {k: v for k, v in
               zip(stocks.keys(), map(lambda x, y: x - y, prices.values(),
                                      _initial_portfolio_prices.values()))}

    # print(_initial_portfolio_prices)
    # 'MSFT'
    return max(profits, key=profits.get)


if __name__ == '__main__':
    stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

    print(calculate_portfolio_value(stocks, {
        "AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}))
    print(calculate_portfolio_return(10_000, 15_000))
    print(_initial_portfolio_prices)
    print(get_most_profitable_stock(stocks, prices))
