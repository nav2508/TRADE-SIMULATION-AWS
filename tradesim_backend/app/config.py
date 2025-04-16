import os

class Config:
    SECRET_KEY = "supersecuredevkey"  # Replace with a secure env var in prod

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://TradeSimdbuser:Navya2508@tradesimdb.cddleueux1yc.us-east-1.rds.amazonaws.com:5432/postgres"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
