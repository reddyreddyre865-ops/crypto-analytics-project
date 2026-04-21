import requests
import pandas as pd
import os

# Create data folder if not exists
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