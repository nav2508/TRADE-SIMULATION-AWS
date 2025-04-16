import random
import time

class MarketEngine:
    def __init__(self):
        # Initialize mock prices
        self.prices = {
            "AAPL": 150.0,
            "GOOG": 120.0,
            "TSLA": 180.0,
            "AMZN": 130.0
        }

    def update_prices(self):
        """Simulate price movement"""
        for symbol in self.prices:
            change = random.uniform(-2, 2)
            self.prices[symbol] = round(self.prices[symbol] + change, 2)

    def get_prices(self):
        """Return current market prices"""
        self.update_prices()
        return {
            "prices": self.prices,
            "timestamp": int(time.time())
        }

    def get_order_book(self):
        """Return a fake order book for each symbol"""
        book = {}
        for symbol, price in self.prices.items():
            book[symbol] = {
                "bids": [round(price - i * 0.3, 2) for i in range(5)],
                "asks": [round(price + i * 0.3, 2) for i in range(1, 6)]
            }
        return book
