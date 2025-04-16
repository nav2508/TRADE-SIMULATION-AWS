from flask import Blueprint, request, jsonify
from app.models import Trade
from datetime import datetime
import math

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/performance', methods=['GET'])
def performance():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    trades = Trade.query.filter_by(user_id=user_id).order_by(Trade.timestamp.asc()).all()
    if not trades:
        return jsonify({"message": "No trades found"}), 404

    total_trades = len(trades)
    win_trades = 0
    loss_trades = 0
    returns = []
    total_return = 0

    for trade in trades:
        # Simple P&L simulation
        mock_current_price = trade.price + (5 if trade.trade_type == "BUY" else -5)
        profit = (mock_current_price - trade.price) * trade.quantity if trade.trade_type == "BUY" else 0

        returns.append(profit)
        if profit > 0:
            win_trades += 1
        elif profit < 0:
            loss_trades += 1

        total_return += profit

    win_rate = round((win_trades / total_trades) * 100, 2)
    avg_return = round(total_return / total_trades, 2)

    # Mock Sharpe ratio
    mean_return = sum(returns) / len(returns)
    stddev = math.sqrt(sum([(r - mean_return) ** 2 for r in returns]) / len(returns))
    sharpe_ratio = round((mean_return / stddev), 2) if stddev != 0 else 0

    return jsonify({
        "total_trades": total_trades,
        "win_rate": f"{win_rate}%",
        "avg_return_per_trade": avg_return,
        "sharpe_ratio": sharpe_ratio,
        "total_profit": round(total_return, 2)
    })
