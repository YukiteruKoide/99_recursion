# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-7490cd7f-a3a1-41ac-8fa8-b126983ae4f5
# MAGIC %md
# MAGIC # トラフィックごとのアクティビティラボ (Activity by Traffic Lab)
# MAGIC ストリーミングデータを処理し、トラフィックソースごとのアクティブユーザー数を表示します。
# MAGIC
# MAGIC ##### Objectives
# MAGIC 1. データストリームを読み込む
# MAGIC 2. トラフィックソースごとのアクティブユーザー数を取得する
# MAGIC 3. display()でクエリーを実行し結果をプロットする
# MAGIC 4. DataStreamWriterにより同じストリーミングクエリーを実行する
# MAGIC 5. クエリーテーブル上で結果が更新されているのを確認する
# MAGIC 6. 全てのアクティブなストリームをリストし、停止する
# MAGIC
# MAGIC ##### Classes
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.DataStreamReader.html" target="_blank">DataStreamReader</a>
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.DataStreamWriter.html" target="_blank">DataStreamWriter</a>
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/api/pyspark.sql.streaming.StreamingQuery.html" target="_blank">StreamingQuery</a>

# COMMAND ----------

# DBTITLE 0,--i18n-ffb260b5-eef7-435a-94da-f43d123719f2
# MAGIC %md
# MAGIC ### セットアップ
# MAGIC 以下のセルを実行して、このラボで使うデータと<strong>`schema`</strong>文字列を生成しましょう。

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-5.1c

# COMMAND ----------

# DBTITLE 0,--i18n-5cc77c5c-04f9-4306-a0f2-a8848bf79e60
# MAGIC %md
# MAGIC ### 1. データストリームを読み込む (Read data stream)
# MAGIC - トリガーごとに1ファイルを処理するよう設定します
# MAGIC - <strong>`DA.paths.events`</strong>のファイルパスにあるデルタファイルから読み込みます
# MAGIC
# MAGIC その結果出来るDataframeを<strong>`df`</strong>に割り当てます。

# COMMAND ----------

# TODO
df = FILL_IN

# COMMAND ----------

# DBTITLE 0,--i18n-d1dbded3-bf92-4f51-882f-ff7354079ca4
# MAGIC %md
# MAGIC **1.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_1_1(df)

# COMMAND ----------

# DBTITLE 0,--i18n-a6dada0b-e17f-4491-8b55-de63101d60c4
# MAGIC %md
# MAGIC ### 2. トラフィックソースごとのアクティブユーザー数を取得する (Get active users by traffic source)
# MAGIC - デフォルトのシャッフルパーティションをあなたが使っているクラスターのコア数になるように設定してください(必須ではないですが、処理速度が上がります)
# MAGIC - <strong>`traffic_source`</strong>でグループ化(group by)します
# MAGIC   - ユニークなユーザー数を近似集計(approx_count_distinct)し、そのカラム名を"active_users"としてください
# MAGIC - <strong>`traffic_source`</strong>でソートします

# COMMAND ----------

# TODO
spark.FILL_IN

traffic_df = df.FILL_IN

# COMMAND ----------

# DBTITLE 0,--i18n-b202f51b-7b0c-48bc-a705-fd43b08abd6b
# MAGIC %md
# MAGIC **2.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_2_1(traffic_df.schema)

# COMMAND ----------

# DBTITLE 0,--i18n-048e3d16-65a1-4502-b76a-b5605b454df7
# MAGIC %md
# MAGIC ### 3. display()でクエリーを実行し結果をプロットする (Execute query with display() and plot results)
# MAGIC - display()を使って<strong>`traffic_df`</strong>の結果を出力します
# MAGIC - ストリーミングクエリーの結果を棒グラフでプロットします

# COMMAND ----------

# TODO

# COMMAND ----------

# DBTITLE 0,--i18n-7ba01b58-dfa9-4554-9d33-94edb188a718
# MAGIC %md
# MAGIC **3.1: 作業結果の確認 (CHECK YOUR WORK)**
# MAGIC - 棒グラフはX軸に<strong>`traffic_source`</strong>を、Y軸に<strong>`active_users`</strong>を表示するはずです
# MAGIC - 上位3つのトラフィックソースは、降順に<strong>`google`</strong>、<strong>`facebook`</strong>、<strong>`instagram`</strong>となるはずです

# COMMAND ----------

# DBTITLE 0,--i18n-d5695c83-1fc1-478d-8319-ee6a57f16793
# MAGIC %md
# MAGIC ### 4. DataStreamWriterにより同じストリーミングクエリーを実行する (Execute the same streaming query with DataStreamWriter)
# MAGIC - クエリー名を"active_users_by_traffic"にします
# MAGIC - フォーマットを"memory"に、出力モード(output mode)を"complete"にします
# MAGIC - トリガーの間隔を1秒にします

# COMMAND ----------

# TODO
traffic_query = (traffic_df.FILL_IN
)

# COMMAND ----------

# DBTITLE 0,--i18n-ff33fa6a-26e6-48eb-be38-4a035fe15829
# MAGIC %md
# MAGIC **4.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_4_1(traffic_query)

# COMMAND ----------

# DBTITLE 0,--i18n-5560d8c5-5acb-477d-ab0c-c7403560cf25
# MAGIC %md
# MAGIC ### 5. クエリーテーブル上で結果が更新されているのを確認する (View results being updated in the query table)
# MAGIC   <strong>`active_users_by_traffic`</strong>からの結果を表示するためにSQLセルでクエリーを実行します

# COMMAND ----------

# MAGIC %sql
# MAGIC -- TODO

# COMMAND ----------

# DBTITLE 0,--i18n-2c5cd18b-39f8-40fc-9d3b-9d313034ec10
# MAGIC %md
# MAGIC **5.1: 作業結果の確認 (CHECK YOUR WORK)**
# MAGIC クエリーの結果はいずれ以下のような値になるはずです。
# MAGIC
# MAGIC |traffic_source|active_users|
# MAGIC |---|---|
# MAGIC |direct|438886|
# MAGIC |email|281525|
# MAGIC |facebook|956769|
# MAGIC |google|1781961|
# MAGIC |instagram|530050|
# MAGIC |youtube|253321|

# COMMAND ----------

# DBTITLE 0,--i18n-efd51cf5-f848-4440-9ab7-ebe2650922ae
# MAGIC %md
# MAGIC ### 6. 全てのアクティブなストリームをリストし、停止する (List and stop all active streams)
# MAGIC - SparkSessionを使い全てのアクティブストリームを取得します
# MAGIC - リストを順に探りそれぞれのクエリーを停止してください

# COMMAND ----------

# TODO

# COMMAND ----------

# DBTITLE 0,--i18n-3d8b9236-eb09-415a-976e-4098c513043c
# MAGIC %md
# MAGIC **6.1: 作業結果の確認 (CHECK YOUR WORK)**

# COMMAND ----------

DA.tests.validate_6_1(traffic_query)

# COMMAND ----------

# DBTITLE 0,--i18n-778b92a6-160a-4210-8e9d-c49ef0621fb7
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
