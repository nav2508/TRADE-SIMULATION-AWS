from flask import Blueprint, request, jsonify
from app.models import Portfolio, db
from sqlalchemy.exc import SQLAlchemyError

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/', methods=['GET'])
def get_portfolio():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    portfolio = Portfolio.query.filter_by(user_id=user_id).first()
    if not portfolio:
        return jsonify({"error": "Portfolio not found"}), 404

    return jsonify({
        "cash": round(portfolio.cash, 2),
        "holdings": portfolio.holdings or {}
    })

@portfolio_bp.route('/update', methods=['POST'])
def update_portfolio():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        cash = data.get('cash')
        holdings = data.get('holdings')

        portfolio = Portfolio.query.filter_by(user_id=user_id).first()
        if not portfolio:
            return jsonify({"error": "Portfolio not found"}), 404

        if cash is not None:
            portfolio.cash = cash
        if holdings is not None:
            portfolio.holdings = holdings

        db.session.commit()
        return jsonify({"message": "Portfolio updated successfully"})

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
