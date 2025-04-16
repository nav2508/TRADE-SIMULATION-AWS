import math

def compute_performance(trades):
    total_trades = len(trades)
    win_trades = 0
    loss_trades = 0
    returns = []
    total_return = 0

    for t in trades:
        simulated_exit_price = t.price + (5 if t.trade_type == "BUY" else -5)
        pnl = (simulated_exit_price - t.price) * t.quantity if t.trade_type == "BUY" else 0
        returns.append(pnl)

        if pnl > 0:
            win_trades += 1
        elif pnl < 0:
            loss_trades += 1

        total_return += pnl

    win_rate = round((win_trades / total_trades) * 100, 2) if total_trades else 0
    avg_return = round(total_return / total_trades, 2) if total_trades else 0

    mean_return = sum(returns) / total_trades if total_trades else 0
    stddev = math.sqrt(sum([(r - mean_return) ** 2 for r in returns]) / total_trades) if total_trades else 1
    sharpe_ratio = round(mean_return / stddev, 2) if stddev != 0 else 0

    return {
        "total_trades": total_trades,
        "win_rate": f"{win_rate}%",
        "avg_return_per_trade": avg_return,
        "sharpe_ratio": sharpe_ratio,
        "total_profit": round(total_return, 2)
    }
