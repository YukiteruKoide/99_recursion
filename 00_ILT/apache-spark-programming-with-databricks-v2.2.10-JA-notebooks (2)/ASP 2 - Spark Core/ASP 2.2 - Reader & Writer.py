# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-66303a31-c6ea-4d3c-9e11-abd55993c014
# MAGIC %md
# MAGIC # Reader & Writer
# MAGIC ##### 目的 (Objectives)
# MAGIC 1. CSVファイルからの読み込み
# MAGIC 1. JSONファイルからの読み込み
# MAGIC 1. DataFrameをファイルに書き込む
# MAGIC 1. DataFrameをテーブルに書き込む
# MAGIC 1. デルタテーブルにDataFrameを書き込む
# MAGIC
# MAGIC ##### メソッド (Methods)
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.html" target="_blank">DataFrameReader</a>: **`csv`**, **`json`**, **`option`**, **`schema`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.html" target="_blank">DataFrameWriter</a>: **`mode`**, **`option`**, **`parquet`**, **`format`**, **`saveAsTable`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.types.StructType.html?highlight=structtype#pyspark.sql.types.StructType" target="_blank">StructType</a>: **`toDDL`**
# MAGIC
# MAGIC ##### Sparkタイプ
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/data_types.html" target="_blank">タイプ</a>: **`ArrayType`**, **`DoubleType`**, **`IntegerType`**, **`LongType`**, **`StringType`**, **`StructType`**, **`StructField`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-7f74aa58-3c7e-4485-be3e-60ed16d191b0
# MAGIC %md
# MAGIC ## DataFrameからの読み込み
# MAGIC 外部ストレージシステムからDataFrameを読み込むために使用するインターフェース
# MAGIC
# MAGIC **`spark.read.parquet("path/to/files")`**
# MAGIC
# MAGIC DataFrameReader は SparkSession の属性 **`read`** からアクセスできます。このクラスには、さまざまな外部ストレージシステムからDataFrameを読み込むためのメソッドが含まれています。

# COMMAND ----------

# DBTITLE 0,--i18n-5bba9927-0496-4938-9f87-f2f47d978d64
# MAGIC %md
# MAGIC ### CSV ファイルからの読み込み
# MAGIC DataFrameReaderの **`csv`** メソッドと以下のオプションを使ってCSVから読み込みます。
# MAGIC
# MAGIC タブ区切り、 最初の行をヘッダーとして使用、 スキーマを推論

# COMMAND ----------

users_csv_path = f"{DA.paths.datasets}/ecommerce/users/users-500k.csv"

users_df = (spark
           .read
           .option("sep", "\t")
           .option("header", True)
           .option("inferSchema", True)
           .csv(users_csv_path)
          )

users_df.printSchema()

# COMMAND ----------

# DBTITLE 0,--i18n-a5b22677-d1b5-4cb0-a08a-9e98626ba587
# MAGIC %md
# MAGIC SparkのPython APIでは、DataFrameReaderのオプションを **`csv`** メソッドのパラメータとして指定することも可能です。

# COMMAND ----------

users_df = (spark
           .read
           .csv(users_csv_path, sep="\t", header=True, inferSchema=True)
          )

users_df.printSchema()

# COMMAND ----------

# DBTITLE 0,--i18n-af4cc86a-1345-4fca-af9e-9c8536e11c18
# MAGIC %md
# MAGIC カラム名とデータ型を持つ **`StructType`** を作成し、スキーマを手動で定義します。

# COMMAND ----------

from pyspark.sql.types import LongType, StringType, StructType, StructField

user_defined_schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("user_first_touch_timestamp", LongType(), True),
    StructField("email", StringType(), True)
])

# COMMAND ----------

# DBTITLE 0,--i18n-1126fe7b-87eb-44e9-bcd4-a75bc5b119a6
# MAGIC %md
# MAGIC スキーマを推論するのではなく、以下ユーザー定義のスキーマを使ってCSVから読み取ります。

# COMMAND ----------

users_df = (spark
           .read
           .option("sep", "\t")
           .option("header", True)
           .schema(user_defined_schema)
           .csv(users_csv_path)
          )

# COMMAND ----------

# DBTITLE 0,--i18n-92d687de-c80c-429a-9522-cb032ba13a9b
# MAGIC %md
# MAGIC あるいは、<a href="https://en.wikipedia.org/wiki/Data_definition_language" target="_blank">データ定義言語（DDL）</a>構文を使ってスキーマを定義します。

# COMMAND ----------

ddl_schema = "user_id string, user_first_touch_timestamp long, email string"

users_df = (spark
           .read
           .option("sep", "\t")
           .option("header", True)
           .schema(ddl_schema)
           .csv(users_csv_path)
          )

# COMMAND ----------

# DBTITLE 0,--i18n-e6eb716e-4634-4ced-9771-711541761085
# MAGIC %md
# MAGIC ### JSONファイルからの読み込み
# MAGIC
# MAGIC DataFrameReaderの **`json`** メソッドとinfer schemaオプションでJSONから読み込みます。

# COMMAND ----------

events_json_path = f"{DA.paths.datasets}/ecommerce/events/events-500k.json"

events_df = (spark
            .read
            .option("inferSchema", True)
            .json(events_json_path)
           )

events_df.printSchema()

# COMMAND ----------

# DBTITLE 0,--i18n-7ca81f5a-08e3-44c9-b935-e5c5c666c815
# MAGIC %md
# MAGIC スキーマ名とデータ型を指定して **`StructType`** を作成することにより、データをより高速に読み取ります。

# COMMAND ----------

from pyspark.sql.types import ArrayType, DoubleType, IntegerType, LongType, StringType, StructType, StructField

user_defined_schema = StructType([
    StructField("device", StringType(), True),
    StructField("ecommerce", StructType([
        StructField("purchaseRevenue", DoubleType(), True),
        StructField("total_item_quantity", LongType(), True),
        StructField("unique_items", LongType(), True)
    ]), True),
    StructField("event_name", StringType(), True),
    StructField("event_previous_timestamp", LongType(), True),
    StructField("event_timestamp", LongType(), True),
    StructField("geo", StructType([
        StructField("city", StringType(), True),
        StructField("state", StringType(), True)
    ]), True),
    StructField("items", ArrayType(
        StructType([
            StructField("coupon", StringType(), True),
            StructField("item_id", StringType(), True),
            StructField("item_name", StringType(), True),
            StructField("item_revenue_in_usd", DoubleType(), True),
            StructField("price_in_usd", DoubleType(), True),
            StructField("quantity", LongType(), True)
        ])
    ), True),
    StructField("traffic_source", StringType(), True),
    StructField("user_first_touch_timestamp", LongType(), True),
    StructField("user_id", StringType(), True)
])

events_df = (spark
            .read
            .schema(user_defined_schema)
            .json(events_json_path)
           )

# COMMAND ----------

# DBTITLE 0,--i18n-a8ad41a8-413e-466a-97f7-d5195258ae10
# MAGIC %md
# MAGIC `StructType`の Scalaのメソッドである `toDDL` を使用すると、DDL形式の文字列を作成することができます。
# MAGIC
# MAGIC それは、CSV と JSON を取り込むために DDL 形式の文字列を取得する必要があるが、手動で作成したり、スキーマの **`StructType`** バリアントを作成したくない場合に便利です。
# MAGIC
# MAGIC ただし、この機能は Python では利用できませんが、Databricksノートブックの機能により、両方の言語を使用できます。

# COMMAND ----------

# Step 1 - use this trick to transfer a value (the dataset path) between Python and Scala using the shared spark-config
spark.conf.set("whatever_your_scope.events", events_json_path)

# COMMAND ----------

# DBTITLE 0,--i18n-5dde5648-2a28-47b6-98c2-2b78d6a655d0
# MAGIC %md
# MAGIC このような Python ノートブックで、Scala セルを作成してデータを取り込み、DDL 形式のスキーマを生成します。

# COMMAND ----------

# MAGIC %scala
# MAGIC // Step 2 - pull the value from the config (or copy & paste it)
# MAGIC val eventsJsonPath = spark.conf.get("whatever_your_scope.events")
# MAGIC
# MAGIC // Step 3 - Read in the JSON, but let it infer the schema
# MAGIC val eventsSchema = spark.read
# MAGIC                         .option("inferSchema", true)
# MAGIC                         .json(eventsJsonPath)
# MAGIC                         .schema.toDDL
# MAGIC
# MAGIC // Step 4 - print the schema, select it, and copy it.
# MAGIC println("="*80)
# MAGIC println(eventsSchema)
# MAGIC println("="*80)

# COMMAND ----------

# Step 5 - paste the schema from above and assign it to a variable as seen here
events_schema = "`device` STRING,`ecommerce` STRUCT<`purchase_revenue_in_usd`: DOUBLE, `total_item_quantity`: BIGINT, `unique_items`: BIGINT>,`event_name` STRING,`event_previous_timestamp` BIGINT,`event_timestamp` BIGINT,`geo` STRUCT<`city`: STRING, `state`: STRING>,`items` ARRAY<STRUCT<`coupon`: STRING, `item_id`: STRING, `item_name`: STRING, `item_revenue_in_usd`: DOUBLE, `price_in_usd`: DOUBLE, `quantity`: BIGINT>>,`traffic_source` STRING,`user_first_touch_timestamp` BIGINT,`user_id` STRING"

# Step 6 - Read in the JSON data using our new DDL formatted string
events_df = (spark.read
                 .schema(events_schema)
                 .json(events_json_path))

display(events_df)

# COMMAND ----------

# DBTITLE 0,--i18n-f625ff39-c731-4c7b-a3c0-5b1c0b0ed760
# MAGIC %md
# MAGIC これは、まったく新しいデータセットのスキーマを作成し、開発を加速するための優れた「トリック」です。
# MAGIC
# MAGIC 完了したら (ステップ 7 など)、一時コードを必ず削除してください。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_warn_32.png"> 警告: **本番環境ではこのトリックを使用しないでください**</br>
# MAGIC スキーマの推論は非常に遅くなる可能性があります。
# MAGIC スキーマを推測するために、強制的に全ソース データセットを読み取ります。

# COMMAND ----------

# DBTITLE 0,--i18n-e1ba25ff-646a-434a-94aa-1dda43388eec
# MAGIC %md
# MAGIC ## DataFrameWriter
# MAGIC DataFrame を外部ストレージ システムに書き込むために使用されるインターフェイス
# MAGIC
# MAGIC <strong><code>
# MAGIC (df  
# MAGIC &nbsp;  .write                         
# MAGIC &nbsp;  .option("compression", "snappy")  
# MAGIC &nbsp;  .mode("overwrite")      
# MAGIC &nbsp;  .parquet(output_dir)       
# MAGIC )
# MAGIC </code></strong>
# MAGIC
# MAGIC DataFrameWriter は、SparkSession 属性 **`write`** を介してアクセスできます。 このクラスには、DataFrame をさまざまな外部ストレージ システムに書き込むためのメソッドが含まれています。

# COMMAND ----------

# DBTITLE 0,--i18n-67e5c4f1-cb91-450d-a537-288dec6a8a53
# MAGIC %md
# MAGIC ### DataFramesをファイルに書き込む
# MAGIC
# MAGIC 以下の構成で **`users_df`** を DataFrameWriter の **`parquet`** メソッドで書き込みます。
# MAGIC
# MAGIC Snappy 圧縮、上書きモード

# COMMAND ----------

users_output_dir = f"{DA.paths.working_dir}/users.parquet"

(users_df
 .write
 .option("compression", "snappy")
 .mode("overwrite")
 .parquet(users_output_dir)
)

# COMMAND ----------

display(
    dbutils.fs.ls(users_output_dir)
)

# COMMAND ----------

# DBTITLE 0,--i18n-e2773c8e-02a1-4c6d-8089-5e6e3c7f0952
# MAGIC %md
# MAGIC DataFrameReader と同様に、Spark の Python API では、 **`parquet`** メソッドのパラメーターとして DataFrameWriter オプションを指定することもできます。

# COMMAND ----------

(users_df
 .write
 .parquet(users_output_dir, compression="snappy", mode="overwrite")
)

# COMMAND ----------

# DBTITLE 0,--i18n-e7eda404-11d6-4e3e-96b1-0abb3c15b1fb
# MAGIC %md
# MAGIC ### DataFrame をテーブルに書き込む
# MAGIC
# MAGIC **`events_df`** を DataFrameWriter メソッド **`saveAsTable`** を使用してテーブルに書き込みます
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_32.png" alt="Note"> 今回はDataFrame の **`createOrReplaceTempView`** メソットによって作成されるローカル ビューとは異なり、グローバル テーブルを作成します。

# COMMAND ----------

events_df.write.mode("overwrite").saveAsTable("events")

# COMMAND ----------

# DBTITLE 0,--i18n-99ce9f84-63bf-4f6f-9518-c7b2b9160627
# MAGIC %md
# MAGIC This table was saved in the database created for you in classroom setup.
# MAGIC
# MAGIC See database name printed below.
# MAGIC
# MAGIC このテーブルは、ノートブックの設定で作成されたデータベースに保存されています。
# MAGIC
# MAGIC 以下に表記されたデータベース名を参照してください。

# COMMAND ----------

print(f"Database Name: {DA.schema_name}")

# COMMAND ----------

# DBTITLE 0,--i18n-ca9ca576-c72c-4522-844e-1fa458b68b80
# MAGIC %md
# MAGIC データベース内でもテーブルを参照できます。

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN ${DA.schema_name}

# COMMAND ----------

# DBTITLE 0,--i18n-32d25721-e313-44bf-a576-842eaab570af
# MAGIC %md
# MAGIC ## Delta Lake
# MAGIC
# MAGIC
# MAGIC ほとんどの場合、特にデータが Databricks ワークスペースから参照される場合は常に、Delta Lake 形式を使用することがベスト プラクティスです。
# MAGIC
# MAGIC <a href="https://delta.io/" target="_blank">Delta Lake</a> はspark と連携してデータ レイクに信頼性をもたらすように設計されたオープン ソース テクノロジです。
# MAGIC
# MAGIC ![delta](https://files.training.databricks.com/images/aspwd/delta_storage_layer.png)
# MAGIC
# MAGIC #### Delta Lakeの主な特長
# MAGIC ACID トランザクション
# MAGIC - スケーラブルなメタデータ処理
# MAGIC - 統合されたストリーミングとバッチ処理
# MAGIC - タイムトラベル (データのバージョン管理)
# MAGIC - スキーマの適用と進化
# MAGIC - 監査履歴
# MAGIC - Parquet フォーマット
# MAGIC - Apache Spark API との互換性

# COMMAND ----------

# DBTITLE 0,--i18n-eef7e839-93de-48bc-8267-d27b1996a9ed
# MAGIC %md
# MAGIC ### Delta Tableに結果を書き込む
# MAGIC
# MAGIC 以下の構成で DataFrameWriter の **`save`** メソッドで **`events_df`** を書き込みます: 
# MAGIC
# MAGIC Delta 形式と上書きモード。

# COMMAND ----------

events_output_path = f"{DA.paths.working_dir}/delta/events"

(events_df
 .write
 .format("delta")
 .mode("overwrite")
 .save(events_output_path)
)

# COMMAND ----------

# DBTITLE 0,--i18n-05f47836-3d11-4204-ad80-50e573bd6d2f
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
