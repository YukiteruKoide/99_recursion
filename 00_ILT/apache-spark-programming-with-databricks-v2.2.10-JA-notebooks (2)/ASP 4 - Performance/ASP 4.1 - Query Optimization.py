# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-3b413d14-1b92-4b70-92de-f7a952f39082
# MAGIC %md
# MAGIC # クエリーの最適化 (Query Optimization)
# MAGIC
# MAGIC いくつかの例についてクエリープランと最適化を探求します。述語のプッシュダウンがされるケースとされないケースの論理的な最適化とexplainについても学びます。
# MAGIC
# MAGIC ##### 目的 (Objectives)
# MAGIC 1. 論理的な最適化
# MAGIC 1. 述語のプッシュダウン
# MAGIC 1. 述語のプッシュダウンがされないケース
# MAGIC
# MAGIC ##### メソッド (Methods)
# MAGIC - <a href="https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.DataFrame.explain.html#pyspark.sql.DataFrame.explain" target="_blank">DataFrame</a>: **`explain`**

# COMMAND ----------

# DBTITLE 0,--i18n-736d5858-6b37-4f1a-8a5a-f7f8f9c7d9e5
# MAGIC %md
# MAGIC セットアップのためのセルを実行し、その後<strong>`df`</strong>変数に入れられた最初のデータフレームを作りましょう。このデータフレームを表示するとイベントデータが見られるはずです。

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

df = spark.read.format("delta").load(DA.paths.events)
display(df)

# COMMAND ----------

# DBTITLE 0,--i18n-8da8aff9-5ffc-45a0-b0f7-4b2c04cae2c4
# MAGIC %md
# MAGIC ### 論理的な最適化 (Logical Optimization)
# MAGIC
# MAGIC <strong>`explain(..)`</strong>により、explainのモードごとに異なる形式で、クエリープランが出力されます。次の論理的プランと物理的プランを比較してみましょう。Catalystが複数の<strong>`filter`</strong>トランスフォーメーションをどう扱うかに注目してください。

# COMMAND ----------

from pyspark.sql.functions import col

limit_events_df = (df
                   .filter(col("event_name") != "reviews")
                   .filter(col("event_name") != "checkout")
                   .filter(col("event_name") != "register")
                   .filter(col("event_name") != "email_coupon")
                   .filter(col("event_name") != "cc_info")
                   .filter(col("event_name") != "delivery")
                   .filter(col("event_name") != "shipping_info")
                   .filter(col("event_name") != "press")
                  )

limit_events_df.explain(True)

# COMMAND ----------

# DBTITLE 0,--i18n-4ff48d99-e6a1-4061-baa6-376c2627f759
# MAGIC %md
# MAGIC もちろん、自分で最初から1つの<strong>`filter`</strong>条件を使ってクエリーを書くことはできました。上のクエリープランと、下のクエリープランを比べてみましょう。

# COMMAND ----------

better_df = (df
             .filter((col("event_name").isNotNull()) &
                     (col("event_name") != "reviews") &
                     (col("event_name") != "checkout") &
                     (col("event_name") != "register") &
                     (col("event_name") != "email_coupon") &
                     (col("event_name") != "cc_info") &
                     (col("event_name") != "delivery") &
                     (col("event_name") != "shipping_info") &
                     (col("event_name") != "press"))
            )

better_df.explain(True)

# COMMAND ----------

# DBTITLE 0,--i18n-4bdbe370-c354-4635-8177-2902c501c34a
# MAGIC %md
# MAGIC 以下のように長く複雑なフィルター条件で実は冗長なことに気づかないようなクエリーをわざと書くことはもちろんないでしょう。では、Catalystがこのクエリーをどう扱うか見てみましょう。

# COMMAND ----------

stupid_df = (df
             .filter(col("event_name") != "finalize")
             .filter(col("event_name") != "finalize")
             .filter(col("event_name") != "finalize")
             .filter(col("event_name") != "finalize")
             .filter(col("event_name") != "finalize")
            )

stupid_df.explain(True)

# COMMAND ----------

# DBTITLE 0,--i18n-7a6ba89a-fad6-4c4f-89b2-b4f0b1e43502
# MAGIC %md
# MAGIC ### キャッシング (Caching)
# MAGIC
# MAGIC デフォルトで、データフレームのデータは、クエリーのデータ処理がされている間しかSparkクラスター上に存在しません。クエリーの後に自動的にクラスター上に保持されることはありません。（Sparkはデータ処理のエンジンでありデータストレージのシステムではないので。) **`cache`** メソッドを実行することにより、Sparkに対してデータフレームを保持するように明示的にリクエストすることができます。
# MAGIC
# MAGIC もしデータフレームをキャッシュした後、それ以上必要なくなったら<strong>`unpersist`</strong>を実行することにより常に明示的にそれをキャッシュから削除すべきです。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_best_32.png" alt="Best Practice"> データフレームをキャッシュした方が良いのは、同じデータフレームを複数回使うのが確かであると考えられる場合であり、例えば以下のようなケースです：
# MAGIC
# MAGIC - 探索的なデータ分析
# MAGIC - 機械学習モデルのトレーニング
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_warn_32.png" alt="Warning"> これらのユースケース以外では、データフレームをキャッシュ**すべきではありません**。アプリケーションの性能を *劣化* させてしまうことがあるからです。
# MAGIC
# MAGIC - 別のタスクの実行に使えるリソースがキャッシングにより消費される
# MAGIC - 次の例で見られるように、キャッシングがクエリーの最適化を妨げることがある

# COMMAND ----------

# DBTITLE 0,--i18n-56f89c15-176f-4fde-8114-b5d6f0e5a240
# MAGIC %md
# MAGIC ### 述語のプッシュダウン (Predicate Pushdown)
# MAGIC
# MAGIC 以下のJDBCソースからの読み取りの例では、Catalystが<strong>述語のプッシュダウン</strong>での処理を決定しています。
# MAGIC 以下のJDBCソースからの読み取りの例では、Catalystが**述語のプッシュダウン**での処理を決定しています。

# COMMAND ----------

# MAGIC %scala
# MAGIC // Ensure that the driver class is loaded
# MAGIC Class.forName("org.postgresql.Driver")

# COMMAND ----------

jdbc_url = "jdbc:postgresql://server1.training.databricks.com/training"

# Username and Password w/read-only rights
conn_properties = {
    "user" : "training",
    "password" : "training"
}

pp_df = (spark
         .read
         .jdbc(url=jdbc_url,                 # the JDBC URL
               table="training.people_1m",   # the name of the table
               column="id",                  # the name of a column of an integral type that will be used for partitioning
               lowerBound=1,                 # the minimum value of columnName used to decide partition stride
               upperBound=1000000,           # the maximum value of columnName used to decide partition stride
               numPartitions=8,              # the number of partitions/connections
               properties=conn_properties    # the connection properties
              )
         .filter(col("gender") == "M")   # Filter the data by gender
        )

pp_df.explain(True)

# COMMAND ----------

# DBTITLE 0,--i18n-3b46d1d1-d9c9-4b44-90b6-099c6020f56e
# MAGIC %md
# MAGIC **Filter**がないことと、**Scan**に**PushedFilters**があることに注目してください。フィルター操作がデータベースに送られ、マッチしたレコードがSparkに返されます。これによりSparkが取り込まなければならないデータ量が大幅に削減されます。

# COMMAND ----------

# DBTITLE 0,--i18n-5dc0fe21-d96b-4246-9e79-f5a94c06c38b
# MAGIC %md
# MAGIC ### 述語のプッシュダウンがされないケース (No Predicate Pushdown)
# MAGIC
# MAGIC これに対して、フィルタリングの前にデータをキャッシュすると述語のプッシュダウンが使われることがなくなります。

# COMMAND ----------

cached_df = (spark
            .read
            .jdbc(url=jdbc_url,
                  table="training.people_1m",
                  column="id",
                  lowerBound=1,
                  upperBound=1000000,
                  numPartitions=8,
                  properties=conn_properties
                 )
            )

cached_df.cache()
filtered_df = cached_df.filter(col("gender") == "M")

filtered_df.explain(True)

# COMMAND ----------

# DBTITLE 0,--i18n-1a5e05ae-b422-4997-8db9-6f1f6ce7fc73
# MAGIC %md
# MAGIC 前の例で見た**Scan**(JDBC読み込み)に加え、**InMemoryTableScan**とそれに続く**Filter**をクエリープランに見ることになります。
# MAGIC
# MAGIC これは、Sparkはデータベースからデータを全て読み込みキャッシュし、キャッシュにあるものをスキャンしてフィルター条件に合うレコードを見つけなければならないことを意味します。

# COMMAND ----------

# DBTITLE 0,--i18n-59b7959a-70e0-4632-ad32-96a5dcdcde7b
# MAGIC %md
# MAGIC 使い終わったらきれいに削除することをお忘れなく！

# COMMAND ----------

cached_df.unpersist()

# COMMAND ----------

# DBTITLE 0,--i18n-f17ee199-dec9-4b05-89ed-da664e4d2ac3
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
