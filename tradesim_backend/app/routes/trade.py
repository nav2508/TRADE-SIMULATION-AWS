from flask import Blueprint, request, jsonify
from app.models import Trade, Portfolio, ComplianceEvent, db
from app.utils.alert import send_alert
from datetime import datetime

trade_bp = Blueprint('trade', __name__)

@trade_bp.route('/place', methods=['POST'])
def place_trade():
    data = request.get_json()
    user_id = data.get('user_id')
    symbol = data.get('symbol')
    trade_type = data.get('type')  # BUY or SELL
    quantity = int(data.get('quantity'))
    price = float(data.get('price'))

    portfolio = Portfolio.query.filter_by(user_id=user_id).first()
    if not portfolio:
        return jsonify({"error": "Portfolio not found"}), 404

    holdings = portfolio.holdings or {}
    total_cost = round(quantity * price, 2)

    # Handle BUY
    if trade_type == "BUY":
        if portfolio.cash < total_cost:
            return jsonify({"error": "Insufficient cash"}), 400
        portfolio.cash -= total_cost
        holdings[symbol] = holdings.get(symbol, 0) + quantity

    # Handle SELL
    elif trade_type == "SELL":
        if holdings.get(symbol, 0) < quantity:
            return jsonify({"error": "Insufficient holdings"}), 400
        portfolio.cash += total_cost
        holdings[symbol] -= quantity
        if holdings[symbol] == 0:
            del holdings[symbol]
    else:
        return jsonify({"error": "Invalid trade type"}), 400

    # Update holdings
    portfolio.holdings = holdings

    # Record trade
    new_trade = Trade(
        user_id=user_id,
        symbol=symbol,
        trade_type=trade_type,
        quantity=quantity,
        price=price,
        timestamp=datetime.utcnow()
    )
    db.session.add(new_trade)
    db.session.commit()

    # Trigger risk alert (example)
    if trade_type == "BUY" and total_cost > 5000:
        send_alert(f"Large BUY Order Alert: {symbol} ${total_cost}")

    return jsonify({"message": "Trade executed successfully"})

@trade_bp.route('/history', methods=['GET'])
def trade_history():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    trades = Trade.query.filter_by(user_id=user_id).order_by(Trade.timestamp.desc()).all()
    trade_log = [{
        "symbol": t.symbol,
        "type": t.trade_type,
        "quantity": t.quantity,
        "price": t.price,
        "timestamp": t.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    } for t in trades]

    return jsonify({"trades": trade_log})
