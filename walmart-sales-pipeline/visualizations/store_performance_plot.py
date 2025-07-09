
import pandas as pd
import matplotlib.pyplot as plt
import snowflake.connector

conn = snowflake.connector.connect(
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT',
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='YOUR_SCHEMA'
)

query = "SELECT store_id, AVG(store_weekly_sales) as avg_sales FROM fact_sales GROUP BY store_id"
df = pd.read_sql(query, conn)

df.plot(kind='bar', x='store_id', y='avg_sales', legend=False)
plt.title("Average Weekly Sales per Store")
plt.xlabel("Store ID")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.show()

conn.close()
