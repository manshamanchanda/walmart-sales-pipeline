
import snowflake.connector

conn = snowflake.connector.connect(
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT',
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='YOUR_SCHEMA'
)

cur = conn.cursor()
cur.execute("SELECT CURRENT_DATE")
print(cur.fetchone())

cur.close()
conn.close()
