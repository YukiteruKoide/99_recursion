# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-5505ea67-f96e-40fd-9c2a-bd4c644c928d
# MAGIC %md
# MAGIC # DataFrame & カラム
# MAGIC ##### Objectives
# MAGIC 1. カラムの作成
# MAGIC 1. カラムのサブセット化
# MAGIC 1. カラムの追加または置換
# MAGIC 1. 行のサブセット化
# MAGIC 1. 行の並び替え
# MAGIC
# MAGIC ##### メソッド
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrame</a>: **`select`**, **`selectExpr`**, **`drop`**, **`withColumn`**, **`withColumnRenamed`**, **`filter`**, **`distinct`**, **`limit`**, **`sort`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/column.html" target="_blank">カラム</a>: **`alias`**, **`isin`**, **`cast`**, **`isNotNull`**, **`desc`**, operators

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-b75891cc-f1e5-438b-be68-49f96665fee9
# MAGIC %md
# MAGIC BedBricksのイベントデータセットを使ってみましょう。

# COMMAND ----------

events_df = spark.read.format("delta").load(DA.paths.events)
display(events_df)

# COMMAND ----------

# DBTITLE 0,--i18n-5a4814ee-e5b1-42af-8dfd-beab9b1b3ce7
# MAGIC %md
# MAGIC ## カラムの作成
# MAGIC
# MAGIC <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/column.html" target="_blank">カラム</a> は式を使用してDataFrameのデータに基づいて計算される論理構造です。
# MAGIC
# MAGIC DataFrame内に存在する入力カラムに基づいて新しいカラムを作成します。

# COMMAND ----------

from pyspark.sql.functions import col

print(events_df.device)
print(events_df["device"])
print(col("device"))

# COMMAND ----------

display(events_df)

# COMMAND ----------

# DBTITLE 0,--i18n-d1d6ab85-093e-4f04-8610-2247222e563d
# MAGIC %md
# MAGIC Scala は、DataFrame 内の既存の列に基づいて新しい列を作成するための追加の構文をサポートしています

# COMMAND ----------

# MAGIC %scala
# MAGIC $"device"

# COMMAND ----------

# DBTITLE 0,--i18n-cc9be674-735b-44f0-9662-dc68b370af7a
# MAGIC %md
# MAGIC ### 列演算子とメソッド
# MAGIC | メソッド | 説明 |
# MAGIC | --- | --- |
# MAGIC | \*, + , <, >= | 数学および比較演算子 |
# MAGIC | ==, != | 等式と不等式のテスト (Scala 演算子は **`===`** と **`=!=`** です) |
# MAGIC | alias | 列に別名を付けます |
# MAGIC | cast, astype | 列を別のデータ型にキャストします |
# MAGIC | isNull, isNotNull, isNan | null である、null でない、NaN である |
# MAGIC | asc, desc | 列の昇順/降順に基づいてソート式を返します |

# COMMAND ----------

# DBTITLE 0,--i18n-3ecd52b1-c84e-4d14-9e1c-c03a48ca0f6f
# MAGIC %md
# MAGIC 既存の列、演算子、およびメソッドを使用して複雑な式を作成します。

# COMMAND ----------

col("ecommerce.purchase_revenue_in_usd") + col("ecommerce.total_item_quantity")
col("event_timestamp").desc()
(col("ecommerce.purchase_revenue_in_usd") * 100).cast("int")

# COMMAND ----------

# DBTITLE 0,--i18n-8ba468bb-ee75-4540-a35a-331e94594e30
# MAGIC %md
# MAGIC Here's an example of using these column expressions in the context of a DataFrame
# MAGIC
# MAGIC 以下の例で、DataFrameに対してコラムのメソッドを示します。

# COMMAND ----------

rev_df = (events_df
         .filter(col("ecommerce.purchase_revenue_in_usd").isNotNull())
         .withColumn("purchase_revenue", (col("ecommerce.purchase_revenue_in_usd") * 100).cast("int"))
         .withColumn("avg_purchase_revenue", col("ecommerce.purchase_revenue_in_usd") / col("ecommerce.total_item_quantity"))
         .sort(col("avg_purchase_revenue").desc())
        )

display(rev_df)

# COMMAND ----------

# DBTITLE 0,--i18n-0100a578-427a-4956-b2d6-d98e3a53cc6a
# MAGIC %md
# MAGIC ## DataFrame 変換メソッド
# MAGIC | メソッド | 説明 |
# MAGIC | --- | --- |
# MAGIC | **`select`** | 各要素に対して与えられた式を計算して新しい DataFrame を返します |
# MAGIC | **`drop`** | 列が削除された新しい DataFrame を返します |
# MAGIC | **`withColumnRenamed`** | 列の名前が変更された新しい DataFrame を返します |
# MAGIC | **`withColumn`** | 列を追加するか、同じ名前の既存の列を置き換えて、新しい DataFrame を返します |
# MAGIC | **`filter`**, **`where`** | 指定された条件を使用して行をフィルタリングする |
# MAGIC | **`sort`**, **`orderBy`** | 指定された式でソートされた新しい DataFrame を返します |
# MAGIC | **`dropDuplicates`**, **`distinct`** | 重複する行が削除された新しい DataFrame を返します |
# MAGIC | **`limit`** | 最初の n 行を取って新しい DataFrame を返します |
# MAGIC | **`groupBy`** | 指定された列を使用して DataFrame をグループ化し、集計を実行できるようにします |

# COMMAND ----------

# DBTITLE 0,--i18n-c89bbba2-4f55-4f22-addc-de25b23ee313
# MAGIC %md
# MAGIC ### カラムのサブセット化
# MAGIC DataFrame変換を使用して列をサブセット化します。

# COMMAND ----------

# DBTITLE 0,--i18n-d57643b9-245e-450f-82b0-b77013f7b684
# MAGIC %md
# MAGIC #### **`select()`**
# MAGIC 列または列ベースの式のセットを抽出します。

# COMMAND ----------

devices_df = events_df.select("user_id", "device")
display(devices_df)

# COMMAND ----------

from pyspark.sql.functions import col

locations_df = events_df.select(
    "user_id", 
    col("geo.city").alias("city"), 
    col("geo.state").alias("state")
)
display(locations_df)

# COMMAND ----------

# DBTITLE 0,--i18n-2ff20919-fa16-4c29-b07e-d43010c8821d
# MAGIC %md
# MAGIC #### **`selectExpr()`**
# MAGIC SQL式のセットを選択します。

# COMMAND ----------

apple_df = events_df.selectExpr("user_id", "device in ('macOS', 'iOS') as apple_user")
display(apple_df)

# COMMAND ----------

# DBTITLE 0,--i18n-eb07b09b-8dd2-4818-9f6f-7f7ad3a6b65e
# MAGIC %md
# MAGIC #### **`drop()`**
# MAGIC 指定した列を削除した後、新しいDataFrameを返します。
# MAGIC
# MAGIC 複数の列を指定するために文字列を使用します。

# COMMAND ----------

anonymous_df = events_df.drop("user_id", "geo", "device")
display(anonymous_df)

# COMMAND ----------

no_sales_df = events_df.drop(col("ecommerce"))
display(no_sales_df)

# COMMAND ----------

# DBTITLE 0,--i18n-a0632c28-d67f-4288-bf4e-1ade3df2b878
# MAGIC %md
# MAGIC ### カラムの追加または置換
# MAGIC DataFrame変換を使用して、列の追加や置換を行います。

# COMMAND ----------

# DBTITLE 0,--i18n-30f0fff0-fb26-4e29-bb71-6d6d21535c18
# MAGIC %md
# MAGIC #### **`withColumn()`**
# MAGIC カラムを追加したり、同じ名前を持つ既存のカラムを置き換えたりして、新しいDataFrameを返します。

# COMMAND ----------

mobile_df = events_df.withColumn("mobile", col("device").isin("iOS", "Android"))
display(mobile_df)

# COMMAND ----------

purchase_quantity_df = events_df.withColumn("purchase_quantity", col("ecommerce.total_item_quantity").cast("int"))
purchase_quantity_df.printSchema()

# COMMAND ----------

# DBTITLE 0,--i18n-506e9b1b-a1f9-4bc9-86f7-db3b7d48ce7a
# MAGIC %md
# MAGIC #### **`withColumnRenamed()`**
# MAGIC この関数は、列の名前を変更した新しいDataFrameを返します。

# COMMAND ----------

location_df = events_df.withColumnRenamed("geo", "location")
display(location_df)

# COMMAND ----------

# DBTITLE 0,--i18n-ec6222b9-3810-4f96-b17d-5952f218d59c
# MAGIC %md
# MAGIC ### 行のサブセット化
# MAGIC DataFrame変換を使用して行をサブセット化します。

# COMMAND ----------

# DBTITLE 0,--i18n-aa67adfe-8712-40e9-9c2b-840dfda38ef9
# MAGIC %md
# MAGIC #### **`filter()`**
# MAGIC 指定されたSQL式またはカラムベースの条件で行をフィルタリングします。
# MAGIC
# MAGIC ##### 別名: **`where`**

# COMMAND ----------

purchases_df = events_df.filter("ecommerce.total_item_quantity > 0")
display(purchases_df)

# COMMAND ----------

revenue_df = events_df.filter(col("ecommerce.purchase_revenue_in_usd").isNotNull())
display(revenue_df)

# COMMAND ----------

android_df = events_df.filter((col("traffic_source") != "direct") & (col("device") == "Android"))
display(android_df)

# COMMAND ----------

# DBTITLE 0,--i18n-1699cd7f-4bd1-431d-b277-6d6004848c56
# MAGIC %md
# MAGIC #### **`dropDuplicates()`**
# MAGIC 重複した行を削除した新しいDataFrameを返します。
# MAGIC
# MAGIC ##### 別名: **`distinct`**

# COMMAND ----------

display(events_df.distinct())

# COMMAND ----------

distinct_users_df = events_df.dropDuplicates(["user_id"])
display(distinct_users_df)

# COMMAND ----------

# DBTITLE 0,--i18n-e8daf914-afef-4159-9414-23bde2efd76a
# MAGIC %md
# MAGIC #### **`limit()`**
# MAGIC 最初のn行を取得して、新しいDataFrameを返します。

# COMMAND ----------

limit_df = events_df.limit(100)
display(limit_df)

# COMMAND ----------

# DBTITLE 0,--i18n-06c7f4a5-02b7-44f6-a29d-213ee2976d48
# MAGIC %md
# MAGIC ### 行の並び替え
# MAGIC DataFrame変換を使用して行をサブセット化します。

# COMMAND ----------

# DBTITLE 0,--i18n-50c39ed4-f70d-45b7-a452-22b819c0bb30
# MAGIC %md
# MAGIC #### **`sort()`**
# MAGIC 指定した列や式で並び替えた新しいDataFrameを返します。
# MAGIC
# MAGIC ##### 別名: **`orderBy`**

# COMMAND ----------

increase_timestamps_df = events_df.sort("event_timestamp")
display(increase_timestamps_df)

# COMMAND ----------

decrease_timestamp_df = events_df.sort(col("event_timestamp").desc())
display(decrease_timestamp_df)

# COMMAND ----------

increase_sessions_df = events_df.orderBy(["user_first_touch_timestamp", "event_timestamp"])
display(increase_sessions_df)

# COMMAND ----------

decrease_sessions_df = events_df.sort(col("user_first_touch_timestamp").desc(), col("event_timestamp"))
display(decrease_sessions_df)

# COMMAND ----------

# DBTITLE 0,--i18n-0062c495-c719-453d-a3eb-eb495d5bafd3
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
