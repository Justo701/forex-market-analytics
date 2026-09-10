-- Stage 18: Trend Analysis
-- Classify price direction and moving-average trend

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
),

moving_averages AS (

    SELECT
        trade_date,
        pair,
        close_price,
        previous_close,

        AVG(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS ma_3,

        AVG(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
            ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
        ) AS ma_5

    FROM price_analysis
)

SELECT
    trade_date,
    pair,
    close_price,

    ROUND(previous_close, 5) AS previous_close,
    ROUND(ma_3, 5) AS ma_3,
    ROUND(ma_5, 5) AS ma_5,

    CASE

        WHEN close_price > previous_close
             AND ma_3 > ma_5
            THEN 'Uptrend'

        WHEN close_price < previous_close
             AND ma_3 < ma_5
            THEN 'Downtrend'

        ELSE 'Sideways'

    END AS trend

FROM moving_averages

ORDER BY pair, trade_date;
