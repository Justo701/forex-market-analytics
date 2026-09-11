"""
Indicator combinations repository.

This module retrieves combined indicator data
from the MariaDB database.
"""

from backend.config.database import get_db_connection


def get_indicator_combinations():
    """
    Retrieve combined EMA and RSI data.

    Returns:
        A list of indicator combination rows.
    """

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
        WITH RECURSIVE price_data AS (

            SELECT
                trade_date,
                pair,
                close_price,

                ROW_NUMBER() OVER (
                    PARTITION BY pair
                    ORDER BY trade_date
                ) AS rn,

                LAG(close_price) OVER (
                    PARTITION BY pair
                    ORDER BY trade_date
                ) AS previous_close

            FROM forex_prices
        ),

        ema_calculation AS (

            SELECT
                trade_date,
                pair,
                close_price,
                rn,
                previous_close,

                close_price AS ema_3,
                close_price AS ema_5

            FROM price_data

            WHERE rn = 1

            UNION ALL

            SELECT
                p.trade_date,
                p.pair,
                p.close_price,
                p.rn,
                p.previous_close,

                (
                    (p.close_price * 0.5)
                    +
                    (e.ema_3 * 0.5)
                ) AS ema_3,

                (
                    (p.close_price * 0.3333333333)
                    +
                    (e.ema_5 * 0.6666666667)
                ) AS ema_5

            FROM ema_calculation AS e

            JOIN price_data AS p
                ON p.pair = e.pair
                AND p.rn = e.rn + 1
        ),

        changes AS (

            SELECT
                trade_date,
                pair,
                close_price,
                ema_3,
                ema_5,

                close_price - previous_close AS price_change

            FROM ema_calculation
        ),

        gain_loss AS (

            SELECT
                trade_date,
                pair,
                close_price,
                ema_3,
                ema_5,

                CASE
                    WHEN price_change > 0
                    THEN price_change
                    ELSE 0
                END AS gain,

                CASE
                    WHEN price_change < 0
                    THEN ABS(price_change)
                    ELSE 0
                END AS loss

            FROM changes
        ),

        rsi_calculation AS (

            SELECT
                trade_date,
                pair,
                close_price,
                ema_3,
                ema_5,

                AVG(gain) OVER (
                    PARTITION BY pair
                    ORDER BY trade_date
                    ROWS BETWEEN 13 PRECEDING AND CURRENT ROW
                ) AS average_gain,

                AVG(loss) OVER (
                    PARTITION BY pair
                    ORDER BY trade_date
                    ROWS BETWEEN 13 PRECEDING AND CURRENT ROW
                ) AS average_loss

            FROM gain_loss
        ),

        indicator_values AS (

            SELECT
                trade_date,
                pair,
                close_price,
                ema_3,
                ema_5,

                CASE
                    WHEN average_loss = 0
                    THEN NULL
                    ELSE
                        100 - (
                            100 / (
                                1 +
                                (
                                    average_gain /
                                    average_loss
                                )
                            )
                        )
                END AS rsi_14

            FROM rsi_calculation
        )

        SELECT
            trade_date,
            pair,
            close_price,

            ROUND(ema_3, 5) AS ema_3,

            ROUND(ema_5, 5) AS ema_5,

            ROUND(rsi_14, 5) AS rsi_14,

            CASE
                WHEN ema_3 > ema_5
                THEN 'UPTREND'

                WHEN ema_3 < ema_5
                THEN 'DOWNTREND'

                ELSE 'NEUTRAL'
            END AS trend,

            CASE
                WHEN rsi_14 > 50
                THEN 'BULLISH'

                WHEN rsi_14 < 50
                THEN 'BEARISH'

                ELSE 'NEUTRAL'
            END AS momentum,

            CASE
                WHEN ema_3 > ema_5
                     AND rsi_14 > 50
                THEN 'BULLISH CONFIRMATION'

                WHEN ema_3 < ema_5
                     AND rsi_14 < 50
                THEN 'BEARISH CONFIRMATION'

                ELSE 'NEUTRAL'
            END AS confirmation

        FROM indicator_values

        ORDER BY
            pair,
            trade_date
        """

        cursor.execute(query)

        return cursor.fetchall()

    finally:

        cursor.close()
        connection.close()
