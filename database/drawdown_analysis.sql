USE forex_market_analytics;

-- ============================================================
-- STAGE 11: DRAWDOWN & RISK ANALYSIS
-- ============================================================

-- STEP 1:
-- Find the highest price reached so far
-- for each currency pair.
WITH running_highs AS (
    SELECT
        trade_date,
        pair,
        close_price,

        -- Running maximum.
        -- PARTITION BY keeps each currency pair separate.
        MAX(close_price) OVER (
            PARTITION BY pair
            ORDER BY trade_date
        ) AS highest_so_far

    FROM forex_prices
),

-- STEP 2:
-- Mark the date whenever a new highest price is reached.
peak_markers AS (
    SELECT
        trade_date,
        pair,
        close_price,
        highest_so_far,

        CASE
            WHEN close_price = highest_so_far
            THEN trade_date
        END AS peak_date_marker

    FROM running_highs
),

-- STEP 3:
-- Carry the most recent peak date forward.
with_peak_dates AS (
    SELECT
        trade_date,
        pair,
        close_price,
        highest_so_far,

        MAX(peak_date_marker) OVER (
            PARTITION BY pair
            ORDER BY trade_date
        ) AS peak_date

    FROM peak_markers
),

-- STEP 4:
-- Calculate the drawdown measurements.
drawdown_analysis AS (
    SELECT
        trade_date,
        pair,
        close_price,
        highest_so_far,
        peak_date,

        -- Difference between peak price
        -- and current price.
        highest_so_far - close_price AS drawdown,

        -- Drawdown expressed as a percentage.
        (
            (highest_so_far - close_price)
            / highest_so_far
        ) * 100 AS drawdown_percentage,

        -- Number of days since the peak.
        DATEDIFF(
            trade_date,
            peak_date
        ) AS days_from_peak

    FROM with_peak_dates
)

-- STEP 5:
-- Display the complete risk analysis.
SELECT
    trade_date,
    pair,
    ROUND(close_price, 5) AS close_price,
    ROUND(highest_so_far, 5) AS highest_so_far,
    peak_date,

    ROUND(drawdown, 5) AS drawdown,

    ROUND(
        drawdown_percentage,
        5
    ) AS drawdown_percentage,

    days_from_peak,

    -- Classify the current market position.
    CASE
        WHEN drawdown_percentage = 0
            THEN 'At Peak'
        ELSE 'In Drawdown'
    END AS risk_status

FROM drawdown_analysis

ORDER BY pair, trade_date;
