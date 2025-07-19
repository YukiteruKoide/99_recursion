# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-626549c9-0309-43a3-baec-ae0fdcaa35ca
# MAGIC %md
# MAGIC # パーティショニング (Partitioning)
# MAGIC ##### 目的 (Objectives)
# MAGIC 1. パーティションとコアの取得
# MAGIC 1. データフレームの再パーティショニング
# MAGIC 1. デフォルトのシャッフルパーティションの設定
# MAGIC
# MAGIC ##### メソッド (Methods)
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrame</a>: **`repartition`**, **`coalesce`**, **`rdd.getNumPartitions`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkConf.html" target="_blank">SparkConf</a>: **`get`**, **`set`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.html" target="_blank">SparkSession</a>: **`spark.sparkContext.defaultParallelism`**
# MAGIC
# MAGIC ##### SparkConfパラメーター (SparkConf Parameters)
# MAGIC - **`spark.sql.shuffle.partitions`**, **`spark.sql.adaptive.enabled`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-17830688-7910-42d3-a253-c688ff562e9c
# MAGIC %md
# MAGIC ### パーティションとコアの取得 (Get partitions and cores)
# MAGIC
# MAGIC <strong>`rdd`</strong>の<strong>`getNumPartitions`</strong>メソッドを使ってデータフレームのパーティション数を取得してみましょう。

# COMMAND ----------

df = spark.read.format("delta").load(DA.paths.events)
df.rdd.getNumPartitions()

# COMMAND ----------

# DBTITLE 0,--i18n-845301f4-e139-4dff-a6ad-c78d3b8aceee
# MAGIC %md
# MAGIC <strong>`SparkContext`</strong>経由で<strong>SparkContext</strong>にアクセスしてコア数やスロット数を取得します。
# MAGIC
# MAGIC <strong>`defaultParallelism`</strong>属性を使ってクラスターのコア数を取得します。

# COMMAND ----------

print(spark.sparkContext.defaultParallelism)

# COMMAND ----------

# DBTITLE 0,--i18n-2b54cb1e-fff0-432d-9a26-dc26efe90a24
# MAGIC %md
# MAGIC <strong>`SparkContext`</strong>はDatabricksのノートブックでは、変数<strong>`sc`</strong>としても提供されています。

# COMMAND ----------

print(sc.defaultParallelism)

# COMMAND ----------

# DBTITLE 0,--i18n-7e13bd07-e839-45f5-b727-d9763e7e83d6
# MAGIC %md
# MAGIC ### データフレームの再パーティショニング (Repartition DataFrame)
# MAGIC
# MAGIC データフレームの再パーティショニングのためのメソッドとしてこの２つがあります: <strong>`repartition`</strong>、<strong>`coalesce`</strong>

# COMMAND ----------

# DBTITLE 0,--i18n-728b9e76-ac70-4003-bc8c-dcde137155f1
# MAGIC %md
# MAGIC #### **`repartition`**
# MAGIC 正確に<strong>`n`</strong>個のパーティションを持つ新しいデータフレームを返します。
# MAGIC
# MAGIC - ワイドトランスフォーメーション
# MAGIC - 長所: パーティションの大きさを均等にできる  
# MAGIC - 短所: 全てのデータをシャッフルする必要がある

# COMMAND ----------

repartitioned_df = df.repartition(8)

# COMMAND ----------

repartitioned_df.rdd.getNumPartitions()

# COMMAND ----------

# DBTITLE 0,--i18n-1d5bbde0-3619-44ff-8fc6-b62a794b6e94
# MAGIC %md
# MAGIC #### **`coalesce`**
# MAGIC より少ない数のパーティションが要求された場合、正確に<strong>`n`</strong>個のパーティションを持つ新しいデータフレームを返します。
# MAGIC
# MAGIC より大きな数のパーティションが要求された場合、現在のパーティション数のままになります。
# MAGIC
# MAGIC - ナロートランスフォーメーションであり、いくつかのパーティションが効果的に結合されます
# MAGIC - 長所: シャッフルが必要ない
# MAGIC - 短所:
# MAGIC   - パーティション数を増やすことはできない
# MAGIC   - パーティションの大きさが不均等になることがある

# COMMAND ----------

coalesce_df = df.coalesce(8)

# COMMAND ----------

coalesce_df.rdd.getNumPartitions()

# COMMAND ----------

# DBTITLE 0,--i18n-5724d4ef-45d8-44db-a703-d6827dbfde91
# MAGIC %md
# MAGIC ### デフォルトのシャッフルパーティションの設定 (Configure default shuffle partitions)
# MAGIC
# MAGIC Sparkの動的な設定パラメーターの取得と設定にはSparkSessionの<strong>`conf`</strong>属性を使います。<strong>`spark.sql.shuffle.partitions`</strong>属性は、シャッフルに使用されるパーティション数を決めます。そのデフォルト値を見てみましょう:

# COMMAND ----------

spark.conf.get("spark.sql.shuffle.partitions")

# COMMAND ----------

# DBTITLE 0,--i18n-c67a0a9d-bb97-43a8-aca5-275775e326b7
# MAGIC %md
# MAGIC データセットがそれほど大きくないと仮定すると、シャッフルパーティション数をコア数と同じにするのが良いかもしれません:

# COMMAND ----------

spark.conf.set("spark.sql.shuffle.partitions", spark.sparkContext.defaultParallelism)
print(spark.conf.get("spark.sql.shuffle.partitions"))

# COMMAND ----------

# DBTITLE 0,--i18n-dae30e85-6039-437c-9cb8-cf8cd16c84b9
# MAGIC %md
# MAGIC ### パーティショニングの指針 (Partitioning Guidelines)
# MAGIC - パーティション数がコア数の倍数になるようにします
# MAGIC - 約200MBが、パーティションの推奨サイズです
# MAGIC - デフォルトのシャッフルパーティション数を決めるために、最大のシャッフルステージのインプットを、目標とするパーティションサイズで割ります （例: 4TB / 200MB = 2万 シャッフルパーティション数)
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_32.png" alt="Note"> データフレームをストレージに出力する際、データフレームのパーティション数により出力されるデータファイル数が決まります。 (これは<a href="https://sparkbyexamples.com/apache-hive/hive-partitions-explained-with-examples/" target="_blank">Hiveパーティショニング</a>がストレージのデータで使われない場合の話です。データフレームのパーティショニング対Hiveパーティショニングは本講座の範囲外です。)

# COMMAND ----------

# DBTITLE 0,--i18n-39e11a07-1a9f-4d84-a119-8b1dcbe33405
# MAGIC %md
# MAGIC ### アダプティブ・クエリー・エグゼキューション (Adaptive Query Execution)
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/aspwd/partitioning_aqe.png" width="60%" />
# MAGIC
# MAGIC Spark 3では, <a href="https://spark.apache.org/docs/latest/sql-performance-tuning.html#adaptive-query-execution" target="_blank">AQE</a>は実行時に<a href="https://databricks.com/blog/2020/05/29/adaptive-query-execution-speeding-up-spark-sql-at-runtime.html" target="_blank">シャッフルパーティションを動的に減少</a>させることができます。これは<strong>`spark.sql.shuffle.partitions`</strong>をアプリケーションが処理する最大のデータセットに基づいて決めることができ、処理するデータ数がより少ない場合はAQEが自動的にパーティション数を減少させることができることを意味します。
# MAGIC
# MAGIC <strong>`spark.sql.adaptive.enabled`</strong>設定オプションはAQEのオン、オフを制御します。

# COMMAND ----------

spark.conf.get("spark.sql.adaptive.enabled")

# COMMAND ----------

# DBTITLE 0,--i18n-ed5dae82-9a3a-42b0-990f-2560f8ee59fe
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
