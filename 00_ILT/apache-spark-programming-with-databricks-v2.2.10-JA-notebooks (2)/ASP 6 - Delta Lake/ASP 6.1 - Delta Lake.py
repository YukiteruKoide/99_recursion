# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-29c969ba-b703-4861-9466-dbf95b81176f
# MAGIC %md
# MAGIC # Delta Lake
# MAGIC
# MAGIC ##### 目的 (Objectives)
# MAGIC 1. Deltaテーブルの作成
# MAGIC 1. トランザクションログの理解
# MAGIC 1. Deltaテーブルからデータを読み込む
# MAGIC 1. Deltaテーブルのデータを更新
# MAGIC 1. タイムトラベルを使って以前のバージョンのテーブルにアクセス
# MAGIC 1. バキューム
# MAGIC
# MAGIC ##### ドキュメント (Documentation)
# MAGIC - <a href="https://docs.delta.io/latest/quick-start.html#create-a-table" target="_blank">Delta Table</a> 
# MAGIC - <a href="https://databricks.com/blog/2019/08/21/diving-into-delta-lake-unpacking-the-transaction-log.html" target="_blank">Transaction Log</a> 
# MAGIC - <a href="https://databricks.com/blog/2019/02/04/introducing-delta-time-travel-for-large-scale-data-lakes.html" target="_blank">Time Travel</a>

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-47af8ff4-2231-4e49-aefd-8832cf3bb995
# MAGIC %md
# MAGIC ### Deltaテーブルの作成 (Create a Delta Table)
# MAGIC はじめにParquetフォーマットのBedBricksイベントデータセットを読み込んでみましょう。

# COMMAND ----------

events_df = spark.read.format("parquet").load(f"{DA.paths.datasets}/ecommerce/events/events.parquet")
display(events_df)

# COMMAND ----------

# DBTITLE 0,--i18n-03fc4dbf-8242-4968-833e-47c9b405d455
# MAGIC %md
# MAGIC <strong>`delta_path`</strong>で指定されたディレクトリにDeltaフォーマットで出力してみましょう。

# COMMAND ----------

delta_path = f"{DA.paths.working_dir}/delta-events"
events_df.write.format("delta").mode("overwrite").save(delta_path)

# COMMAND ----------

# DBTITLE 0,--i18n-aea460aa-80cd-401a-b82f-add4452425c5
# MAGIC %md
# MAGIC メタストアのマネージドテーブルとしてDeltaフォーマットで出力します。

# COMMAND ----------

events_df.write.format("delta").mode("overwrite").saveAsTable("delta_events")

# COMMAND ----------

# DBTITLE 0,--i18n-48970b1e-8857-4675-9499-28ee9e438641
# MAGIC %md
# MAGIC 他のファイルフォーマットと同様にDeltaは、特定のカラムのユニークな値を使ってデータをストレージ上にパーティション分割することができます（Hiveパーティショニングとも呼ばれます)。
# MAGIC
# MAGIC 州(state)別にパーティション分割するために、<strong>`delta_path`</strong>ディレクトリにあるDeltaデータセットを上書き(**overwrite**)してみましょう。これにより州別のフィルター速度が向上します。

# COMMAND ----------

from pyspark.sql.functions import col

state_events_df = events_df.withColumn("state", col("geo.state"))

state_events_df.write.format("delta").mode("overwrite").partitionBy("state").option("overwriteSchema", "true").save(delta_path)

# COMMAND ----------

# DBTITLE 0,--i18n-246546ce-4fe0-48c8-b698-26f5e70b7b75
# MAGIC %md
# MAGIC ### トランザクションログの理解 (Understand the Transaction Log)
# MAGIC Deltaがそれぞれのディレクトリに異なる州のパーティションを保存しているかを見てみましょう。
# MAGIC
# MAGIC さらに、<strong>`_delta_log`</strong>という名前のディレクトリにトランザクションログが保存されるのも見ることができます。
# MAGIC
# MAGIC Delta Lakeのデータセットが出来た時に、そのトランザクションログも<strong>`_delta_log`</strong>というサブディレクトリに自動的に作成されます。

# COMMAND ----------

display(dbutils.fs.ls(delta_path))

# COMMAND ----------

# DBTITLE 0,--i18n-59dd5b49-90b4-49ad-bc4b-d88b9f1902c4
# MAGIC %md
# MAGIC そのテーブルに変化がある時、それらの変更は順番に不可分(atomic)なコミットとしてトランザクションログに記録されます。
# MAGIC
# MAGIC それぞれのコミットは00000000000000000000.jsonから始まるJSONファイルとして出力されます。
# MAGIC
# MAGIC それ以降のテーブルの変更は、数字の昇順で番号が振られたJSONファイルとして生成されます。
# MAGIC
# MAGIC <div style="img align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://user-images.githubusercontent.com/20408077/87174138-609fe600-c29c-11ea-90cc-84df0c1357f1.png" width="500"/>
# MAGIC </div>

# COMMAND ----------

display(dbutils.fs.ls(f"{delta_path}/_delta_log/"))

# COMMAND ----------

# DBTITLE 0,--i18n-07403490-e05e-4095-8168-9384ee6da385
# MAGIC %md
# MAGIC 次に、トランザクションログファイルを見てみましょう。
# MAGIC
# MAGIC
# MAGIC <a href="https://docs.databricks.com/delta/delta-utility.html" target="_blank">4つの列</a>はそれぞれ、テーブル作成というDeltaテーブルへの最初のコミットに関する異なる部分を表しています。
# MAGIC
# MAGIC - <strong>`add`</strong>列には、Dataframe全体および個々の列に関する統計情報が含まれています。
# MAGIC - <strong>`commitInfo`</strong>列には、操作が何であったか(WRITEかREADか)や誰が操作を実行したかに関する有用な情報が含まれています。
# MAGIC - <strong>`metaData`</strong>列には列スキーマに関する情報が含まれています。
# MAGIC - <strong>`protocol`</strong>のバージョンには、このDeltaテーブルへの書き込みや読み込みに必要な最小のDeltaのバージョンに関する情報が含まれています。

# COMMAND ----------

display(spark.read.json(f"{delta_path}/_delta_log/00000000000000000000.json"))

# COMMAND ----------

# DBTITLE 0,--i18n-84a54908-8e70-42e8-93fb-355da0b3314c
# MAGIC %md
# MAGIC これら2つのトランザクションログの1つの主要な違いは、JSONファイルのサイズで、前バージョンの7行と比較して206行を持ちます。
# MAGIC
# MAGIC なぜかを理解するために<strong>`commitInfo`</strong>列を見てみましょう。<strong>`operationParameters`</strong>セクションを見ると、<strong>`partitionBy`</strong>が<strong>`state`</strong>になっていることがわかります。さらに、3行めのaddセクションを見ると、<strong>`partitionValues`</strong>という新しいセクションが出来ていることがわかります。これまで見てきた通り、Deltaはパーティションを別々にメモリに格納していますが、これらのパーティションの情報を同じトランザクションログファイルに保存しています。

# COMMAND ----------

display(spark.read.json(f"{delta_path}/_delta_log/00000000000000000001.json"))

# COMMAND ----------

# DBTITLE 0,--i18n-3794c8e9-c286-454b-ab04-4214d103e0ae
# MAGIC %md
# MAGIC 最後に、stateパーティションの一つにあるファイルを見てみましょう。内部のファイルは _delta_log ディレクトリのパーティションコミット (file 01) に対応しています。

# COMMAND ----------

display(dbutils.fs.ls(f"{delta_path}/state=CA/"))

# COMMAND ----------

# DBTITLE 0,--i18n-b523d430-c025-409e-a32b-4001c92a582b
# MAGIC %md
# MAGIC ### Deltaテーブルからデータを読み込む (Read from your Delta table)

# COMMAND ----------

df = spark.read.format("delta").load(delta_path)
display(df)

# COMMAND ----------

# DBTITLE 0,--i18n-d99c45c5-c19a-4a80-885d-1fa07841a4e8
# MAGIC %md
# MAGIC ### Deltaテーブルのデータを更新 (Update your Delta Table)
# MAGIC
# MAGIC モバイル端末からのイベントの行をフィルタリングしてみましょう。

# COMMAND ----------

df_update = state_events_df.filter(col("device").isin(["Android", "iOS"]))
display(df_update)

# COMMAND ----------

df_update.write.format("delta").mode("overwrite").save(delta_path)

# COMMAND ----------

df = spark.read.format("delta").load(delta_path)
display(df)

# COMMAND ----------

# DBTITLE 0,--i18n-4974ded0-c507-45ab-9973-d9a6ede4a434
# MAGIC %md
# MAGIC 更新後のカリフォルニア州のパーティションにあるファイルを見てみましょう。このディレクトリにある異なるファイルは、異なるコミットに対応するDataframeのスナップショットであることを覚えておきましょう。

# COMMAND ----------

display(dbutils.fs.ls(f"{delta_path}/state=CA/"))

# COMMAND ----------

# DBTITLE 0,--i18n-a871e8d3-9a89-45b5-8f83-35fdf905b88e
# MAGIC %md
# MAGIC ### タイムトラベルを使って以前のバージョンのテーブルにアクセス (Access previous versions of table using Time Travel)

# COMMAND ----------

# DBTITLE 0,--i18n-db5de62b-fb0b-448a-922a-e6737fcd04c2
# MAGIC %md
# MAGIC なんと、全体のデータセットが必要だったことが判明しました！タイムトラベルを利用して以前のバージョンのDeltaテーブルにアクセスすることができます。バージョン履歴にアクセスするために以下の２つのセルを使ってください。Delta Lakeはデフォルトで30日間のバージョン履歴を保持しますが、必要に応じてDeltaはそれより長い期間のバージョン履歴を保持することもできます。

# COMMAND ----------

spark.sql("DROP TABLE IF EXISTS train_delta")
spark.sql(f"CREATE TABLE train_delta USING DELTA LOCATION '{delta_path}'")

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY train_delta

# COMMAND ----------

# DBTITLE 0,--i18n-8f796a3b-d9b5-4731-8177-18a1dd934adb
# MAGIC %md
# MAGIC <strong>`versionAsOf`</strong>オプションを使うことで以前のバージョンのDeltaテーブルに簡単にアクセスできます。

# COMMAND ----------

df = spark.read.format("delta").option("versionAsOf", 0).load(delta_path)
display(df)

# COMMAND ----------

# DBTITLE 0,--i18n-7492d08f-77c0-46dd-8347-289a2a992e03
# MAGIC %md
# MAGIC タイムスタンプを使うことでも、古いバージョンにアクセスすることができます。
# MAGIC
# MAGIC タイムスタンプの文字列をバージョン履歴の情報で置き換えてください。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_32.png"> ノート: 必要に応じて、時刻の情報無しの日付を使うこともできます。

# COMMAND ----------

# TODO

temp_df = spark.sql("DESCRIBE HISTORY train_delta").select("timestamp").orderBy(col("timestamp").asc())
time_stamp = temp_df.first()["timestamp"]

as_of_df = spark.read.format("delta").option("timestampAsOf", time_stamp).load(delta_path)
display(as_of_df)

# COMMAND ----------

# DBTITLE 0,--i18n-a10072d6-7351-46e6-a34b-100a1c2566f2
# MAGIC %md
# MAGIC ### バキューム (Vacuum)
# MAGIC
# MAGIC これでDeltaテーブルが完成したので、<strong>`VACUUM`</strong>を使ってディレクトリをクリーンアップしましょう。VACUUMは時間単位の保持期間を入力として受け付けます。

# COMMAND ----------

# DBTITLE 0,--i18n-a52c1e95-8122-4038-8cf1-2fc97afe4a3b
# MAGIC %md
# MAGIC このコードの実行は成功しないようです！デフォルトでは、最近のコミットを誤ってバキュームしてしまうのを防ぐために、Delta Lakeはユーザーに7日間または168時間未満の期間のバキュームを許可しません。一度バキュームされると、タイムトラベルで以前のコミットに戻ることはできず、直近のDeltaテーブルだけが保存されます。

# COMMAND ----------

# from delta.tables import *

# delta_table = DeltaTable.forPath(spark, delta_path)
# delta_table.vacuum(0)

# COMMAND ----------

# DBTITLE 0,--i18n-f69d8001-a93e-4dce-ae97-4e84ee31120a
# MAGIC %md
# MAGIC デフォルトの保持期間のチェックを回避するようにSparkに設定することでこの問題を回避することができます。

# COMMAND ----------

from delta.tables import *

spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")
delta_table = DeltaTable.forPath(spark, delta_path)
delta_table.vacuum(0)

# COMMAND ----------

# DBTITLE 0,--i18n-8f16824b-2cb5-4753-841e-d221fed27afc
# MAGIC %md
# MAGIC Deltaテーブルのファイルを見てみましょう。バキュームした後、ディレクトリには直近のDeltaテーブルコミットのパーティションのみが保持されています。

# COMMAND ----------

display(dbutils.fs.ls(delta_path + "/state=CA/"))

# COMMAND ----------

# DBTITLE 0,--i18n-ea8feef0-0ab1-4f62-9754-bc2183ded4f4
# MAGIC %md
# MAGIC バキューム処理でDeltaテーブルで参照されているファイルが削除されるため、過去のバージョンにアクセスできなくなりました。 
# MAGIC
# MAGIC 以下のコードはエラーが発生するはずです。
# MAGIC
# MAGIC コメントを外し、試してみてください。

# COMMAND ----------

# df = spark.read.format("delta").option("versionAsOf", 0).load(delta_path)
# display(df)

# COMMAND ----------

# DBTITLE 0,--i18n-12edf5ff-c28b-4b35-a7fe-2ec9efbdba72
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
