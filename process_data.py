import pandas as pd
import sqlite3

df = pd.read_csv("../data/raw_data.csv")

# Clean
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# Select columns
df = df[[
    "name",
    "current_price",
    "market_cap",
    "price_change_percentage_24h"
]]

# Save processed file
df.to_csv("../data/processed_data.csv", index=False)

# Save to database
conn = sqlite3.connect("../data/crypto.db")
df.to_sql("crypto_data", conn, if_exists="replace", index=False)
conn.close()

print("✅ Data processed and stored")