from flask import Blueprint, request, jsonify
from app.models import db, Strategy, Portfolio, Trade
from datetime import datetime
import random

strategy_bp = Blueprint('strategy', __name__)

@strategy_bp.route('/save', methods=['POST'])
def save_strategy():
    data = request.get_json()
    user_id = data.get('user_id')
    name = data.get('name')
    conditions = data.get('conditions')  # Ex: {"symbol": "AAPL", "rule": "price < 150"}

    if not all([user_id, name, conditions]):
        return jsonify({"error": "Missing strategy fields"}), 400

    strategy = Strategy(user_id=user_id, name=name, conditions=conditions)
    db.session.add(strategy)
    db.session.commit()

    return jsonify({"message": "Strategy saved", "strategy_id": strategy.id})


@strategy_bp.route('/list', methods=['GET'])
def list_strategies():
    user_id = request.args.get('user_id')
    strategies = Strategy.query.filter_by(user_id=user_id).all()

    result = [{
        "id": s.id,
        "name": s.name,
        "conditions": s.conditions
    } for s in strategies]

    return jsonify(result)


@strategy_bp.route('/execute', methods=['GET'])
def execute_strategies():
    """
    Simulates the evaluation and execution of all strategies.
    Executes trades if conditions are met.
    """
    all_strategies = Strategy.query.all()
    results = []

    for strategy in all_strategies:
        rule = strategy.conditions
        symbol = rule.get("symbol")
        price_threshold = rule.get("price")
        comparison = rule.get("comparison")  # 'lt' or 'gt'

        # Simulate market price
        mock_price = round(random.uniform(120, 200), 2)
        match = (
            (comparison == "lt" and mock_price < price_threshold)
            or (comparison == "gt" and mock_price > price_threshold)
        )

        if match:
            # Place a mock trade
            portfolio = Portfolio.query.filter_by(user_id=strategy.user_id).first()
            if not portfolio or portfolio.cash < 1000:
                continue

            quantity = 1
            price = mock_price
            symbol = symbol or "AAPL"

            new_trade = Trade(
                user_id=strategy.user_id,
                symbol=symbol,
                trade_type="BUY",
                quantity=quantity,
                price=price,
                timestamp=datetime.utcnow()
            )

            portfolio.cash -= price
            holdings = portfolio.holdings or {}
            holdings[symbol] = holdings.get(symbol, 0) + quantity
            portfolio.holdings = holdings

            db.session.add(new_trade)
            db.session.commit()

            results.append({
                "strategy_id": strategy.id,
                "executed": True,
                "symbol": symbol,
                "price": price,
                "action": "BUY"
            })
        else:
            results.append({
                "strategy_id": strategy.id,
                "executed": False
            })

    return jsonify({"results": results})
