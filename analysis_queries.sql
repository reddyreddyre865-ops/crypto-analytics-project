-- Top 10 coins
SELECT name, market_cap
FROM crypto_data
ORDER BY market_cap DESC
LIMIT 10;

-- Top gainers
SELECT name, price_change_percentage_24h
FROM crypto_data
ORDER BY price_change_percentage_24h DESC
LIMIT 5;

-- Top losers
SELECT name, price_change_percentage_24h
FROM crypto_data
ORDER BY price_change_percentage_24h ASC
LIMIT 5;

-- Average change
SELECT AVG(price_change_percentage_24h) AS avg_change
FROM crypto_data;