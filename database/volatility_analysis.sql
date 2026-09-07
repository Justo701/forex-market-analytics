USE forex_market_analytics;

WITH price_changes AS (
    SELECT
        trade_date,
        pair,
        close_price,

        LAG(close_price) OVER (
            ORDER BY trade_date
        ) AS previous_close

    FROM forex_prices
),
percentage_changes AS (
    SELECT
        trade_date,
        pair,
        close_price,

        (
            (close_price - previous_close)
            / previous_close
        ) * 100 AS percentage_change

    FROM price_changes
)
SELECT
    pair,

    ROUND(
        AVG(percentage_change),
        5
    ) AS average_daily_change,

    ROUND(
        AVG(ABS(percentage_change)),
        5
    ) AS average_daily_movement,

    ROUND(
        VARIANCE(percentage_change),
        5
    ) AS daily_variance,

    ROUND(
        STDDEV(percentage_change),
        5
    ) AS daily_volatility

FROM percentage_changes

GROUP BY pair;
