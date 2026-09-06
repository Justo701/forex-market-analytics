-- Forex Market Analytics
-- Database schema

CREATE DATABASE IF NOT EXISTS forex_market_analytics;

USE forex_market_analytics;

CREATE TABLE IF NOT EXISTS forex_prices (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    pair VARCHAR(10) NOT NULL,
    trade_date DATETIME NOT NULL,
    open_price DECIMAL(12,5) NOT NULL,
    high_price DECIMAL(12,5) NOT NULL,
    low_price DECIMAL(12,5) NOT NULL,
    close_price DECIMAL(12,5) NOT NULL,
    volume BIGINT UNSIGNED
);
