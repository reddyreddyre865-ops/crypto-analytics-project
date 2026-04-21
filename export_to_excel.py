import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('../data/crypto.db')

# Read data from table
query = "SELECT * FROM crypto"
df = pd.read_sql_query(query, conn)

# Save to Excel
df.to_excel('../data/crypto_report.xlsx', index=False)

print("Excel report generated successfully!")