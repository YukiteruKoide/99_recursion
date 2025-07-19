# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-f71eff64-cf6e-469a-ab37-a297936c4980
# MAGIC %md
# MAGIC # アクティブユーザー ラボ（Active Users Lab）
# MAGIC 毎日のアクティブユーザーと平均アクティブユーザーを曜日別にプロットしてください。
# MAGIC 1. イベントのタイムスタンプと日付を抽出
# MAGIC 2. 毎日のアクティブユーザーを取得
# MAGIC 3. 曜日別の平均アクティブユーザー数の取得
# MAGIC 4.  曜日を正しい順に並べ替え

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-3a6a78da-1772-441e-b73a-eff2e82561bb
# MAGIC %md
# MAGIC ### Setup
# MAGIC 以下のセルを実行して、BedBricksのWebサイトに記録されたユーザーIDとイベントのタイムスタンプ（timestamps）の最初のDataframeを作成します。

# COMMAND ----------

from pyspark.sql.functions import col

df = (spark
      .read
      .format("delta")
      .load(DA.paths.events)
      .select("user_id", col("event_timestamp").alias("ts"))
     )

display(df)

# COMMAND ----------

# DBTITLE 0,--i18n-7fa26321-781b-4633-bce4-5b86082adbcc
# MAGIC %md
# MAGIC ### 1. イベントのタイムスタンプ（timestamp）と日付（date）を抽出
# MAGIC - **`ts`** を100万で割ってマイクロ秒から秒に変換し、タイムスタンプにキャストしてください。
# MAGIC - **`ts`** を日付に変換して **`date`** カラムを追加してください。

# COMMAND ----------

# TODO
from pyspark.sql.functions import to_date

datetime_df = (df
               .withColumn("ts", (col("ts") / 1e6).cast("timestamp"))
               .withColumn("date", to_date(col("ts")))
)
display(datetime_df)

# COMMAND ----------

# DBTITLE 0,--i18n-50e248b0-9067-4ec0-b633-1862739315f1
# MAGIC %md
# MAGIC **1.1: 結果のチェック**

# COMMAND ----------

from pyspark.sql.types import DateType, StringType, StructField, StructType, TimestampType

expected1a = StructType([StructField("user_id", StringType(), True),
                         StructField("ts", TimestampType(), True),
                         StructField("date", DateType(), True)])

result1a = datetime_df.schema

assert expected1a == result1a, "datetime_df does not have the expected schema"
print("All test pass")

# COMMAND ----------

import datetime

expected1b = datetime.date(2020, 6, 19)
result1b = datetime_df.sort("date").first().date

assert expected1b == result1b, "datetime_df does not have the expected date values"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-cffda679-267e-4934-9316-f33d68f1fff6
# MAGIC %md
# MAGIC ### 2. 毎日のアクティブユーザーを取得
# MAGIC - 日付別にグループ化してください。
# MAGIC - **`user_id`** における重複を排除した近似カウント数を、"active_users"という別名で集計してください。
# MAGIC  - 重複を排除した近似カウント数（**approximate count distinct**）を得るための組み込み関数を呼び出してください。
# MAGIC - 日付順に並び替えてください。
# MAGIC - 折れ線グラフとしてプロットしてください。

# COMMAND ----------

# TODO
from pyspark.sql.functions import approx_count_distinct
active_users_df = (datetime_df
                   .groupBy("date")
                   .agg(approx_count_distinct("user_id").alias("active_users"))
                   .sort("date")
)
display(active_users_df)

# COMMAND ----------

# DBTITLE 0,--i18n-168eed92-68bf-4966-98b6-f92bc44fbe67
# MAGIC %md
# MAGIC **2.1: 結果のチェック**

# COMMAND ----------

from pyspark.sql.types import LongType

expected2a = StructType([StructField("date", DateType(), True),
                         StructField("active_users", LongType(), False)])

result2a = active_users_df.schema

assert expected2a == result2a, "active_users_df does not have the expected schema"
print("All test pass")

# COMMAND ----------

expected2b = [(datetime.date(2020, 6, 19), 251573), (datetime.date(2020, 6, 20), 357215), (datetime.date(2020, 6, 21), 305055), (datetime.date(2020, 6, 22), 239094), (datetime.date(2020, 6, 23), 243117)]

result2b = [(row.date, row.active_users) for row in active_users_df.orderBy("date").take(5)]

assert expected2b == result2b, "active_users_df does not have the expected values"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-ac71e88e-aa3d-4032-8741-876f0d8ff8da
# MAGIC %md
# MAGIC ### 3. 曜日別の平均アクティブユーザー数の取得
# MAGIC - 日付時間（datetime）パターン文字列を用いて **`date`** から曜日を抽出して **`day`** カラムを追加してください（例えば、 **`Mon`** 、 **`1`**　ではありません）。
# MAGIC - **`day`** でグループ化してください。
# MAGIC - "active_users" の平均値を、 **`avg_users`** という別名（alias）で集計してください。

# COMMAND ----------

# TODO
from pyspark.sql.functions import date_format, avg

active_dow_df = (active_users_df
                 .withColumn("day", date_format(col("date"), "E"))
                 .groupBy("day")
                 .agg(avg(col("active_users")).alias("avg_users"))
                )
display(active_dow_df)

# COMMAND ----------

# DBTITLE 0,--i18n-889c1b5c-f870-45d0-8cc0-5e1c58f6640e
# MAGIC %md
# MAGIC **3.1: 結果のチェック**

# COMMAND ----------

from pyspark.sql.types import DoubleType

expected3a = StructType([StructField("day", StringType(), True),
                         StructField("avg_users", DoubleType(), True)])

result3a = active_dow_df.schema

assert expected3a == result3a, "active_dow_df does not have the expected schema"
print("All test pass")

# COMMAND ----------

expected3b = [("Fri", 247180.66666666666), ("Mon", 238195.5), ("Sat", 278482.0), ("Sun", 282905.5), ("Thu", 264620.0), ("Tue", 260942.5), ("Wed", 227214.0)]

result3b = [(row.day, row.avg_users) for row in active_dow_df.sort("day").collect()]

assert expected3b == result3b, "active_dow_df does not have the expected values"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-f4b41974-87d7-47fe-81f8-93fd5c99fbe1
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
