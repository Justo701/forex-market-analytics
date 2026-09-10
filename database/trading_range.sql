-- Stage 20: Trading Range Analysis
-- Calculate rolling high, low, range size,
-- and current price position within the range

USE forex_market_analytics;

WITH trading_ranges AS (

    SELECT
        trade_date,
        pair,
        close_price,

        MAX(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
            ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
        ) AS range_high,

        MIN(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
            ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
        ) AS range_low

    FROM forex_prices
)

SELECT
    trade_date,
    pair,
    close_price,

    ROUND(range_high, 5) AS range_high,
    ROUND(range_low, 5) AS range_low,

    ROUND(
        range_high - range_low,
        5
    ) AS range_size,

    ROUND(
        (
            (close_price - range_low)
            / NULLIF(range_high - range_low, 0)
        ) * 100,
        2
    ) AS range_position_percentage

FROM trading_ranges

ORDER BY pair, trade_date;
