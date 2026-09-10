-- Stage 23: Multi-Pair Comparison
-- Compare Forex pairs using price and volatility metrics

USE forex_market_analytics;

WITH price_changes AS (

    SELECT
        pair,
        trade_date,
        close_price,

        LAG(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
        ) AS previous_close

    FROM forex_prices
),

pair_analysis AS (

    SELECT
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

    ROUND(AVG(close_price), 5) AS average_price,

    ROUND(MAX(close_price), 5) AS highest_price,

    ROUND(MIN(close_price), 5) AS lowest_price,

    ROUND(
        AVG(ABS(percentage_change)),
        5
    ) AS average_daily_movement,

    ROUND(
        STDDEV(percentage_change),
        5
    ) AS price_volatility

FROM pair_analysis

GROUP BY pair

ORDER BY price_volatility DESC;
