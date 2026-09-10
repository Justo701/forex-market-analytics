-- Stage 22: Risk Classification
-- Classify market risk using rolling volatility

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
        ) AS rolling_volatility

    FROM percentage_changes
),

volatility_average AS (

    SELECT
        trade_date,
        pair,
        close_price,
        percentage_change,
        rolling_volatility,

        AVG(rolling_volatility) OVER (
            PARTITION BY pair
        ) AS average_volatility

    FROM rolling_volatility
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
        rolling_volatility,
        5
    ) AS rolling_volatility,

    ROUND(
        average_volatility,
        5
    ) AS average_volatility,

    CASE

        WHEN rolling_volatility IS NULL
            THEN 'Unknown'

        WHEN rolling_volatility < average_volatility
            THEN 'Low Risk'

        WHEN rolling_volatility > average_volatility
            THEN 'High Risk'

        ELSE 'Moderate Risk'

    END AS risk_level

FROM volatility_average

ORDER BY pair, trade_date;
