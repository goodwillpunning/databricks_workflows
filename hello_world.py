# Databricks notebook source
dbutils.widgets.text("name", "Will", "Name")

# COMMAND ----------

name = dbutils.widgets.get("name")

# COMMAND ----------

print(f'Hello, {name}!')

# COMMAND ----------


