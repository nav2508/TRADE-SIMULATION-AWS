from flask import Blueprint, jsonify
import random
import time

market_bp = Blueprint('market', __name__)

# Simulated price memory
current_prices = {
    "AAPL": 150.0,
    "GOOG": 120.0,
    "TSLA": 180.0,
    "AMZN": 130.0
}

@market_bp.route('/ticker', methods=['GET'])
def ticker():
    # Simulate random price changes
    for symbol in current_prices:
        change = random.uniform(-1, 1)
        current_prices[symbol] = round(current_prices[symbol] + change, 2)
    return jsonify({
        "prices": current_prices,
        "timestamp": int(time.time())
    })

@market_bp.route('/orderbook', methods=['GET'])
def order_book():
    # Fake order book with 5 bid/asks
    book = {}
    for symbol, price in current_prices.items():
        book[symbol] = {
            "bids": [round(price - i * 0.2, 2) for i in range(5)],
            "asks": [round(price + i * 0.2, 2) for i in range(1, 6)]
        }
    return jsonify(book)
