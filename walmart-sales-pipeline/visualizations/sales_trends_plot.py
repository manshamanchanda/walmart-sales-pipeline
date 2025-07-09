
import pandas as pd
import seaborn as sns
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

query = "SELECT store_date, store_weekly_sales FROM fact_sales"
df = pd.read_sql(query, conn)
df['store_date'] = pd.to_datetime(df['store_date'])

sns.lineplot(x='store_date', y='store_weekly_sales', data=df)
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

conn.close()
