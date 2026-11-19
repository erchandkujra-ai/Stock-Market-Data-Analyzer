
def add_alert(ticker, rule, threshold):

    # Create database tables first
    initialize_database()

    alert_id = str(uuid.uuid4())

    ticker = ticker.upper()

    with get_connection() as connection:

        connection.execute(
            """
            INSERT INTO alerts (
                id,
                ticker,
                rule,
                threshold,
                active
            )
            VALUES (?, ?, ?, ?, 1)
            """,
            (
                alert_id,
                ticker,
                rule,
                threshold
            )
        )

    print(f"Alert created successfully: {ticker}")

    return alert_id
