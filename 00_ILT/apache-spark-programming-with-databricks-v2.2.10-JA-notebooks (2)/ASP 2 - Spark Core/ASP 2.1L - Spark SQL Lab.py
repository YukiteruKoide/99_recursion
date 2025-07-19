# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-20cef24c-ad62-4f88-b1d7-dc681c8367b6
# MAGIC %md
# MAGIC # Spark SQL ラボ (Lab)
# MAGIC
# MAGIC ##### タスク (Tasks)
# MAGIC 1. **`events`** テーブルから DataFrame を作成します
# MAGIC 1. DataFrame を表示し、そのスキーマを調べる
# MAGIC 1. **`macOS`** イベントのフィルタリングとソートに変換(transformations)を適用する
# MAGIC 1. 結果をカウントし、最初の 5行を取る
# MAGIC 1. SQLクエリを使用して同じ DataFrame を作成する
# MAGIC
# MAGIC ##### メソッド (Methods)
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/spark_session.html" target="_blank">SparkSession</a>: **`sql `** , **`table`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrame</a>変換 (transformations): **` select`** , **`where`** , **`orderBy`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.DataFrame.html" target="_blank">DataFrame</a> アクション(actions): **`show`** , **`count`** , **`take`**
# MAGIC - その他の<a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrame</a> メソッド (methods): **`printSchema`** , **`schema`** , **`createOrReplaceTempView`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-SQL

# COMMAND ----------

# DBTITLE 0,--i18n-ebdca5f9-ebbe-4201-a9ba-2b352857fab6
# MAGIC %md
# MAGIC ### 1.**`events`** テーブルから DataFrame を作成します
# MAGIC - SparkSessionを使用して **`events`** テーブルから DataFrame を作成します

# COMMAND ----------

# TODO
events_df = spark.table('events')

# COMMAND ----------

# DBTITLE 0,--i18n-8ea8bd96-3ff2-4ff0-9bf4-0253c250b3bb
# MAGIC %md
# MAGIC ### 2.DataFrame を表示してスキーマを調べる
# MAGIC - 上記のメソッドを使用して、DataFrame のコンテンツとスキーマを確認します

# COMMAND ----------

# TODO
events_df.printSchema()

# COMMAND ----------

display(events_df)

# COMMAND ----------

# DBTITLE 0,--i18n-cd1e0cf7-0e70-44d1-9306-5bd6820b057e
# MAGIC %md
# MAGIC ### 3.**`macOS`** イベントのフィルタリングとソートに変換(transformations)を適用する
# MAGIC - **`device`** が **`macOS`** である行のフィルター
# MAGIC - **`event_timestamp`** で行を並べ替える
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint"> フィルター SQL式で一重引用符と二重引用符を使用します

# COMMAND ----------

mac_df = (events_df
          .where("device = 'macOS'")
          .sort("event_timestamp")
         )

display(mac_df)

# COMMAND ----------

# DBTITLE 0,--i18n-880171c8-0275-41da-9cee-5377f4287698
# MAGIC %md
# MAGIC ### 4.結果をカウントし、最初の 5 行を取る
# MAGIC - DataFrame アクションを使用して、行を数えて取得します

# COMMAND ----------

# TODO
num_rows = mac_df.count()
rows = mac_df.take(5)

# COMMAND ----------

# DBTITLE 0,--i18n-91144c8b-b3f1-42fb-94d7-a4bb72396626
# MAGIC %md
# MAGIC **4.1:結果をチェック**

# COMMAND ----------

from pyspark.sql import Row

assert(num_rows == 1938215)
assert(len(rows) == 5)
assert(type(rows[0]) == Row)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-8073930e-9a33-4e96-bf6d-2c3e79b93c6b
# MAGIC %md
# MAGIC ### 5.SQL クエリを使用して同じ DataFrame を作成する
# MAGIC - SparkSession を使用して **`events`** テーブルで SQL クエリを実行します
# MAGIC - SQL コマンドを使用して、前に使用したものと同じフィルターおよびソートのクエリを記述します。

# COMMAND ----------

# TODO
mac_sql_df = spark.sql("""
SELECT * FROM events
WHERE device = 'macOS'
ORDER BY event_timestamp
LIMIT 5
""")

display(mac_sql_df)

# COMMAND ----------

# DBTITLE 0,--i18n-ddb8f309-ed6d-49ca-adca-2a059a9b22d2
# MAGIC %md
# MAGIC **5.1:結果をチェック**
# MAGIC - **`device`** 列には **`macOS`** の値のみが表示されるはずです。
# MAGIC - 5行目は、タイムスタンプが **`1592539226602157`** のイベントが表示されているはずです。

# COMMAND ----------

verify_rows = mac_sql_df.take(5)
assert (mac_sql_df.select("device").distinct().count() == 1 and len(verify_rows) == 5 and verify_rows[0]['device'] == "macOS"), "Incorrect filter condition"
assert (verify_rows[4]['event_timestamp'] == 1592539226602157), "Incorrect sorting"
del verify_rows
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-5a1d7fa1-d8cb-4bc5-863a-4c21fc5eb8ce
# MAGIC %md
# MAGIC ### クラスルームで使ったリソースの削除 (Clean up classroom)
# MAGIC このレッスンで作成された一時ファイル、テーブル、およびデータベースをクリーンアップします。

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
