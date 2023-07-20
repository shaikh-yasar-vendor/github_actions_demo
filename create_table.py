import snowflake.connector
import os
# Snowflake connection details
account = os.environ.get("account")
user = os.environ.get("user")
password = os.environ.get("password")
warehouse = os.environ.get("warehouse")
database = os.environ.get("database")
schema = os.environ.get("schema")

# Table details
# table_name = "demo_table"

# Snowflake connection
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)

# Create the table
query = f"""
GRANT USAGE ON SCHEMA DW_DEV.DATA_OPS TO ROLE NON_PROD_DEVELOPER
"""
cursor = conn.cursor()
cursor.execute(query)

# Close the connection
cursor.close()
conn.close()
