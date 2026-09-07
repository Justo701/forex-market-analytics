USE forex_market_analytics;

-- Stage 9: Movement Rankings

-- Rank daily percentage movements within each currency pair
WITH price_changes AS (
    SELECT
        trade_date,
        pair,
        close_price,
        LAG(close_price) OVER (
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
ranked_movements AS (
    SELECT
        trade_date,
        pair,
        close_price,
        percentage_change,
        ABS(percentage_change) AS movement_magnitude,

        ROW_NUMBER() OVER (
            PARTITION BY pair
            ORDER BY ABS(percentage_change) DESC
        ) AS movement_number

    FROM percentage_changes

    WHERE previous_close IS NOT NULL
)

SELECT
    trade_date,
    pair,
    close_price,
    ROUND(percentage_change, 5) AS percentage_change,
    ROUND(movement_magnitude, 5) AS movement_magnitude,

    CASE
        WHEN percentage_change > 0
            THEN 'Increased'
        WHEN percentage_change < 0
            THEN 'Decreased'
        ELSE 'Unchanged'
    END AS direction,

    movement_number

FROM ranked_movements

WHERE movement_number <= 3

ORDER BY pair, movement_number;
