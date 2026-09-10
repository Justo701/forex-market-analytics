-- Stage 19: Price Momentum Analysis
-- Measure the direction and strength of daily price movement

USE forex_market_analytics;

WITH price_analysis AS (

    SELECT
        trade_date,
        pair,
        close_price,

        LAG(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
        ) AS previous_close

    FROM forex_prices
)

SELECT
    trade_date,
    pair,
    close_price,

    ROUND(previous_close, 5) AS previous_close,

    ROUND(
        close_price - previous_close,
        5
    ) AS momentum,

    ROUND(
        (
            (close_price - previous_close)
            / previous_close
        ) * 100,
        5
    ) AS momentum_percentage,

    CASE

        WHEN close_price > previous_close
            THEN 'Positive'

        WHEN close_price < previous_close
            THEN 'Negative'

        ELSE 'Neutral'

    END AS momentum_status

FROM price_analysis

ORDER BY pair, trade_date;
