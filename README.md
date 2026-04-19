📊 Crypto Analytics Project
📌 Overview

This project is an end-to-end data analytics pipeline that fetches real-time cryptocurrency data from the CoinGecko API, processes it, stores it in a SQLite database, and generates actionable insights using SQL and Power BI.

The goal of this project is to demonstrate data engineering + data analysis skills required for real-world data analyst roles.

🧰 Tools & Technologies Used
Python – Data extraction & automation
SQLite – Data storage
SQL – Data analysis
Power BI – Dashboard visualization
Excel – Data exploration & validation
⚙️ Project Architecture
crypto-analytics-project/
│
├── data/                  # Raw & processed data
├── scripts/               # Python scripts
│   ├── fetch_data.py      # Fetch data from API
│   ├── process_data.py    # Clean & transform data
│   ├── automation.py      # Pipeline automation
│
├── sql/
│   └── analysis.sql       # SQL queries for insights
│
├── dashboard/             # Power BI dashboard file
├── screenshots/           # Dashboard screenshots
└── README.md
🔄 Data Pipeline Workflow
Data Extraction
Fetches live cryptocurrency data from CoinGecko API
Data Processing
Cleans and formats data
Handles missing/null values
Data Storage
Stores structured data into SQLite database
Automation
Entire pipeline runs using Python scripts
Can be scheduled for periodic execution
📊 Key SQL Analysis
🔹 Top Cryptocurrencies by Market Cap
SELECT name, market_cap
FROM crypto
ORDER BY market_cap DESC
LIMIT 10;
🔹 Average Price of Cryptocurrencies
SELECT AVG(current_price) FROM crypto;
🔹 Bitcoin Market Dominance
SELECT 
(market_cap * 100.0 / (SELECT SUM(market_cap) FROM crypto)) AS btc_dominance
FROM crypto
WHERE name = 'Bitcoin';
📈 Dashboard Features (Power BI)
Market Cap Distribution
Top 10 Cryptocurrencies
Price Trends
Volume Analysis
BTC Dominance KPI
💡 Business Insights
Bitcoin dominance increased from 48% to 52%, indicating strong investor preference
Top 5 cryptocurrencies contribute ~75–80% of total market capitalization
High trading volume coins show stronger price stability
Market trends indicate concentration around major assets

## Screenshots

![alt text](<Screenshot 2026-04-19 152631.png>) ![alt text](<Screenshot 2026-04-19 152656.png>) ![alt text](<Screenshot 2026-04-19 152713.png>) ![alt text](<Screenshot 2026-04-19 152728.png>) ![alt text](<Screenshot 2026-04-19 152742.png>) ![alt text][def]

[def]: <Screenshot 2026-04-19 152753.png>

🚀 Key Highlights

✔ End-to-end data pipeline
✔ Real-time API integration
✔ SQL-based analysis
✔ Automated workflow
✔ Interactive dashboard

📌 Future Improvements
Add historical trend analysis
Deploy dashboard online
Use PostgreSQL instead of SQLite
Add Airflow for scheduling
👨‍💻 Author

Reddy Hima Kumar

📢 Conclusion

This project demonstrates practical skills in:

Data extraction
Data transformation
SQL analysis
Dashboard creation

It is designed to simulate a real-world data analyst workflow.
