# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-b11bddc6-97f8-42c1-85a5-a16f1662e3ba
# MAGIC %md
# MAGIC # 購買収益ラボ (Purchase Revenues Lab)
# MAGIC
# MAGIC 購入収益を含むイベントのデータセットを準備します。
# MAGIC
# MAGIC ##### Tasks
# MAGIC 1. イベントごとの購入収益を抽出する
# MAGIC 2.収益が null でないイベントをフィルター処理する
# MAGIC 3. 収入のあるイベントの種類を確認する
# MAGIC 4. 不要な列を削除する
# MAGIC
# MAGIC ##### メソッド
# MAGIC - DataFrame: **`select`**, **`drop`**, **`withColumn`**, **`filter`**, **`dropDuplicates`**
# MAGIC - カラム: **`isNotNull`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

events_df = spark.read.format("delta").load(DA.paths.events)
display(events_df)

# COMMAND ----------

# DBTITLE 0,--i18n-60bd4181-97a2-4a06-a803-21b6f6f53743
# MAGIC %md
# MAGIC ### 1. 各イベントの購入収益を抽出する（Extract purchase revenue for each event）
# MAGIC **`ecommerce.purchase_revenue_in_usd`**　から抽出情報で　**`revenue`**　という新カラムを作成

# COMMAND ----------

# ANSWER
from pyspark.sql.functions import col

revenue_df = events_df.withColumn("revenue", col("ecommerce.purchase_revenue_in_usd"))
display(revenue_df)

# COMMAND ----------

# DBTITLE 0,--i18n-0772d97a-4f9c-4214-9395-a79881a4af01
# MAGIC %md
# MAGIC **1.1: 結果確認**

# COMMAND ----------

from pyspark.sql.functions import col
expected1 = [5830.0, 5485.0, 5289.0, 5219.1, 5180.0, 5175.0, 5125.0, 5030.0, 4985.0, 4985.0]
result1 = [row.revenue for row in revenue_df.sort(col("revenue").desc_nulls_last()).limit(10).collect()]

assert(expected1 == result1)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-304eff86-a096-4ed1-a492-2420b1db8e77
# MAGIC %md
# MAGIC ### 2. 収益が null でないイベントをフィルター処理する（Filter events where revenue is not null）
# MAGIC **`revenue`** が **`null`** でないレコードのフィルタ

# COMMAND ----------

# ANSWER
purchases_df = revenue_df.filter(col("revenue").isNotNull())
display(purchases_df)

# COMMAND ----------

# DBTITLE 0,--i18n-31a6d284-50e0-4022-b795-c9b941c44123
# MAGIC %md
# MAGIC **2.1: 結果確認**

# COMMAND ----------

assert purchases_df.filter(col("revenue").isNull()).count() == 0, "Nulls in 'revenue' column"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-493074be-c415-400d-8527-85acc1dff0da
# MAGIC %md
# MAGIC ### 3. 収益のあるイベントの種類を確認する（Check what types of events have revenue）
# MAGIC 次の 2 つの方法のいずれかで、 **`purchases_df`** で一意の **`event_name`** 値を見つけます。
# MAGIC - "event_name" を選択して個別のレコードを取得する
# MAGIC - "event_name" のみに基づいて重複レコードを削除する
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint"> 収益に関連するイベントは 1 つだけです

# COMMAND ----------

# ANSWER

# Method 1
distinct_df1 = purchases_df.select("event_name").distinct()
display(distinct_df1)

# Method 2
distinct_df2 = purchases_df.dropDuplicates(["event_name"])
display(distinct_df2)

# COMMAND ----------

# DBTITLE 0,--i18n-a2cdcb0b-22b6-4f87-8352-5d427c6d5bd2
# MAGIC %md
# MAGIC ### 4. 不要な列を削除（Drop unneeded column）
# MAGIC イベント タイプは 1 つしかないため、 **`purchases_df`** から **`event_name`** を削除します。

# COMMAND ----------

# ANSWER
final_df = purchases_df.drop("event_name")
display(final_df)

# COMMAND ----------

# DBTITLE 0,--i18n-94f780e0-76f0-4668-ab10-125a4d3bd8cc
# MAGIC %md
# MAGIC **4.1: 結果確認**

# COMMAND ----------

expected_columns = {"device", "ecommerce", "event_previous_timestamp", "event_timestamp",
                    "geo", "items", "revenue", "traffic_source",
                    "user_first_touch_timestamp", "user_id"}
assert(set(final_df.columns) == expected_columns)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-86c5d7d7-c387-4452-ac0a-fb96386ab78e
# MAGIC %md
# MAGIC ### 5. ステップ 3 を除く上記のすべてのステップを連鎖します（Chain all the steps above excluding step 3）

# COMMAND ----------

# ANSWER
final_df = (events_df
            .withColumn("revenue", col("ecommerce.purchase_revenue_in_usd"))
            .filter(col("revenue").isNotNull())
            .drop("event_name")
           )

display(final_df)

# COMMAND ----------

# DBTITLE 0,--i18n-99029e50-6d9d-4943-99ad-0edd4e8f9c97
# MAGIC %md
# MAGIC **5.1: 結果確認**

# COMMAND ----------

assert(final_df.count() == 180678)
print("All test pass")

# COMMAND ----------

expected_columns = {"device", "ecommerce", "event_previous_timestamp", "event_timestamp",
                    "geo", "items", "revenue", "traffic_source",
                    "user_first_touch_timestamp", "user_id"}
assert(set(final_df.columns) == expected_columns)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-6bc7dc19-46ee-48d2-9422-d3a2530542fc
# MAGIC %md
# MAGIC ### クラスルームで使ったリソースの削除 (Clean up classroom)

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
