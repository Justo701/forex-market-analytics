-- Stage 4: Multiple Moving Averages
-- 3-Period and 5-Period Moving Averages

USE forex_market_analytics;

SELECT
    trade_date,
    pair,
    close_price,

    -- Average of the current row and previous 2 rows
    ROUND(
        AVG(close_price) OVER (
            ORDER BY trade_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        5
    ) AS ma_3,

    -- Average of the current row and previous 4 rows
    ROUND(
        AVG(close_price) OVER (
            ORDER BY trade_date
            ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
        ),
        5
    ) AS ma_5

FROM forex_prices

ORDER BY trade_date;
