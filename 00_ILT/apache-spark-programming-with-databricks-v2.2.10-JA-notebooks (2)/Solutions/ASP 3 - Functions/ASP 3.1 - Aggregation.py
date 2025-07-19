# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-33ed5661-945e-4602-9062-1d41550d349e
# MAGIC %md
# MAGIC # Aggregation
# MAGIC
# MAGIC ##### 目的（Objectives）
# MAGIC 1. 特定のカラムに対してのデータのグループ化
# MAGIC 1. グループ化データメソッド（Grouped data methods）
# MAGIC 1. 組み込み集計関数(Build-in functions)
# MAGIC
# MAGIC
# MAGIC ##### メソッド（Methods）
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrame</a>: **`groupBy`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/grouping.html" target="_blank" target="_blank">グループ化したデータへ計算</a>: **`agg`**, **`avg`**, **`count`**, **`max`**, **`sum`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html" target="_blank">組み込み関数（Functions）</a>: **`approx_count_distinct`** , **`avg`** , **`sum`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-53c415db-4b5b-4572-a19b-98af284f250a
# MAGIC %md
# MAGIC BedBricksのイベントデータセットを使ってみましょう。

# COMMAND ----------

df = spark.read.format("delta").load(DA.paths.events)
display(df)

# COMMAND ----------

# DBTITLE 0,--i18n-d33fd16f-8f2c-45e0-94a1-2f5638a1f44c
# MAGIC %md
# MAGIC ### 1.データのグループ化（Grouping data）
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/aspwd/aggregation_groupby.png" width="60%" />

# COMMAND ----------

# DBTITLE 0,--i18n-33c82540-0afb-41d5-8366-b072102ae475
# MAGIC %md
# MAGIC ### 2.groupBy
# MAGIC グループ化データオブジェクトを作成するためには、DataFrameの　**`groupBy`**　メソッドを使用します。
# MAGIC
# MAGIC このグループ化データオブジェクトは、Scalaでは　**`RelationalGroupedDataset`** 、　Pythonでは　**`GroupedData`** と呼ばれています。

# COMMAND ----------

df.groupBy("event_name")

# COMMAND ----------

df.groupBy("geo.state", "geo.city")

# COMMAND ----------

# DBTITLE 0,--i18n-de9bc0c1-8991-448d-be80-f3dd455bee06
# MAGIC %md
# MAGIC ### 3.グループ化データメソッド（Grouped data methods）
# MAGIC
# MAGIC  <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/grouping.html" target="_blank">グループ化データオブジェクト</a> においては、様々な集計関数（Aggregation methods）が利用可能です。 
# MAGIC
# MAGIC
# MAGIC | メソッド | 説明 |
# MAGIC | --- | --- |
# MAGIC | agg | 集計対象列について、集約処理を計算 |
# MAGIC | avg | 各グループの各数値列に対して平均値を計算 |
# MAGIC | count | 各グループの行数をカウント |
# MAGIC | max | 各グループの各数値列に対して最大値を計算　|
# MAGIC | mean | 各グループの各数値列に対して平均値を計算 |
# MAGIC | min | 各グループの各数値列の最小値を計算　|
# MAGIC | pivot | 現在のDataFrameの列をピボッドし、指定された集約関数（Aggregation method）を適用 |
# MAGIC | sum | 各グループの各数値列の合計を計算|

# COMMAND ----------

event_counts_df = df.groupBy("event_name").count()
display(event_counts_df)

# COMMAND ----------

# DBTITLE 0,--i18n-1bc3f8ca-7dec-4b6a-9647-00791b82b2ac
# MAGIC %md
# MAGIC それぞれの平均購入売上高（Purchase revenue）の計算します。

# COMMAND ----------

avg_state_purchases_df = df.groupBy("geo.state").avg("ecommerce.purchase_revenue_in_usd")
display(avg_state_purchases_df)

# COMMAND ----------

# DBTITLE 0,--i18n-a3c86855-8cf6-4832-bad1-67c2e19ae93a
# MAGIC %md
# MAGIC そして、各州と都市の組み合わせに対して、それぞれの平均購入売上高の数量(Quantity)と売上高(Purchase revenue)

# COMMAND ----------

city_purchase_quantities_df = df.groupBy("geo.state", "geo.city").sum("ecommerce.total_item_quantity", "ecommerce.purchase_revenue_in_usd")
display(city_purchase_quantities_df)

# COMMAND ----------

# DBTITLE 0,--i18n-41705fda-f6ec-4008-8561-3d89b337ba35
# MAGIC %md
# MAGIC ### 4.組み込み関数（Built-In Functions）
# MAGIC DataFrameやColumnの変換メソッドに加え、Sparkの <a href="https://docs.databricks.com/spark/latest/spark-sql/language-manual/sql-ref-functions-builtin.html" target="_blank">SQL functions</a> モジュールには便利な関数（Functions）がたくさんあります。
# MAGIC
# MAGIC Scalaにおいては, こちらの <a href="https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/functions$.html" target="_blank">**`org.apache.spark.sql.functions`**</a>を、そしてPythonにおいては <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql.html#functions" target="_blank">**`pyspark.sql.functions`**</a>を参照してください。
# MAGIC なお、このこのモジュールにある関数を利用する場合は、このモジュールを必ずimportしてください。

# COMMAND ----------

# DBTITLE 0,--i18n-4c587ad6-517c-4416-8ed9-24df20602f8e
# MAGIC %md
# MAGIC ### 集約関数（Aggregate Functions）
# MAGIC
# MAGIC いくつかの集約（Aggregation）に関する組み込み関数が使用可能です。
# MAGIC
# MAGIC | メソッド | 説明 |
# MAGIC | --- | --- |
# MAGIC | approx_count_distinct | グループ内の一意な項目数の近似数を返す |
# MAGIC | avg | グループ内の値の平均値を計算 |
# MAGIC | collect_list | 重複を含むオブジェクトのリストを返す |
# MAGIC | corr | 2つの列のピアソン相関係数を計算 |
# MAGIC | max | 各グループの各数値列の最大値を計算 |
# MAGIC | mean | 各グループの各数値列の平均値を計算 |
# MAGIC | stddev_samp | グループ内の式の標本標準偏差を計算 |
# MAGIC | sumDistinct | 特定の式内での一意な値の合計値を計算 |
# MAGIC | var_pop | グループ内の値の母集団分散を計算 |
# MAGIC
# MAGIC
# MAGIC 組み込み集約関数（Aggregate functions）を適用するためには、グループ化データメソッドにおいて、
# MAGIC  <a href="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.GroupedData.agg.html#pyspark.sql.GroupedData.agg" target="_blank">**`agg`**</a> を使用してください。
# MAGIC
# MAGIC これにより、<a href="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.Column.alias.html" target="_blank">**`alias`**</a>　のような、結果の列に他の変換処理を適応することができます。

# COMMAND ----------

from pyspark.sql.functions import sum

state_purchases_df = df.groupBy("geo.state").agg(sum("ecommerce.total_item_quantity").alias("total_purchases"))
display(state_purchases_df)

# COMMAND ----------

# DBTITLE 0,--i18n-0cbb1c99-23da-45cd-85f2-b4de3e6d2587
# MAGIC %md
# MAGIC グループ化されたデータ上ので、複数の集約関数（Aggregate functions）の適応

# COMMAND ----------

from pyspark.sql.functions import avg, approx_count_distinct

state_aggregates_df = (df
                       .groupBy("geo.state")
                       .agg(avg("ecommerce.total_item_quantity").alias("avg_quantity"),
                            approx_count_distinct("user_id").alias("distinct_users"))
                      )

display(state_aggregates_df)

# COMMAND ----------

# DBTITLE 0,--i18n-fbc371d8-a5c5-46e4-856c-43e84b029d72
# MAGIC %md
# MAGIC ### 数学関数（Math Functions）
# MAGIC いくつかの数学演算に使用できる組み込み関数が使用可能です。
# MAGIC
# MAGIC | メソッド | 説明 |
# MAGIC | --- | --- |
# MAGIC | ceil | 指定した列の切り上げ値を計算 |
# MAGIC | cos | 指定した値の余弦（Cosine）値を計算 |
# MAGIC | log | 指定下値の自然対数（the natural logarithm）を計算 |
# MAGIC | round | HALF_UPの丸めモードで、列eの値を小数点以下0桁に丸めた値を返す　|
# MAGIC | sqrt | 指定された浮動小数点数の平方根（the square root）を計算 |

# COMMAND ----------

from pyspark.sql.functions import cos, sqrt

display(spark.range(10)  # Create a DataFrame with a single column called "id" with a range of integer values
        .withColumn("sqrt", sqrt("id"))
        .withColumn("cos", cos("id"))
       )

# COMMAND ----------

# DBTITLE 0,--i18n-cfb43a90-72e5-466e-82e6-31e1f14dfbf3
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
