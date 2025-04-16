from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    cash = db.Column(db.Float, default=100000.0)
    holdings = db.Column(db.JSON, default={})  # { "AAPL": 10, "TSLA": 5 }

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    trade_type = db.Column(db.String(4), nullable=False)  # BUY / SELL
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Strategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100))
    conditions = db.Column(db.JSON)  # e.g. {"symbol": "AAPL", "rule": "price < 150"}

class ComplianceEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    trade_id = db.Column(db.Integer)
    violation = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
