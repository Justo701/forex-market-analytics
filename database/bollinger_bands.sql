-- Stage 27: Bollinger Bands
-- Calculate 20-period Bollinger Bands

USE forex_market_analytics;

WITH price_analysis AS (

    SELECT
        trade_date,
        pair,
        close_price,

        COUNT(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
            ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
        ) AS period_count,

        AVG(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
            ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
        ) AS middle_band,

        STDDEV_SAMP(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
            ROWS BETWEEN 19 PRECEDING AND CURRENT ROW
        ) AS standard_deviation

    FROM forex_prices
)

SELECT
    trade_date,
    pair,
    close_price,

    ROUND(
        CASE
            WHEN period_count = 20
            THEN middle_band
            ELSE NULL
        END,
        5
    ) AS middle_band,

    ROUND(
        CASE
            WHEN period_count = 20
            THEN middle_band + (2 * standard_deviation)
            ELSE NULL
        END,
        5
    ) AS upper_band,

    ROUND(
        CASE
            WHEN period_count = 20
            THEN middle_band - (2 * standard_deviation)
            ELSE NULL
        END,
        5
    ) AS lower_band

FROM price_analysis

ORDER BY
    pair,
    trade_date;
