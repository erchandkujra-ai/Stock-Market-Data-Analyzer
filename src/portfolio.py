
import uuid
import pandas as pd

from src.database import (
    get_connection,
    initialize_database
)


def add_transaction(
    ticker,
    side,
    quantity,
    price,
    fees=0
):

    side = side.upper()
    ticker = ticker.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if quantity <= 0 or price <= 0 or fees < 0:
        raise ValueError("Invalid transaction values")

    initialize_database()

    transaction_id = str(uuid.uuid4())

    with get_connection() as connection:

        if side == "SELL":

            current = get_positions()

            position = current[
                current["ticker"] == ticker
            ]

            available = (
                float(position.iloc[0]["quantity"])
                if not position.empty
                else 0
            )

            if quantity > available:
                raise ValueError(
                    "Cannot sell more shares than held."
                )

        connection.execute(
            """
            INSERT INTO portfolio_tx
            (id, ticker, ts, side, qty, price, fees)
            VALUES (?, ?, datetime('now'), ?, ?, ?, ?)
            """,
            (
                transaction_id,
                ticker,
                side,
                quantity,
                price,
                fees
            )
        )

    return transaction_id


def get_positions():

    initialize_database()

    with get_connection() as connection:

        transactions = pd.read_sql_query(
            """
            SELECT ticker, side, qty, price, fees
            FROM portfolio_tx
            ORDER BY ts, id
            """,
            connection
        )

    if transactions.empty:

        return pd.DataFrame(
            columns=[
                "ticker",
                "quantity",
                "average_cost"
            ]
        )

    results = []

    for ticker, group in transactions.groupby("ticker"):

        quantity = 0.0
        total_cost = 0.0

        for row in group.itertuples(index=False):

            if row.side == "BUY":

                total_cost += (
                    row.qty * row.price + row.fees
                )

                quantity += row.qty

            else:

                if quantity > 0:

                    average_cost = total_cost / quantity

                    total_cost -= (
                        average_cost * row.qty
                    )

                    quantity -= row.qty

        average_cost = (
            total_cost / quantity
            if quantity > 0
            else 0
        )

        results.append({
            "ticker": ticker,
            "quantity": quantity,
            "average_cost": average_cost
        })

    return pd.DataFrame(results)
