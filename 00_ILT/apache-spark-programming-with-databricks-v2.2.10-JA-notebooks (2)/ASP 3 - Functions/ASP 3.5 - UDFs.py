# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-6073baf8-0a6a-403b-9287-a7d32b63eda8
# MAGIC %md
# MAGIC # ユーザー定義関数 (User-Defined Functions)
# MAGIC
# MAGIC ##### 目的 (Objectives)
# MAGIC 1. 関数の定義
# MAGIC 1. UDFの作成と適用
# MAGIC 1. SQLで使用するUDFを適用
# MAGIC 1. Pythonのデコレーター構文を使ったUDFの作成と登録
# MAGIC 1. Pandasのベクトル化されたUDFの作成と適用
# MAGIC
# MAGIC ##### メソッド （Methods)
# MAGIC - <a href="https://docs.databricks.com/spark/latest/spark-sql/udf-python.html" target="_blank">UDFの登録(<strong>`spark.udf`</strong>)</a>: <strong>`register`</strong>
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.udf.html?highlight=udf#pyspark.sql.functions.udf" target="_blank">組み込み関数</a>: **`udf`**
# MAGIC - <a href="https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.functions.udf.html" target="_blank">Python UDFデコレータ</a>: **`@udf`**
# MAGIC - <a href="https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.functions.pandas_udf.html" target="_blank">Pandas UDFデコレータ</a>: **`@pandas_udf`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-8b417b0d-b543-4930-bfb7-14c358d5b077
# MAGIC %md
# MAGIC ### ユーザー定義関数 (User-Defined Function、UDF)
# MAGIC カスタマイズされた列変換の関数
# MAGIC
# MAGIC - Catalystオプティマイザでは最適化されない
# MAGIC - 関数はシリアライズされてエグゼキューターに送信される
# MAGIC - 行のデータはSparkのネイティブフォーマットからデシリアライズされてUDFに渡され、その結果はSparkのネイティブフォーマットにシリアアイズされる
# MAGIC - Python UDFでは、各ワーカーノードでエグゼキューターとPythonインタプリタの間でのプロセス間通信のオーバーヘッドが追加で発生する

# COMMAND ----------

# DBTITLE 0,--i18n-856c854b-c777-44e6-8f95-e73cd7821909
# MAGIC %md
# MAGIC このデモでは、販売データを使います。

# COMMAND ----------

sales_df = spark.read.format("delta").load(DA.paths.sales)
display(sales_df)

# COMMAND ----------

# DBTITLE 0,--i18n-f20fb6e6-f628-48b1-b808-d9ace8352199
# MAGIC %md
# MAGIC ### 関数の定義 (Define a function)
# MAGIC
# MAGIC <strong>`email`</strong>フィールドから最初の文字を取得する関数を(ドライバーで)定義します。

# COMMAND ----------

def first_letter_function(email):
    return email[0]

first_letter_function("annagray@kaufman.com")

# COMMAND ----------

# DBTITLE 0,--i18n-5f3a5cf5-2f99-41fb-82ab-9da773148758
# MAGIC %md
# MAGIC ### UDFの作成と適用 (Create and apply UDF)
# MAGIC この関数をUDFとして登録します。これにより関数はシリアライズされ、データフレームのレコードを変換することができるようにエグゼキューターに送信されます。

# COMMAND ----------

first_letter_udf = udf(first_letter_function)

# COMMAND ----------

# DBTITLE 0,--i18n-05ea1414-ab37-43a0-ad4a-69f64ae5b445
# MAGIC %md
# MAGIC <strong>`email`</strong>列にUDFを適用します。

# COMMAND ----------

from pyspark.sql.functions import col

display(sales_df.select(first_letter_udf(col("email"))))

# COMMAND ----------

# DBTITLE 0,--i18n-db44861a-9b5e-4ee7-8c40-9478da9a5a60
# MAGIC %md
# MAGIC ### SQLで使用するUDFを適用 (Register UDF to use in SQL)
# MAGIC UDFを<strong>`spark.udf.register`</strong>を使って登録することで、SQL内でも利用できるようになります。

# COMMAND ----------

sales_df.createOrReplaceTempView("sales")

first_letter_udf = spark.udf.register("sql_udf", first_letter_function)

# COMMAND ----------

# You can still apply the UDF from Python
display(sales_df.select(first_letter_udf(col("email"))))

# COMMAND ----------

# MAGIC %sql
# MAGIC -- You can now also apply the UDF from SQL
# MAGIC SELECT sql_udf(email) AS first_letter FROM sales

# COMMAND ----------

# DBTITLE 0,--i18n-0717df0b-3986-4f76-ac37-2ecbbf536e3a
# MAGIC %md
# MAGIC ### デコレーター構文の使用(Pythonのみ)　(Use Decorator Syntax (Python Only))
# MAGIC
# MAGIC この代わりに、<a href="https://realpython.com/primer-on-python-decorators/" target="_blank">Pythonのデコレーター構文</a>を使ってUDFの定義と登録をすることもできます。<strong>`@udf`</strong>デコレーターのパラメーターは、関数が返すColumnのデータ型です。
# MAGIC
# MAGIC Pythonのローカル関数を呼ぶことができなくなります(すなわち<strong>`first_letter_udf("annagray@kaufman.com")`</strong>が動かなくなります)。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_32.png" alt="Note"> この例ではPython3.5で導入された<a href="https://docs.python.org/3/library/typing.html" target="_blank">Python型ヒント</a>も使われています。この例では型ヒントは必須ではありませんが、開発者が関数を正しく使うためのドキュメントとして役立ちます。この例では、UDFが1度に1レコードずつ処理し、1つの<strong>`str`</strong>を引数として<strong>`str`</strong>を返すことがわかります。

# COMMAND ----------

# Our input/output is a string
@udf("string")
def first_letter_udf(email: str) -> str:
    return email[0]

# COMMAND ----------

# DBTITLE 0,--i18n-15b7d228-a4a9-4b29-8ef4-1254701ce583
# MAGIC %md
# MAGIC ここでデコレーターUDFを使ってみましょう。

# COMMAND ----------

from pyspark.sql.functions import col

sales_df = spark.read.format("delta").load(DA.paths.sales)
display(sales_df.select(first_letter_udf(col("email"))))

# COMMAND ----------

# DBTITLE 0,--i18n-e99e7e62-1bbd-446f-8a01-71d5e49fbb14
# MAGIC %md
# MAGIC ### Pandasのベクトル化されたUDF (Pandas/Vectorized UDFs)
# MAGIC
# MAGIC Pandas UDFは、UDFの効率を向上させるために利用することができます。Pandas UDFは計算処理を高速化するためにApache Arrowを使っています。
# MAGIC
# MAGIC * <a href="https://databricks.com/blog/2017/10/30/introducing-vectorized-udfs-for-pyspark.html" target="_blank">ブログ投稿</a>
# MAGIC * <a href="https://spark.apache.org/docs/latest/api/python/user_guide/sql/arrow_pandas.html?highlight=arrow" target="_blank">ドキュメント</a>
# MAGIC
# MAGIC <img src="https://databricks.com/wp-content/uploads/2017/10/image1-4.png" alt="Benchmark" width ="500" height="1500">
# MAGIC
# MAGIC ユーザー定義関数は以下を利用して動作します: 
# MAGIC * <a href="https://arrow.apache.org/" target="_blank">Apache Arrow</a>は、 Sparkで使われるオンメモリの列指向データフォーマットで、JVMとPythonの間のシリアライズ/デシリアライズの処理時間をほぼ0にすることでデータ転送を効率化します。
# MAGIC * 関数内ではPandasとして動作し、PandasのインスタンスやAPIが使われます
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_warn_32.png" alt="Warning"> Spark 3.0時点ではPandas UDFを定義する際は**常に**Pythonの型ヒントを使うべきです。

# COMMAND ----------

import pandas as pd
from pyspark.sql.functions import pandas_udf

# We have a string input/output
@pandas_udf("string")
def vectorized_udf(email: pd.Series) -> pd.Series:
    return email.str[0]

# Alternatively
# def vectorized_udf(email: pd.Series) -> pd.Series:
#     return email.str[0]
# vectorized_udf = pandas_udf(vectorized_udf, "string")

# COMMAND ----------

display(sales_df.select(vectorized_udf(col("email"))))

# COMMAND ----------

# DBTITLE 0,--i18n-76f8656d-cd35-4fdd-9a1e-44e4eb7df462
# MAGIC %md
# MAGIC Pandas UDFも、SQLの中で使えるように登録することができます。

# COMMAND ----------

spark.udf.register("sql_vectorized_udf", vectorized_udf)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Use the Pandas UDF from SQL
# MAGIC SELECT sql_vectorized_udf(email) AS firstLetter FROM sales

# COMMAND ----------

# DBTITLE 0,--i18n-8414766d-ccbd-4a83-8883-f3dee4858435
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
