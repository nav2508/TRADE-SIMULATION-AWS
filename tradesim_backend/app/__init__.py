from flask import Flask
from flask_cors import CORS
from app.models import db
from app.routes import (
    auth_bp, market_bp, portfolio_bp,
    trade_bp, strategy_bp, analytics_bp, compliance_bp
)

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register route blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(market_bp, url_prefix='/api/market')
    app.register_blueprint(portfolio_bp, url_prefix='/api/portfolio')
    app.register_blueprint(trade_bp, url_prefix='/api/trade')
    app.register_blueprint(strategy_bp, url_prefix='/api/strategy')
    app.register_blueprint(analytics_bp, url_prefix='/api/analytics')
    app.register_blueprint(compliance_bp, url_prefix='/api/compliance')

    return app
