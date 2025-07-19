# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="77c31689-d17b-4d25-b97b-53e046c50b10"/>
# MAGIC
# MAGIC # Scaling Pandas with Spark
# MAGIC
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) このレッスンでは<br>
# MAGIC
# MAGIC - pandas API on Spark APIとpandas APIの類似性のデモを実施する
# MAGIC - Spark上のpandas APIとPySparkとの間で、DataFrameにおける操作構文の違いを理解する

# COMMAND ----------

# MAGIC %md <i18n value="8fad101f-86e7-4d33-9792-83cd3c87c23e"/>
# MAGIC
# MAGIC クラウドコンピューティングの授業で、大規模データの分散処理を管理するオープンソースのデータ処理エンジンである[Apache Spark](https://spark.apache.org/)のことを思い出してください。
# MAGIC
# MAGIC このコースでは、データ解析のための優れたライブラリであるPandasを使用してきましたが、これは1台のマシン上でしか動作しないため、分散処理には向いていません。幸い、Pandas API on Sparkを使えば、従来のPandasと同じようにSparkを利用することができます。
# MAGIC
# MAGIC pandas API on Sparkプロジェクトは、Apache Sparkの上にpandas DataFrame APIを実装することで、データサイエンティストがビッグデータを扱う際の生産性を向上させるものです。使い慣れたAPIで2つのエコシステムを統合することで、pandas API on Sparkは小規模データと大規模データの間のシームレスな移行を提供します。
# MAGIC
# MAGIC Spark上でのPandas構文の使用に関する詳細は、こちらの<a href="https://databricks.com/blog/2021/10/04/pandas-api-on-upcoming-apache-spark-3-2.html" target="_blank">blog post</a>を参照してください。

# COMMAND ----------

# MAGIC %md <i18n value="9112c122-6e72-4fe2-85f3-c1786b8d0620"/>
# MAGIC
# MAGIC <div style="img align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://files.training.databricks.com/images/301/31gb.png" width="900"/>
# MAGIC </div>
# MAGIC
# MAGIC <div style="img align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://files.training.databricks.com/images/301/95gb.png" width="900"/>
# MAGIC </div>
# MAGIC
# MAGIC **Pandas** DataFramesはミュータブルで、eagerilyに評価され、行の順序を維持します。単一マシンに限定され、a)に示すようにデータセットが小さい場合に非常に高い性能を発揮します。
# MAGIC
# MAGIC **Spark** DataFrameは、分散型、遅延評価型、不変型であり、行順を保持しない。b)とc)に示すように、大規模な処理を行う際に非常に高い性能を発揮します。
# MAGIC
# MAGIC **pandas API on Spark** は、pandasのAPIとSparkの性能の利点を組み合わせたものです。しかし、Sparkでネイティブにソリューションを実装するほど高速ではありません。その理由を以下に説明します。

# COMMAND ----------

# MAGIC %md <i18n value="812c6711-72b9-464c-86f8-66b93dd7e0d2"/>
# MAGIC
# MAGIC ## 内部フレーム(InternalFrame)
# MAGIC
# MAGIC InternalFrameは、現在のSpark DataFrameと内部のイミュータブルなメタデータを保持します。
# MAGIC
# MAGIC pandas API on Sparkのカラム名からSparkのカラム名へのマッピングや、pandas API on Sparkのインデックス名からSparkのカラム名へのマッピングを管理します。
# MAGIC
# MAGIC ユーザーが何らかのAPIを呼び出した場合、pandas API on Spark DataFrameはInternalFrame内のSpark DataFrameとメタデータを更新します。現在のInternalFrameを新しい状態で作成またはコピーし、新しいpandas API on Spark DataFrameを返します。
# MAGIC
# MAGIC <div style="img align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://files.training.databricks.com/images/301/InternalFramePs.png" width="900"/>
# MAGIC </div>

# COMMAND ----------

# MAGIC %md <i18n value="118a32b5-df6e-4679-884c-8077c2d6aa09"/>
# MAGIC
# MAGIC ### データセットの読み込み（Read in the dataset）
# MAGIC
# MAGIC * PySpark
# MAGIC * pandas
# MAGIC * pandas API on Spark

# COMMAND ----------

# MAGIC %run "./Includes/Classroom-Setup"

# COMMAND ----------

# MAGIC %md <i18n value="a5801cbc-ab2a-444a-ad8a-a96791cf0596"/>
# MAGIC
# MAGIC pandasでCSVファイルからデータを読み込むのと同じように、sparkでもファイルからデータを読み込むことができます。

# COMMAND ----------

spark_df = spark.read.csv(f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv", header="true", inferSchema="true", multiLine="true", escape='"')
display(spark_df)

# COMMAND ----------

# MAGIC %md <i18n value="8f40703f-c097-4532-9bae-d56b07dd6907"/>
# MAGIC
# MAGIC pandasでCSVを読み込む

# COMMAND ----------

import pandas as pd

pandas_df = pd.read_csv(f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv".replace("dbfs:", "/dbfs"))
pandas_df.head()

# COMMAND ----------

# MAGIC %md <i18n value="3092efbf-6f55-45ca-9ec7-4a45250d55f5"/>
# MAGIC
# MAGIC Sparkのpandas APIを使ってCSVを読み込みます。pandas API on Sparkでは、pandasのようにインデックスカラムを生成してくれることがわかります。

# COMMAND ----------

import pyspark.pandas as ps

df = ps.read_csv(f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv", inferSchema="true", multiLine="true", escape='"')
df.head()

# COMMAND ----------

# MAGIC %md <i18n value="ec4b222c-7a5f-49d7-a913-bc5a1c6c269f"/>
# MAGIC
# MAGIC ### <a href="https://koalas.readthedocs.io/en/latest/user_guide/options.html#default-index-type" target="_blank">Index Types</a>
# MAGIC
# MAGIC ![](https://files.training.databricks.com/images/301/koalas_index.png)

# COMMAND ----------

ps.set_option("compute.default_index_type", "distributed-sequence")
df_dist_sequence = ps.read_csv(f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv", inferSchema="true", multiLine="true", escape='"')
df_dist_sequence.head()

# COMMAND ----------

# MAGIC %md <i18n value="2fd38d18-35ae-4971-825f-a6fd5cbc7b64"/>
# MAGIC
# MAGIC ### Spark DataFrameと pandas API on Sparkへの相互変換（Converting to pandas API on Spark DataFrame to/from Spark DataFrame）

# COMMAND ----------

# MAGIC %md <i18n value="43331470-511a-4975-b075-3cf006da4e23"/>
# MAGIC
# MAGIC PySparkのDataFrameからpandas API on SparkのDataFrameを作成する

# COMMAND ----------

df = ps.DataFrame(spark_df)
display(df)

# COMMAND ----------

# MAGIC %md <i18n value="9579fb05-e9a2-4774-a4ad-d1988e0249ea"/>
# MAGIC
# MAGIC PySparkのDataFrameからSparkのDataFrameにpandas APIを作成する別の方法

# COMMAND ----------

df = spark_df.to_pandas_on_spark()
display(df)

# COMMAND ----------

# MAGIC %md <i18n value="22d68896-91dc-432b-afd8-94bdfb962c09"/>
# MAGIC
# MAGIC pandas API on Spark DataFrameからSpark DataFrameに移行する

# COMMAND ----------

display(df.to_spark())

# COMMAND ----------

# MAGIC %md <i18n value="523332ab-1890-411e-a830-f81476dc0aba"/>
# MAGIC
# MAGIC ###値の集計（Value Counts）

# COMMAND ----------

# MAGIC %md <i18n value="d76a4309-2ad4-4ba9-9948-96d3f1dab224"/>
# MAGIC
# MAGIC PySparkで異なるプロパティタイプの値カウントを取得する

# COMMAND ----------

display(spark_df.groupby("property_type").count().orderBy("count", ascending=False))

# COMMAND ----------

# MAGIC %md <i18n value="63d5ecb1-8d6f-47fd-882f-8dd9d13d9748"/>
# MAGIC
# MAGIC pandas API on Sparkで異なるプロパティタイプの値カウントを取得する

# COMMAND ----------

df["property_type"].value_counts()

# COMMAND ----------

# MAGIC %md <i18n value="cb1c7961-4a96-4c18-9e0b-b9bbd35d5096"/>
# MAGIC
# MAGIC ### 可視化（Visualizations）
# MAGIC
# MAGIC 可視化の種類に応じて、pandas API on Sparkはプロットの実行方法を最適化しています
# MAGIC <br><br>
# MAGIC
# MAGIC ![](https://files.training.databricks.com/images/301/ps_plotting.png)

# COMMAND ----------

df["bedrooms"].hist(bins=20)

# COMMAND ----------

# MAGIC %md <i18n value="f449a17a-d308-4729-9696-4f6d804168f6"/>
# MAGIC
# MAGIC ### Spark DataFrame上でのpandas APIを使ったSQL（SQL on pandas API on Spark DataFrames）

# COMMAND ----------

ps.sql("SELECT distinct(property_type) FROM {df}", df=df)

# COMMAND ----------

# MAGIC %md <i18n value="b9935020-093d-44f1-b84d-95b676d0d7cc"/>
# MAGIC
# MAGIC ### 興味ある事（Interesting Facts）
# MAGIC
# MAGIC * pandas API on Sparkでは、Delta Tablesからの読み込みと、ファイルのディレクトリでの読み込みが可能
# MAGIC * pandas API on Spark の DF で apply を使用し、その DF が <1000 (デフォルト) の場合、pandas API on Spark は pandas をショートカットとして使用　- これは **`compute.shortcut_limit`** で調整することも可能
# MAGIC * 棒グラフを作成する場合、上位n行のみが使用される - これは **`plotting.max_rows`** で調整可能
# MAGIC * どのように **`.apply`** 
# MAGIC <a href="https://koalas.readthedocs.io/en/latest/reference/api/databricks.koalas.DataFrame.apply.html#databricks.koalas.DataFrame.apply" target="_blank">docs</a> と pandas UDF のような戻り値のヒントを使用するか
# MAGIC * どのように実行計画やSpark DF上でのpandas APIのキャッシュ（直感的にはわからないと思います）をどう確認するか
# MAGIC * Koalas は有袋類で最高速度は時速30キロ（時速20マイル）である。

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
