def evaluate_trade_risk(trade_data):
    """
    Simple risk rules:
    - Disallow trades over $10,000 unless flagged
    - Disallow margin BUYs over 50% of cash (in full version)
    """

    total_value = trade_data['quantity'] * trade_data['price']
    risk_flags = []

    if total_value > 10000:
        risk_flags.append("Trade exceeds $10,000 threshold")

    # Add more advanced risk checks here...
    # For example: cash balance %, volatility detection, position limits

    return risk_flags
