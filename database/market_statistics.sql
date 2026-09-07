USE forex_market_analytics;

-- Stage 8: Market Statistics

-- Average, highest, lowest price and number of records per pair
SELECT
    pair,
    ROUND(AVG(close_price), 5) AS average_price,
    ROUND(MAX(close_price), 5) AS highest_price,
    ROUND(MIN(close_price), 5) AS lowest_price,
    COUNT(*) AS total_records
FROM forex_prices
GROUP BY pair;


-- Number of up days and down days per pair
WITH price_changes AS (
    SELECT
        trade_date,
        pair,
        close_price,

        LAG(close_price) OVER (
            ORDER BY trade_date
        ) AS previous_close

    FROM forex_prices
)

SELECT
    pair,

    COUNT(
        CASE
            WHEN close_price > previous_close
            THEN 1
        END
    ) AS up_days,

    COUNT(
        CASE
            WHEN close_price < previous_close
            THEN 1
        END
    ) AS down_days

FROM price_changes
GROUP BY pair;
-- Average daily percentage change
WITH price_changes AS (
    SELECT
        trade_date,
        pair,
        close_price,

        LAG(close_price) OVER (
            ORDER BY trade_date
        ) AS previous_close

    FROM forex_prices
)

SELECT
    pair,

    ROUND(
        AVG(
            (
                (close_price - previous_close)
                / previous_close
            ) * 100
        ),
        5
    ) AS average_daily_percentage_change

FROM price_changes

GROUP BY pair;


-- Average daily movement magnitude
WITH price_changes AS (
    SELECT
        trade_date,
        pair,
        close_price,

        LAG(close_price) OVER (
            ORDER BY trade_date
        ) AS previous_close

    FROM forex_prices
)

SELECT
    pair,

    ROUND(
        AVG(
            ABS(
                (
                    (close_price - previous_close)
                    / previous_close
                ) * 100
            )
        ),
        5
    ) AS average_daily_movement

FROM price_changes

GROUP BY pair;

