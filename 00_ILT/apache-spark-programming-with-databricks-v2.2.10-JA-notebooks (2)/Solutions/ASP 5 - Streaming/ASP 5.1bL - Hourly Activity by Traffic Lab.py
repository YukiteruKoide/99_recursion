# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-5d844227-898e-41b2-adf0-bdc282c32a19
# MAGIC %md
# MAGIC ## 時間ごとのトラフィックソース (Hourly Activity by Traffic Lab)
# MAGIC ストリーミングのデータを処理し、トラフィックソースごとに1時間のウィンドウでアクティブユーザー数を表示します。
# MAGIC 1. timestamp型にキャストして2時間のウォーターマークを加える
# MAGIC 2. トラフィックソースごとにアクティブユーザーを１時間のウィンドウで集約する
# MAGIC 3. クエリーを<strong>`display`</strong>で実行し結果を表示する
# MAGIC 4. クエリー名を使ってストリーミングクエリーを停止する

# COMMAND ----------

# DBTITLE 0,--i18n-734c8d4c-5d28-4370-9403-1531ae27fd3c
# MAGIC %md
# MAGIC ### セットアップ (Setup)
# MAGIC 以下のセルを実行し、2020年7月3日分のイベントデータに該当するJSONファイルを生成してください。

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-5.1b

# COMMAND ----------

schema = "device STRING, ecommerce STRUCT<purchase_revenue_in_usd: DOUBLE, total_item_quantity: BIGINT, unique_items: BIGINT>, event_name STRING, event_previous_timestamp BIGINT, event_timestamp BIGINT, geo STRUCT<city: STRING, state: STRING>, items ARRAY<STRUCT<coupon: STRING, item_id: STRING, item_name: STRING, item_revenue_in_usd: DOUBLE, price_in_usd: DOUBLE, quantity: BIGINT>>, traffic_source STRING, user_first_touch_timestamp BIGINT, user_id STRING"

# Directory of hourly events logged from the BedBricks website on July 3, 2020
hourly_events_path = f"{DA.paths.datasets}/ecommerce/events/events-2020-07-03.json"

df = (spark.readStream
           .schema(schema)
           .option("maxFilesPerTrigger", 1)
           .json(hourly_events_path))

# COMMAND ----------

# DBTITLE 0,--i18n-99264197-aba0-4df5-8346-8501cd6efba0
# MAGIC %md
# MAGIC ### 1. timestamp型にキャストして2時間のウォーターマークを加える (Cast to timestamp and add watermark for 2 hours)
# MAGIC - <strong>`event_timestamp`</strong>を100万で割りtimestamp型にキャストして<strong>`createdAt`</strong>カラムとして追加します
# MAGIC - <strong>`createdAt`</strong>カラムに2時間のウォーターマークを加えます
# MAGIC
# MAGIC 出来たDataframeを<strong>`events_df`</strong>に割り当てます。

# COMMAND ----------

# ANSWER
from pyspark.sql.functions import col

events_df = (df.withColumn("createdAt", (col("event_timestamp") / 1e6).cast("timestamp"))
               .withWatermark("createdAt", "2 hours"))

# COMMAND ----------

# DBTITLE 0,--i18n-73d176cb-bf2f-450b-bdaf-a72427e0947d
# MAGIC %md
# MAGIC **1.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_1_1(events_df.schema)

# COMMAND ----------

# DBTITLE 0,--i18n-db2b1906-b389-4f49-889c-c9474d381a3f
# MAGIC %md
# MAGIC ### 2. トラフィックソースごとにアクティブユーザーを１時間のウィンドウで集約する (Aggregate active users by traffic source for 1 hour windows)
# MAGIC
# MAGIC - デフォルトのシャッフルパーティションをあなたが使っているクラスターのコア数になるように設定してください
# MAGIC - <strong>`createdAt`</strong>カラムに基づいた1時間のタンブリングウィンドウを使い<strong>`traffic_source`</strong>カラムでグループ化してください
# MAGIC - <strong>`user_id`</strong>単位でユニークなデータ数を近似集計(approx_count_distinct)し、カラム名を`active_users`としてください
# MAGIC - <strong>`traffic_source`</strong>、<strong>`active_users`</strong>そして<strong>`window.start`</strong>から抽出して<strong>`hour`</strong>というカラム名にしたものを選択(select)してください
# MAGIC - <strong>`hour`</strong>の昇順でソートしてください
# MAGIC 出来たDataframeを<strong>`traffic_df`</strong>に割り当てます。

# COMMAND ----------

# ANSWER
from pyspark.sql.functions import approx_count_distinct, hour, window

spark.conf.set("spark.sql.shuffle.partitions", spark.sparkContext.defaultParallelism)

traffic_df = (events_df
              .groupBy("traffic_source", window(col("createdAt"), "1 hour"))
              .agg(approx_count_distinct("user_id").alias("active_users"))
              .select(col("traffic_source"), col("active_users"), hour(col("window.start")).alias("hour"))
              .sort("hour")
             )

# COMMAND ----------

# DBTITLE 0,--i18n-2a1ee964-474d-450f-99e2-9c023406fa73
# MAGIC %md
# MAGIC **2.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_2_1(traffic_df.schema)

# COMMAND ----------

# DBTITLE 0,--i18n-690240f6-4981-405c-8719-2f24054c889d
# MAGIC %md
# MAGIC ### 3. クエリーを<strong>`display`</strong>で実行し結果を表示する (Execute query with display() and plot results)
# MAGIC - <strong>`display`</strong>を使って<strong>`traffic_df`</strong>をストリーミングクエリーとして開始させ、出力されるメモリーシンクを表示します
# MAGIC   - <strong>`display`</strong>の<strong>`streamName`</strong>パラメーターを設定することによりクエリー名を"hourly_traffic"としてください
# MAGIC - ストリーミングクエリーの結果を棒グラフとしてプロットしてください
# MAGIC - 次のプロットオプションを設定します:
# MAGIC   - キー: **`hour`**
# MAGIC   - シリーズのグループ化: **`traffic_source`**
# MAGIC   - 値: **`active_users`**

# COMMAND ----------

# ANSWER
display(traffic_df, streamName="hourly_traffic")

# COMMAND ----------

# DBTITLE 0,--i18n-80df0c45-6643-4933-816a-3c63b68719a0
# MAGIC %md
# MAGIC **3.1: 作業結果の確認 (CHECK YOUR WORK)**
# MAGIC
# MAGIC - 棒グラフは<strong>`hour`</strong>をX軸に、<strong>`active_users`</strong>をY軸にプロットされるはず
# MAGIC - 全てのトラフィックソースで毎時6つの棒が表示されるはず
# MAGIC - チャートは23時で終了するはず

# COMMAND ----------

# DBTITLE 0,--i18n-f9ef0d57-9b71-4bfa-ae83-b854770c603d
# MAGIC %md
# MAGIC ### 4. ストリーミングクエリーを管理する (Manage streaming query)
# MAGIC - SparkSessionのアクティブなストリームのリストを順に探り、"hourly_traffic"という名前のものを見つけてください
# MAGIC - ストリーミングクエリーを停止してください

# COMMAND ----------

# ANSWER
DA.block_until_stream_is_ready("hourly_traffic")

for s in spark.streams.active:
    if s.name == "hourly_traffic":
        s.stop()
        s.awaitTermination()

# COMMAND ----------

# DBTITLE 0,--i18n-9ecfd9e1-edfd-4964-b45e-fa207f194320
# MAGIC %md
# MAGIC **4.1: 作業結果の確認 (CHECK YOUR WORK)**
# MAGIC
# MAGIC 全てのアクティブなストリームを出力して、"hourly_traffic"がもう存在しないことを確認してください

# COMMAND ----------

DA.tests.validate_4_1()

# COMMAND ----------

# DBTITLE 0,--i18n-a78e18c1-6071-4759-9e57-61060aab83bc
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
