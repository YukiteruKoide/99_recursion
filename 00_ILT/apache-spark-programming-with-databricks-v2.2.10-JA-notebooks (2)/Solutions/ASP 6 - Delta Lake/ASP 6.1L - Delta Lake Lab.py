# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-b7ab8d00-d772-4194-be2b-21869a88d017
# MAGIC %md
# MAGIC # Delta Lakeラボ
# MAGIC ##### タスク (Tasks)
# MAGIC 1. Deltaに販売データを書き込む
# MAGIC 1. 商品配列ではなく商品数を表示するように販売データを修正
# MAGIC 1. データを同じDeltaパスに書き換え
# MAGIC 1. テーブルを作成してバージョン履歴を表示
# MAGIC 1. 前のバージョンを読むためにタイムトラベル

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

sales_df = spark.read.parquet(f"{DA.paths.datasets}/ecommerce/sales/sales.parquet")
delta_sales_path = f"{DA.paths.working_dir}/delta-sales"

# COMMAND ----------

# DBTITLE 0,--i18n-3ddef38d-a094-4485-891b-04aba30c1fc3
# MAGIC %md
# MAGIC ### 1. Deltaに販売データを書き込む (Write sales data to Delta)
# MAGIC <strong>`delta_sales_path`</strong>に<strong>`sales_df`</strong>を出力してください。

# COMMAND ----------

# ANSWER
sales_df.write.format("delta").mode("overwrite").save(delta_sales_path)

# COMMAND ----------

# DBTITLE 0,--i18n-b23c5a11-5446-48b8-9e9e-d3aa051473fe
# MAGIC %md
# MAGIC **1.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

assert len(dbutils.fs.ls(delta_sales_path)) > 0

# COMMAND ----------

# DBTITLE 0,--i18n-a7ff98a7-66d3-49a8-a3d3-6d1f12e329d6
# MAGIC %md
# MAGIC ### 2. 商品配列ではなく商品数を表示するように販売データを修正 (Modify sales data to show item count instead of item array)
# MAGIC <strong>`items`</strong>列の値を、itemsの配列サイズの整数値で置き換えてください。
# MAGIC 出来たDataframeを<strong>`updated_sales_df`</strong>に割り当ててください。

# COMMAND ----------

# ANSWER
from pyspark.sql.functions import size, col

updated_sales_df = sales_df.withColumn("items", size(col("items")))
display(updated_sales_df)

# COMMAND ----------

# DBTITLE 0,--i18n-a6058b29-1241-4067-9c31-e716d04c9840
# MAGIC %md
# MAGIC **2.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

from pyspark.sql.types import IntegerType

assert updated_sales_df.schema[6].dataType == IntegerType()
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-1449e3a9-db22-49e7-8b0b-b1b0c2a50a25
# MAGIC %md
# MAGIC ### 3. データを同じDeltaパスに書き換え (Rewrite sales data to same Delta path)
# MAGIC <strong>`updated_sales_df`</strong>を同じDeltaの場所<strong>`delta_sales_path`</strong>に出力してください。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint"> スキーマを上書き(overwrite)するオプションが無いと失敗します。

# COMMAND ----------

# ANSWER
updated_sales_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(delta_sales_path)

# COMMAND ----------

# DBTITLE 0,--i18n-56b5c3af-c575-4a44-becb-63b0a5321872
# MAGIC %md
# MAGIC **3.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

assert spark.read.format("delta").load(delta_sales_path).schema[6].dataType == IntegerType()
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-646700b2-7030-4adc-858e-3866c4917923
# MAGIC %md
# MAGIC ### 4. テーブルを作成してバージョン履歴を表示 (Create table and view version history)
# MAGIC 以下のステップを実現するため、`spark.sql()`の中にSQLを書くことでSQLクエリーを実行してください。
# MAGIC - <strong>`sales_delta`</strong>テーブルが存在する場合、削除してください
# MAGIC - <strong>`delta_sales_path`</strong>の場所を使って<strong>`sales_delta`</strong>テーブルを作成してください
# MAGIC - <strong>`sales_delta`</strong>テーブルのバージョン履歴を表示します
# MAGIC
# MAGIC `spark.sql()`の中のSQLクエリーの例として```spark.sql("SELECT * FROM sales_data")```を参考にしてください

# COMMAND ----------

# ANSWER
spark.sql("DROP TABLE IF EXISTS sales_delta")
spark.sql("CREATE TABLE sales_delta USING DELTA LOCATION '{}'".format(delta_sales_path))

# COMMAND ----------

# ANSWER
display(spark.sql("DESCRIBE HISTORY sales_delta"))

# COMMAND ----------

# DBTITLE 0,--i18n-ba038ee5-a6ff-4744-9876-3c2b088f3ca4
# MAGIC %md
# MAGIC **4.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

sales_delta_df = spark.sql("SELECT * FROM sales_delta")
assert sales_delta_df.count() == 210370
assert sales_delta_df.schema[6].dataType == IntegerType()
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-0d7572b5-2bd5-4f4b-a42a-4810bd7fca92
# MAGIC %md
# MAGIC ### 5. 前のバージョンを読むためにタイムトラベル (Time travel to read previous version)
# MAGIC <strong>`delta_sales_path`</strong>のDeltaテーブルをバージョン0で読み込んでください。
# MAGIC 出来たDataframeを<strong>`old_sales_df`</strong>に割り当ててください。

# COMMAND ----------

# ANSWER
old_sales_df = spark.read.format("delta").option("versionAsOf", 0).load(delta_sales_path)
display(old_sales_df)

# COMMAND ----------

# DBTITLE 0,--i18n-c36128f3-0818-4dc4-a628-a35f97d253ba
# MAGIC %md
# MAGIC **5.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

assert old_sales_df.select(size(col("items"))).first()[0] == 1
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-3e03f968-f1f4-40d2-903f-fab13b238a52
# MAGIC %md
# MAGIC ### クラスルームで使ったリソースの削除 (Classroom Cleanup)

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
