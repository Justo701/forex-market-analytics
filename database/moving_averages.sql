USE forex_market_analytics;

WITH price_analysis AS (

    SELECT
        trade_date,
        pair,
        close_price,

        LAG(close_price) OVER (
            ORDER BY trade_date
        ) AS previous_close

    FROM forex_prices
),

movement_analysis AS (

    SELECT
        trade_date,
        pair,
        close_price,
        previous_close,

        close_price - previous_close AS price_change,

        (
            (close_price - previous_close)
            / previous_close
        ) * 100 AS percentage_change,

        ABS(
            (
                (close_price - previous_close)
                / previous_close
            ) * 100
        ) AS absolute_percentage_change

    FROM price_analysis
)

SELECT
    trade_date,
    pair,
    close_price,

    ROUND(previous_close, 5) AS previous_close,

    ROUND(price_change, 5) AS price_change,

    ROUND(percentage_change, 5) AS percentage_change,

    ROUND(absolute_percentage_change, 5)
        AS absolute_percentage_change,

    CASE
        WHEN absolute_percentage_change < 0.10
            THEN 'Low Movement'

        WHEN absolute_percentage_change <= 0.30
            THEN 'Moderate Movement'

        ELSE 'High Movement'
    END AS movement_class

FROM movement_analysis

ORDER BY trade_date;
