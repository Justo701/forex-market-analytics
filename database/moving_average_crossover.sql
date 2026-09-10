-- Stage 12: Moving-Average Crossover Detection
-- Detect bullish and bearish crossovers

USE forex_market_analytics;

WITH moving_averages AS (

    SELECT
        trade_date,
        pair,
        close_price,

        ROUND(
            AVG(close_price) OVER (
                PARTITION BY pair
                ORDER BY trade_date
                ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
            ),
            5
        ) AS ma_3,

        ROUND(
            AVG(close_price) OVER (
                PARTITION BY pair
                ORDER BY trade_date
                ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
            ),
            5
        ) AS ma_5

    FROM forex_prices
),

trend_analysis AS (

    SELECT
        trade_date,
        pair,
        close_price,
        ma_3,
        ma_5,

        CASE
            WHEN ma_3 > ma_5
                THEN 'Bullish'

            WHEN ma_3 < ma_5
                THEN 'Bearish'

            ELSE 'Neutral'
        END AS trend_relationship

    FROM moving_averages
),

relationship_analysis AS (

    SELECT
        trade_date,
        pair,
        close_price,
        ma_3,
        ma_5,
        trend_relationship,

        LAG(trend_relationship) OVER (
            PARTITION BY pair
            ORDER BY trade_date
        ) AS previous_relationship

    FROM trend_analysis
)

SELECT
    trade_date,
    pair,
    close_price,
    ma_3,
    ma_5,
    trend_relationship,
    previous_relationship,

    CASE

    WHEN trend_relationship = 'Bullish'
         AND previous_relationship IN ('Neutral', 'Bearish')
        THEN 'Bullish Crossover'

    WHEN trend_relationship = 'Bearish'
         AND previous_relationship IN ('Neutral', 'Bullish')
        THEN 'Bearish Crossover'

    ELSE 'No Crossover'

END AS crossover_signal

FROM relationship_analysis

ORDER BY pair, trade_date;
