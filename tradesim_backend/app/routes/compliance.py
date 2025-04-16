from flask import Blueprint, request, jsonify
from app.models import db, Trade, ComplianceEvent
from datetime import datetime, timedelta

compliance_bp = Blueprint('compliance', __name__)

@compliance_bp.route('/audit', methods=['GET'])
def audit_trades():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID required"}), 400

    trades = Trade.query.filter_by(user_id=user_id).order_by(Trade.timestamp.desc()).all()
    flagged = []

    for i, trade in enumerate(trades):
        # Rule 1: Large trade amount
        if trade.quantity * trade.price > 10000:
            violation = ComplianceEvent(
                user_id=user_id,
                trade_id=trade.id,
                violation="Trade exceeds $10,000 threshold"
            )
            db.session.add(violation)
            flagged.append({
                "trade_id": trade.id,
                "violation": "Trade exceeds $10,000 threshold"
            })

        # Rule 2: Pattern trading (same stock within short time)
        if i < len(trades) - 1:
            next_trade = trades[i + 1]
            if trade.symbol == next_trade.symbol:
                time_diff = trade.timestamp - next_trade.timestamp
                if time_diff < timedelta(minutes=5):
                    violation = ComplianceEvent(
                        user_id=user_id,
                        trade_id=trade.id,
                        violation="Pattern trading detected (multiple trades within 5 minutes)"
                    )
                    db.session.add(violation)
                    flagged.append({
                        "trade_id": trade.id,
                        "violation": "Pattern trading (within 5 minutes)"
                    })

    db.session.commit()

    return jsonify({
        "message": f"{len(flagged)} compliance issues detected",
        "violations": flagged
    })


@compliance_bp.route('/violations', methods=['GET'])
def get_violations():
    user_id = request.args.get('user_id')
    violations = ComplianceEvent.query.filter_by(user_id=user_id).all()

    output = [{
        "trade_id": v.trade_id,
        "violation": v.violation,
        "timestamp": v.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    } for v in violations]

    return jsonify({"violations": output})
