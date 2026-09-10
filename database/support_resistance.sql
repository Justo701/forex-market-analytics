-- Stage 17: Support and Resistance Detection
-- Identify local highs and local lows

USE forex_market_analytics;

WITH price_levels AS (

    SELECT
        trade_date,
        pair,
        close_price,

        LAG(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
        ) AS previous_close,

        LEAD(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
        ) AS next_close

    FROM forex_prices
)

SELECT
    trade_date,
    pair,
    close_price,

    ROUND(previous_close, 5) AS previous_close,
    ROUND(next_close, 5) AS next_close,

    CASE

        WHEN close_price > previous_close
             AND close_price > next_close
            THEN 'Resistance'

        WHEN close_price < previous_close
             AND close_price < next_close
            THEN 'Support'

        ELSE 'No Level'

    END AS price_level

FROM price_levels

ORDER BY pair, trade_date;
