
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

query = "SELECT store_id, store_weekly_sales FROM fact_sales"
df = pd.read_sql(query, conn)

df.groupby("store_id").sum().plot(kind="bar")
plt.title("Weekly Sales by Store")
plt.xlabel("Store ID")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

conn.close()
