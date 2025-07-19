# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-536ff4eb-272a-489d-8bb9-59f9ef0de847
# MAGIC %md
# MAGIC # トラフィックソースの売上高に関するラボ（Revenue by Traffic Lab）
# MAGIC
# MAGIC ##交通量による売上高に関するラボ
# MAGIC 総売上高が上位3位のトラフィックソースを取得
# MAGIC 1. トラフィックソースによる売上高のデータ集約
# MAGIC 2. 総売上高でトップ3のトラフィックソースを取得
# MAGIC 3. 小数点以下2桁を持つように売上高の列を修正
# MAGIC
# MAGIC ##### メソッド（Methods）
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrameオブジェクト</a>: **`groupBy`**, **`sort`**, **`limit`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/column.html" target="_blank">列オブジェクト（Column）</a>: **`alias`**, **`desc`**, **`cast`**, **`operators`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html" target="_blank">組み込み関数（Built-in Functions）</a>: **`avg`**, **`sum`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-e6e01ed4-02eb-4b48-8b90-84d440c515a0
# MAGIC %md
# MAGIC ### Setup
# MAGIC
# MAGIC 以下のセルを実行して、最初のDataframe  **`df`**　を作成します。

# COMMAND ----------

from pyspark.sql.functions import col

# Purchase events logged on the BedBricks website
df = (spark.read.format("delta").load(DA.paths.events)
      .withColumn("revenue", col("ecommerce.purchase_revenue_in_usd"))
      .filter(col("revenue").isNotNull())
      .drop("event_name")
     )

display(df)

# COMMAND ----------

# DBTITLE 0,--i18n-917ddee5-b24d-4f28-9931-b251e5708c35
# MAGIC %md
# MAGIC ### 1. トラフィックソース別の売上高の集計
# MAGIC - **`traffic_source`** にてグループ化してください。
# MAGIC - **`revenue`** の合計を **`total_rev`** として取得してください。また10の桁で四捨五入してください（例： nnnnn.n）。
# MAGIC - **`avg_rev`** として **`revenue`** の平均を取得してください。
# MAGIC
# MAGIC 必要な組み込み関数（built-in functions）を忘れずにインポートしてください。

# COMMAND ----------

# ANSWER
from pyspark.sql.functions import avg, col, sum

traffic_df = (df
              .groupBy("traffic_source")
              .agg(sum(col("revenue")).alias("total_rev"),
                   avg(col("revenue")).alias("avg_rev"))
             )

display(traffic_df)

# COMMAND ----------

# DBTITLE 0,--i18n-3c5e0ac8-5f3f-4848-8403-dae36db0d3b5
# MAGIC %md
# MAGIC **1.1: 結果をチェック**

# COMMAND ----------

from pyspark.sql.functions import round

expected1 = [(12704560.0, 1083.175), (78800000.3, 983.2915), (24797837.0, 1076.6221), (47218429.0, 1086.8303), (16177893.0, 1083.4378), (8044326.0, 1087.218)]
test_df = traffic_df.sort("traffic_source").select(round("total_rev", 4).alias("total_rev"), round("avg_rev", 4).alias("avg_rev"))
result1 = [(row.total_rev, row.avg_rev) for row in test_df.collect()]

assert(expected1 == result1)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-718d5dd8-6d52-442d-88af-ecf838d5deb8
# MAGIC %md
# MAGIC ### 2. 総売上高でトップ3のトラフィックソースを取得
# MAGIC - **`total_rev`** の降順で並べ替えてください。
# MAGIC - 最初の3行に制限してください。

# COMMAND ----------

# ANSWER
top_traffic_df = traffic_df.sort(col("total_rev").desc()).limit(3)
display(top_traffic_df)

# COMMAND ----------

# DBTITLE 0,--i18n-a6f740e0-3808-4626-9c60-924cbcaafd5a
# MAGIC %md
# MAGIC **2.1: 結果をチェック**

# COMMAND ----------

expected2 = [(78800000.3, 983.2915), (47218429.0, 1086.8303), (24797837.0, 1076.6221)]
test_df = top_traffic_df.select(round("total_rev", 4).alias("total_rev"), round("avg_rev", 4).alias("avg_rev"))
result2 = [(row.total_rev, row.avg_rev) for row in test_df.collect()]

assert(expected2 == result2)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-72051bbe-4207-44b1-95ef-f5beee6d10e2
# MAGIC %md
# MAGIC ### 3. 総売上高の列を小数点以下2桁に制限
# MAGIC - 小数点以下2桁の数値を含むように **`avg_rev`** と **`total_rev`** 列を修正してください。
# MAGIC  - **`withColumn()`** を同じ名前で使用して、これらの列を置換してください。
# MAGIC  - 小数点以下2桁に制限するには、各列に100を掛け、longにキャストしてから、100で割ってください。

# COMMAND ----------

# ANSWER
final_df = (top_traffic_df
            .withColumn("avg_rev", (col("avg_rev") * 100).cast("long") / 100)
            .withColumn("total_rev", (col("total_rev") * 100).cast("long") / 100)
           )

display(final_df)

# COMMAND ----------

# DBTITLE 0,--i18n-e90f2db4-1f38-4c46-87de-2760f96b2de8
# MAGIC %md
# MAGIC **3.1: 結果をチェック**

# COMMAND ----------

expected3 = [(78800000.29, 983.29), (47218429.0, 1086.83), (24797837.0, 1076.62)]
result3 = [(row.total_rev, row.avg_rev) for row in final_df.collect()]

assert(expected3 == result3)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-060c0140-3c4c-4558-96de-f7c2379742d3
# MAGIC %md
# MAGIC ### 4. 補講: 組み込み数学関数を使って書き換え
# MAGIC 指定した小数点以下の桁数に四捨五入する組み込みの数学関数を探してください。

# COMMAND ----------

# ANSWER
from pyspark.sql.functions import round

bonus_df = (top_traffic_df
            .withColumn("avg_rev", round("avg_rev", 2))
            .withColumn("total_rev", round("total_rev", 2))
           )

display(bonus_df)

# COMMAND ----------

# DBTITLE 0,--i18n-9875e048-7810-4019-9891-712d6b7a5256
# MAGIC %md
# MAGIC **4.1: 結果をチェック**

# COMMAND ----------

expected4 = [(78800000.3, 983.29), (47218429.0, 1086.83), (24797837.0, 1076.62)]
result4 = [(row.total_rev, row.avg_rev) for row in bonus_df.collect()]

assert(expected4 == result4)
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-085d88db-a489-4142-9e04-47687adcf61d
# MAGIC %md
# MAGIC ### 5. まとめ

# COMMAND ----------

# ANSWER
# Solution #1 using round

chain_df = (df
            .groupBy("traffic_source")
            .agg(sum(col("revenue")).alias("total_rev"),
                 avg(col("revenue")).alias("avg_rev"))
            .sort(col("total_rev").desc())
            .limit(3)
            .withColumn("avg_rev", round("avg_rev", 2))
            .withColumn("total_rev", round("total_rev", 2))
           )

display(chain_df)

# COMMAND ----------

# ANSWER
# Solution #2 using *100, cast, /100
# chain_df = (df
#             .groupBy("traffic_source")
#             .agg(sum(col("revenue")).alias("total_rev"),
#                  avg(col("revenue")).alias("avg_rev"))
#             .sort(col("total_rev").desc())
#             .limit(3)
#             .withColumn("avg_rev", (col("avg_rev") * 100).cast("long") / 100)
#             .withColumn("total_rev", (col("total_rev") * 100).cast("long") / 100)
#            )

# display(chain_df)

# COMMAND ----------

# DBTITLE 0,--i18n-7ca119b7-9322-4f04-9c58-c7873a1ea474
# MAGIC %md
# MAGIC **5.1: 結果をチェック**

# COMMAND ----------

method_a = [(78800000.3,  983.29), (47218429.0, 1086.83), (24797837.0, 1076.62)]
method_b = [(78800000.29, 983.29), (47218429.0, 1086.83), (24797837.0, 1076.62)]
result5 = [(row.total_rev, row.avg_rev) for row in chain_df.collect()]

assert result5 == method_a or result5 == method_b
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-60b8db05-ebb2-4d50-bed2-c72259929b16
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
