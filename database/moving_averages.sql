-- Stage 3: Moving Averages
-- 3-Period Moving Average

USE forex_market_analytics;

SELECT
    trade_date,
    pair,
    close_price,

    ROUND(
        AVG(close_price) OVER (
            ORDER BY trade_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        5
    ) AS moving_average

FROM forex_prices

ORDER BY trade_date;
