import snowflake.connector
import os
# Snowflake connection details
account = os.environ.get("SNOWFLAKE_ACCOUNT")
user = os.environ.get("SNOWFLAKE_USER")
password = os.environ.get("SNOWFLAKE_PASSWORD")
warehouse = os.environ.get("SNOWFLAKE_WAREHOUSE")
database = os.environ.get("SNOWFLAKE_DATABASE")
schema = os.environ.get("SNOWFLAKE_SCHEMA")

# Table details
# table_name = "demo_table"

# Snowflake connection
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database
)

# Create the table
query = f"""
GRANT privilege(s) ON TABLE DW_DEV.DATA_OPS.SNOWFLAKE_TABLE_DETAILS TO ROLE NON_PROD_DEVELOPER
"""
cursor = conn.cursor()
cursor.execute(query)

# Close the connection
cursor.close()
conn.close()
