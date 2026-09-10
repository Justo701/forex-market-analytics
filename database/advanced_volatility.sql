-- Stage 21: Advanced Volatility Analysis
-- Calculate rolling 5-period volatility

USE forex_market_analytics;

WITH price_changes AS (

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

percentage_changes AS (

    SELECT
        trade_date,
        pair,
        close_price,
        previous_close,

        (
            (close_price - previous_close)
            / previous_close
        ) * 100 AS percentage_change

    FROM price_changes
),

rolling_volatility AS (

    SELECT
        trade_date,
        pair,
        close_price,
        percentage_change,

        STDDEV(percentage_change) OVER (
            PARTITION BY pair
            ORDER BY trade_date
            ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
        ) AS volatility

    FROM percentage_changes
)

SELECT
    trade_date,
    pair,
    close_price,

    ROUND(
        percentage_change,
        5
    ) AS percentage_change,

    ROUND(
        volatility,
        5
    ) AS rolling_volatility

FROM rolling_volatility

ORDER BY pair, trade_date;
