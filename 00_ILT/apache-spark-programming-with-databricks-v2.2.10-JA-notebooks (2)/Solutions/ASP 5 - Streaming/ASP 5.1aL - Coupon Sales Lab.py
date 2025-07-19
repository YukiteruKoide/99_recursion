# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-c22511ee-b15c-4a9f-a051-c905b8e344e9
# MAGIC %md
# MAGIC # クーポン販売 ラボ (Coupon Sales Lab)
# MAGIC クーポンを使ったトランザクションのストリーミングデータを処理して追加します。
# MAGIC 1. データストリームの読み込み
# MAGIC 2. クーポンコードを使った取引のフィルタリング
# MAGIC 3. ストリーミングクエリの結果をデルタに書き込む
# MAGIC 4. ストリーミングクエリの監視
# MAGIC 5. ストリーミングクエリの停止
# MAGIC
# MAGIC ##### クラス (Classes)
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.DataStreamReader.html" target="_blank">DataStreamReader</a>
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.DataStreamWriter.html" target="_blank">DataStreamWriter</a>
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.StreamingQuery.html" target="_blank">StreamingQuery</a>

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-5.1a

# COMMAND ----------

# DBTITLE 0,--i18n-d166abd5-a348-46f9-8134-72f510207bc1
# MAGIC %md
# MAGIC ### 1. データストリームの読み込み (Read data stream)
# MAGIC - トリガーごとに１ファイルずつ処理されるように設定してください
# MAGIC - <strong>`DA.paths.sales`</strong>で指定されたソースディレクトリにあるデルタファイルを読み込んでください
# MAGIC
# MAGIC 出来たDataframeを<strong>`df`</strong>に割り当ててください。

# COMMAND ----------

# ANSWER
df = (spark
      .readStream
      .option("maxFilesPerTrigger", 1)
      .format("delta")
      .load(DA.paths.sales)
     )

# COMMAND ----------

# DBTITLE 0,--i18n-7655ea48-abe2-4ff2-abf3-3d25e728fbe3
# MAGIC %md
# MAGIC **1.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_1_1(df)

# COMMAND ----------

# DBTITLE 0,--i18n-d3f81153-b55d-4ce8-9012-91fd09185880
# MAGIC %md
# MAGIC ### 2. クーポンコードを使った取引のフィルタリング (Filter for transactions with coupon codes)
# MAGIC - <strong>`df`</strong>の<strong>`items`</strong>フィールドをエクスプロードした結果で、既存の<strong>`items`</strong>フィールドを上書きしてください
# MAGIC - <strong>`items.coupon`</strong>がnullでないレコードを抽出してください
# MAGIC
# MAGIC 出来たDataframeを<strong>`coupon_sales_df`</strong>に割り当ててください。

# COMMAND ----------

# ANSWER
t
t
coupon_sales_df = (df
                   .withColumn("items", explode(col("items")))
                   .filter(col("items.coupon").isNotNull())
                  )

# COMMAND ----------

# DBTITLE 0,--i18n-37e4766a-e845-4b4e-9e7e-82d63fbfc29f
# MAGIC %md
# MAGIC **2.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_2_1(coupon_sales_df.schema)

# COMMAND ----------

# DBTITLE 0,--i18n-793d6d02-ac0b-4dfa-b711-b4a01636e099
# MAGIC %md
# MAGIC ### 3. ストリーミングクエリの結果をデルタに書き込む (Write streaming query results to Delta)
# MAGIC - 「append」モードでデルタフォーマットのファイルに出力するようにストリーミングクエリーを設定してください
# MAGIC - クエリー名を「coupon_sales」と設定してください
# MAGIC - トリガー間隔を1秒に設定してください
# MAGIC - チェックポイントのロケーションを<strong>`coupons_checkpoint_path`</strong>に設定してください
# MAGIC - 出力ファイルのパスを<strong>`coupons_output_path`</strong>に設定してください
# MAGIC
# MAGIC ストリーミングクエリーを開始し、出来たハンドルを<strong>`coupon_sales_query`</strong>に割り当ててください。

# COMMAND ----------

# ANSWER

coupons_checkpoint_path = f"{DA.paths.checkpoints}/coupon-sales"
coupons_output_path = f"{DA.paths.working_dir}/coupon-sales/output"

coupon_sales_query = (coupon_sales_df
                      .writeStream
                      .outputMode("append")
                      .format("delta")
                      .queryName("coupon_sales")
                      .trigger(processingTime="1 second")
                      .option("checkpointLocation", coupons_checkpoint_path)
                      .start(coupons_output_path))

DA.block_until_stream_is_ready(coupon_sales_query)

# COMMAND ----------

# DBTITLE 0,--i18n-204ee663-db1b-441a-9084-a58a9aa88a9c
# MAGIC %md
# MAGIC **3.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_3_1(coupon_sales_query)

# COMMAND ----------

# DBTITLE 0,--i18n-a8c6095a-6725-4ecc-8c23-f85832d548f9
# MAGIC %md
# MAGIC ### 4. ストリーミングクエリの監視 (Monitor streaming query)
# MAGIC - ストリーミングクエリのIDを取得して<strong>`queryID`</strong>に格納してください
# MAGIC - ストリーミングクエリの状態を取得して<strong>`queryStatus`</strong>に格納してください

# COMMAND ----------

# ANSWER
query_id = coupon_sales_query.id
print(query_id)

# COMMAND ----------

# ANSWER
query_status = coupon_sales_query.status
print(query_status)

# COMMAND ----------

# DBTITLE 0,--i18n-80d700dc-c312-4c0d-8997-1ce7fe69aefd
# MAGIC %md
# MAGIC **4.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_4_1(query_id, query_status)

# COMMAND ----------

# DBTITLE 0,--i18n-fac79dfb-738f-4c44-ae25-8e9439866be6
# MAGIC %md
# MAGIC ### 5. ストリーミングクエリの停止 (Stop streaming query)
# MAGIC - ストリーミングクエリを停止してください

# COMMAND ----------

# ANSWER
coupon_sales_query.stop()
coupon_sales_query.awaitTermination()

# COMMAND ----------

# DBTITLE 0,--i18n-4b582543-cdec-47f0-9ee3-55a8b2dc42db
# MAGIC %md
# MAGIC **5.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_5_1(coupon_sales_query)

# COMMAND ----------

# DBTITLE 0,--i18n-9e759d24-b277-4237-86ff-92650fdac8f7
# MAGIC %md
# MAGIC ### 6. レコードがデルタフォーマットで書き込まれたことを確認する (Verify the records were written in Delta format)

# COMMAND ----------

# ANSWER
display(spark.read.format("delta").load(coupons_output_path))

# COMMAND ----------

# DBTITLE 0,--i18n-7917bc49-1f8c-404a-b37c-76fa3d945620
# MAGIC %md
# MAGIC ### クラスルームで使ったリソースの削除 (Classroom Cleanup)
# MAGIC 以下のセルを実行してリソースを削除してください。

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
