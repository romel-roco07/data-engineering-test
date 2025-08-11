import sqlite3
import pandas as pd

conn = sqlite3.connect('S30 ETL Assignment.db')
df = pd.read_sql_query("SELECT * FROM your_table", conn)
print(df.head())
conn.close()