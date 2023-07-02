# Databricks notebook source
# MAGIC %fs ls dbfs:/databricks-datasets/samples/lending_club/parquet/

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   addr_state, *
# MAGIC FROM
# MAGIC   parquet.`dbfs:/databricks-datasets/samples/lending_club/parquet/`

# COMMAND ----------


# -- ingest step
catalog = "development"
database = "team_databricks_sme"
spark.sql(
    f"""
CREATE TABLE IF NOT EXISTS {catalog}.{database}.lending_data
USING DELTA -- this is default just for explicit purpose
SELECT * FROM parquet.`dbfs:/databricks-datasets/samples/lending_club/parquet/`
"""
)

# COMMAND ----------

# Step 2
catalog = "development"
database = "team_databricks_sme"
spark.sql(
    f"""
OPTIMIZE {catalog}.{database}.lending_data;
"""
)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT distinct addr_state FROM development.team_databricks_sme.lending_data

# COMMAND ----------


# -- T&S 1 process AZ data
catalog = "development"
database = "team_databricks_sme"
spark.sql(
    f"""
CREATE OR REPLACE TABLE {catalog}.{database}.lending_data_az_geo
USING DELTA -- this is default just for explicit purpose
SELECT * FROM {catalog}.{database}.lending_data where addr_state = 'AZ'
"""
)

# COMMAND ----------

# -- T&S 2 process CA data
catalog = "development"
database = "team_databricks_sme"
spark.sql(
    f"""
CREATE OR REPLACE TABLE {catalog}.{database}.lending_data_ca_geo
USING DELTA -- this is default just for explicit purpose
SELECT * FROM {catalog}.{database}.lending_data where addr_state = 'CA'
"""
)

# COMMAND ----------

# -- T&S 3 process IL data
catalog = "development"
database = "team_databricks_sme"
spark.sql(
    f"""
CREATE OR REPLACE TABLE {catalog}.{database}.lending_data_il_geo
USING DELTA -- this is default just for explicit purpose
SELECT * FROM {catalog}.{database}.≈ where addr_state = 'IL'
"""
)

# COMMAND ----------

# -- Union Data Together
catalog = "development"
database = "team_databricks_sme"
spark.sql(
    f"""
CREATE OR REPLACE TABLE {catalog}.{database}.lending_data_az_ca_il_geo
USING DELTA -- this is default just for explicit purpose
SELECT * FROM {catalog}.{database}.lending_data_az_geo
UNION ALL
SELECT * FROM {catalog}.{database}.lending_data_ca_geo
UNION ALL
SELECT * FROM {catalog}.{database}.lending_data_il_geo
"""
)

# COMMAND ----------

# -- Union Data Together
catalog = "development"
database = "team_databricks_sme"
spark.sql(
    f"""
SELECT * FROM {catalog}.{database}.lending_data_az_ca_il_geo
"""
).limit(10).toPandas().to_csv("data.csv")
with open("data.csv", "r") as f:
    print(f.read())

# COMMAND ----------
