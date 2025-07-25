# Databricks notebook source
# MAGIC %run ./_common
# MAGIC

# COMMAND ----------

lesson_config.create_schema = False

DA = DBAcademyHelper(course_config, lesson_config)
DA.reset_lesson()
DA.init()

# COMMAND ----------

DA.print_copyrights()
