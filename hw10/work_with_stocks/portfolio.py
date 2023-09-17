"""Calculation of financial indicators of a stock portfolio

"""
import math


class Portfolio:

    def __init__(self, stocks, init_prices, init_val, current_val):
        self.stocks = stocks
        self._initial_portfolio_prices = init_prices
        self.initial_value = init_val
        self.current_value = current_val

    def calculate_portfolio_value(self, current_prices) -> float:
        """Calculating the total value of a stock portfolio.

        Example:
            In:
                stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
                prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
            Out:
                16410,25
        :param stocks: dict, where the keys: stock symbols (e.g. 'AAPL'),
            and values the number of shares of each symbol.
        :param current_prices: dictionary where the keys are stock symbols, and
            values - the current price of each share.
        :return: float. The total value of a stock portfolio based on the
            number of shares and their current prices.
        """
        return sum(list(
            map(lambda x, y: x * y,
                self.stocks.values(),
                current_prices.values())))

    def calculate_portfolio_return(self) -> float:
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
        return (self.current_value - self.initial_value) / 100

    def get_most_profitable_stock(self, changed_prices: dict) -> str:
        """Determining the most profitable stock.

        Example:
            In:
                stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
                prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
            Out:
                MSFT

        :param stocks: dict. Dictionary with stocks and their quantity.
        :param changed_prices: dict. Dictionary with stocks and their
            current prices.
        :return: str. The stock symbol (key) that has the highest profit
            compared to its initial cost.
        """
        # {'AAPL': 5.0, 'GOOGL': 100.0, 'MSFT': 500.0}
        profits = {k: v for k, v in
                   zip(self.stocks.keys(),
                       map(lambda x, y: math.fabs(x - y),
                           changed_prices.values(),
                           self._initial_portfolio_prices.values()))}

        # 'MSFT'
        return max(profits, key=profits.get)


if __name__ == '__main__':
    stocks_1 = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices_1 = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

    portfolio = Portfolio(stocks_1, prices_1, 10_000, 15_000)

    new_prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

    print(portfolio.calculate_portfolio_value(new_prices))
    print(portfolio.calculate_portfolio_return())
    print(portfolio.get_most_profitable_stock(new_prices))
