
import numpy as np
import pandas as pd


def run_sma_backtest(
    data,
    fee_bps=5
):
    """
    Long-only SMA20/SMA50 historical backtest.

    Positions use the previous day's signal
    to avoid look-ahead bias.
    """

    df = data.copy()

    df = df.dropna(
        subset=["close", "sma20", "sma50"]
    ).reset_index(drop=True)

    if len(df) < 2:
        raise ValueError(
            "Not enough data for backtesting."
        )

    # Desired position: 1 = invested, 0 = cash
    signal = (
        df["sma20"] > df["sma50"]
    ).astype(int)

    # Execute signal on the following period
    position = signal.shift(1).fillna(0)

    # Daily stock returns
    market_return = df["close"].pct_change().fillna(0)

    # Strategy return before fees
    gross_return = position * market_return

    # Charge fees when position changes
    turnover = position.diff().abs().fillna(0)

    transaction_cost = (
        turnover * fee_bps / 10000
    )

    net_return = gross_return - transaction_cost

    # Equity curves
    strategy_equity = (1 + net_return).cumprod()

    buy_hold_equity = (
        1 + market_return
    ).cumprod()

    # Drawdown
    peak = strategy_equity.cummax()

    drawdown = (
        strategy_equity / peak - 1
    )

    # Annualized Sharpe ratio
    daily_std = net_return.std()

    if daily_std > 0:
        sharpe = (
            np.sqrt(252) *
            net_return.mean() /
            daily_std
        )
    else:
        sharpe = 0.0

    stats = {
        "strategy_return": float(
            strategy_equity.iloc[-1] - 1
        ),
        "buy_hold_return": float(
            buy_hold_equity.iloc[-1] - 1
        ),
        "max_drawdown": float(
            drawdown.min()
        ),
        "sharpe_ratio": float(sharpe),
        "number_of_position_changes": int(
            turnover.sum()
        ),
        "trading_days": len(df)
    }

    result = pd.DataFrame({
        "date": df["date"],
        "strategy_equity": strategy_equity,
        "buy_hold_equity": buy_hold_equity,
        "strategy_return": net_return,
        "position": position
    })

    return stats, result
