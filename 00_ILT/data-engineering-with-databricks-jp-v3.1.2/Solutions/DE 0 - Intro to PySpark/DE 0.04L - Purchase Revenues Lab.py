# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-5b46ceba-8f87-4062-91cc-6f02f3303258
# MAGIC %md
# MAGIC # 購入売上ラボ (Purchase Revenues Lab)
# MAGIC
# MAGIC 購入売上を含むイベントのデータセットを準備します。
# MAGIC
# MAGIC ##### タスク (Tasks)
# MAGIC 1. イベントごとの購入売上を抽出する
# MAGIC 2. 売上が null でないイベントをフィルター処理する
# MAGIC 3. 収入のあるイベントの種類を確認する
# MAGIC 4. 不要な列を削除する
# MAGIC
# MAGIC ##### メソッド (Methods)
# MAGIC - DataFrame: **`select`**, **`drop`**, **`withColumn`**, **`filter`**, **`dropDuplicates`**
# MAGIC - カラム: **`isNotNull`**

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-00.04L

# COMMAND ----------

events_df = spark.table("events")
display(events_df)

# COMMAND ----------

# DBTITLE 0,--i18n-412840ac-10d6-473e-a3ea-8e9e92446b80
# MAGIC %md
# MAGIC ### 1. 各イベントの購入売上を抽出する （Extract purchase revenue for each event）
# MAGIC <strong>`ecommerce.purchase_revenue_in_usd`</strong>を抽出して<strong>`revenue`</strong>という新カラムを作成します

# COMMAND ----------

# ANSWER
from pyspark.sql.functions import col

revenue_df = events_df.withColumn('revenue', col('ecommerce.purchase_revenue_in_usd'))
display(revenue_df)

# COMMAND ----------

# DBTITLE 0,--i18n-66dfc9f4-0a59-482e-a743-cfdbc897aee8
# MAGIC %md
# MAGIC **1.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

from pyspark.sql.functions import col
expected1 = [4351.5, 4044.0, 3985.0, 3946.5, 3885.0, 3590.0, 3490.0, 3451.5, 3406.5, 3385.0]
result1 = [row.revenue for row in revenue_df.sort(col("revenue").desc_nulls_last()).limit(10).collect()]
print(result1)
assert(expected1 == result1)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-cb49af43-880a-4834-be9c-62f65581e67a
# MAGIC %md
# MAGIC ### 2. 売上がnullでないイベントをフィルター処理する (Filter events where revenue is not null)
# MAGIC <strong>`revenue`</strong>が<strong>`null`</strong>でないレコードのフィルタ

# COMMAND ----------

# ANSWER
purchases_df = revenue_df.filter(col())
display(purchases_df)

# COMMAND ----------

# DBTITLE 0,--i18n-3363869f-e2f4-4ec6-9200-9919dc38582b
# MAGIC %md
# MAGIC **2.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

assert purchases_df.filter(col("revenue").isNull()).count() == 0, "Nulls in 'revenue' column"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-6dd8d228-809d-4a3b-8aba-60da65c53f1c
# MAGIC %md
# MAGIC ### 3. 売上のあるイベントの種類を確認する (Check what types of events have revenue)
# MAGIC 次の2つの方法のいずれかで、<strong>`purchases_df`</strong>で一意の<strong>`event_name`</strong>値を見つけます。
# MAGIC - "event_name"を選択してユニークなレコードを取得します
# MAGIC - "event_name"のみに基づいて重複レコードを削除します
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint"> 売上に関連するイベントは１つだけです

# COMMAND ----------

# ANSWER

# Method 1
distinct_df1 = purchases_df.select("event_name").distinct()
display(distinct_df1)

# Method 2
distinct_df2 = purchases_df.dropDuplicates(["event_name"])
display(distinct_df2)

# COMMAND ----------

# DBTITLE 0,--i18n-f0d53260-4525-4942-b901-ce351f55d4c9
# MAGIC %md
# MAGIC ### 4. 不要なカラムを削除 (Drop unneeded column)
# MAGIC イベントタイプは1つしかないため、<strong>`purchases_df`</strong>から<strong>`event_name`</strong>を削除します。

# COMMAND ----------

# ANSWER
final_df = purchases_df.drop("event_name")
display(final_df)

# COMMAND ----------

# DBTITLE 0,--i18n-8ea4b4df-c55e-4015-95ee-1caccafa44d6
# MAGIC %md
# MAGIC **4.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

expected_columns = {"device", "ecommerce", "event_previous_timestamp", "event_timestamp",
                    "geo", "items", "revenue", "traffic_source",
                    "user_first_touch_timestamp", "user_id"}
assert(set(final_df.columns) == expected_columns)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-ed143b89-079a-44e9-87f3-9c8d242f09d2
# MAGIC %md
# MAGIC ### 5. ステップ3以外の全てのステップを連結します （Chain all the steps above excluding step 3)

# COMMAND ----------

# ANSWER
final_df = (events_df
            .withColumn("revenue", col("ecommerce.purchase_revenue_in_usd"))
            .filter(col("revenue").isNotNull())
            .drop("event_name")
           )

display(final_df)

# COMMAND ----------

# DBTITLE 0,--i18n-d7b35e13-8c38-4e17-b676-2146b64045fe
# MAGIC %md
# MAGIC **5.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

assert(final_df.count() == 9056)
print("All test pass")

# COMMAND ----------

expected_columns = {"device", "ecommerce", "event_previous_timestamp", "event_timestamp",
                    "geo", "items", "revenue", "traffic_source",
                    "user_first_touch_timestamp", "user_id"}
assert(set(final_df.columns) == expected_columns)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-03e7e278-385e-4afe-8268-229a1984a654
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
