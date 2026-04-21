# 📊 Crypto Analytics Project

---

## 📌 Overview

This project is an **end-to-end data analytics pipeline** that fetches real-time cryptocurrency data from the CoinGecko API, processes it, stores it in a SQLite database, and generates actionable insights using SQL and dashboards.

The goal is to demonstrate **real-world Data Analyst + Data Engineering skills** including:

* API data extraction
* Data cleaning & transformation
* SQL-based analysis
* Automation pipeline
* Reporting

---

## 🧰 Tools & Technologies Used

* Python
* Pandas
* SQLite
* SQL
* Excel
* Power BI
* REST API (CoinGecko)
* Git & GitHub

---

## ⚙️ Project Architecture

```
crypto-analytics-project/
│
├── data/
│   ├── raw_data.csv
│   ├── processed_data.csv
│   ├── crypto.db
│   └── crypto_report.xlsx
│
├── scripts/
│   ├── fetch_data.py
│   ├── process_data.py
│   └── automation.py
│
├── sql/
│   └── analysis.sql
│
├── dashboard/
│   └── crypto_dashboard.pbix
│
├── screenshots/
│   └── dashboard images
│
└── README.md
```

---

## 🔄 Data Pipeline Workflow

### 1️⃣ Data Extraction

Fetches live cryptocurrency data from API

### 2️⃣ Data Processing

* Cleans missing values
* Removes duplicates
* Selects important columns

### 3️⃣ Data Storage

Stores processed data in SQLite database

### 4️⃣ Automation

Full pipeline runs automatically using Python scripts

### 5️⃣ Reporting

* Generates Excel report
* Power BI dashboard for visualization

---

## 📥 Python Code

### 🔹 fetch_data.py

```python
import requests
import pandas as pd
import os

os.makedirs("../data", exist_ok=True)

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv("../data/raw_data.csv", index=False)
    print("✅ Data fetched successfully")
else:
    print("❌ API Error:", response.status_code)
```

---

### 🔹 process_data.py

```python
import pandas as pd
import sqlite3

# Load raw data
df = pd.read_csv("../data/raw_data.csv")

# Clean data
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# Select useful columns
df = df[[
    "name",
    "current_price",
    "market_cap",
    "price_change_percentage_24h"
]]

# Connect to SQLite DB
conn = sqlite3.connect("../data/crypto.db")

# Create table
df.to_sql("crypto_data", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("✅ Data processed and stored in crypto.db")
```

---

### 🔹 automation.py

```python
import os
import time

print("Starting pipeline...")

os.system("python scripts/fetch_data.py")
time.sleep(2)

os.system("python scripts/process_data.py")

print("Pipeline completed successfully!")
```

---

### 🔹 generate_report.py

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('../data/crypto.db')

query = "SELECT * FROM crypto_data"
df = pd.read_sql_query(query, conn)

df.to_excel('../data/crypto_report.xlsx', index=False)

print("Excel report generated successfully!")
```

---

## 📊 SQL Analysis

```sql
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
```

---

## 📈 Dashboard Features (Power BI)

* Market Cap Distribution
* Top 10 Cryptocurrencies
* Price Trends
* Volume Analysis
* BTC Dominance KPI

---

## 💡 Business Insights

* Top cryptocurrencies dominate majority of market cap
* High market cap coins show more stability
* Market trends indicate strong concentration in major assets

---

## 🚀 Key Highlights

✔ End-to-end pipeline
✔ Real-time API integration
✔ SQL analytics
✔ Automated workflow
✔ Dashboard visualization

---

## 📌 Future Improvements

* Add historical data tracking
* Use PostgreSQL instead of SQLite
* Deploy dashboard online
* Schedule pipeline using Airflow

---

## 👨‍💻 Author

**Reddy Hima Kumar**

---

## 📢 Conclusion

This project demonstrates:

* Data extraction from APIs
* Data transformation
* SQL-based insights
* Dashboard reporting

It simulates a **real-world Data Analyst workflow**.

---

