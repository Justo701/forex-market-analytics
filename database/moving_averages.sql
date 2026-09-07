USE forex_market_analytics;

WITH moving_averages AS (
    SELECT
        trade_date,
        pair,
        close_price,

        AVG(close_price) OVER (
            ORDER BY trade_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS ma_3,

        AVG(close_price) OVER (
            ORDER BY trade_date
            ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
        ) AS ma_5

    FROM forex_prices
),

with_previous AS (
    SELECT
        trade_date,
        pair,
        close_price,
        ma_3,
        ma_5,

        LAG(ma_3) OVER (
            ORDER BY trade_date
        ) AS previous_ma_3,

        LAG(ma_5) OVER (
            ORDER BY trade_date
        ) AS previous_ma_5

    FROM moving_averages
)

SELECT
    trade_date,
    pair,
    close_price,
    ROUND(ma_3, 5) AS ma_3,
    ROUND(ma_5, 5) AS ma_5,
    ROUND(previous_ma_3, 5) AS previous_ma_3,
    ROUND(previous_ma_5, 5) AS previous_ma_5,

    CASE
        WHEN previous_ma_3 <= previous_ma_5
             AND ma_3 > ma_5
            THEN 'Bullish Crossover'

        WHEN previous_ma_3 >= previous_ma_5
             AND ma_3 < ma_5
            THEN 'Bearish Crossover'

        ELSE 'No Crossover'
    END AS crossover_signal

FROM with_previous
ORDER BY trade_date;
