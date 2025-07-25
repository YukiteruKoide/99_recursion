# Databricks notebook source
# MAGIC %run ./_common
# MAGIC

# COMMAND ----------

DA = DBAcademyHelper(**helper_arguments)
DA.init(install_datasets=True, create_db=False)

# COMMAND ----------

DA.print_copyrights(mappings={
    "COVID/": "coronavirusdataset/coronavirusdataset-readme.md",
})
