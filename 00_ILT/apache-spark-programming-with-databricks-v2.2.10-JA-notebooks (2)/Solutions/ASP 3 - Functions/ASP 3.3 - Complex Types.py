# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-0a3c3f90-d80f-4eb9-8f94-930aba6cadd1
# MAGIC %md
# MAGIC # 複雑タイプ (Complex Types)
# MAGIC
# MAGIC コレクションと文字列を操作するための組み込み関数を探索します。
# MAGIC
# MAGIC ##### 目的 (Objectives)
# MAGIC 1. コレクション関数を配列の処理に適用する
# MAGIC 1. データフレームをユニオンする
# MAGIC
# MAGIC ##### メソッド (Methods)
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrame</a>:**`union`**, **`unionByName`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html" target="_blank">Built-In Functions</a>:
# MAGIC   - 集約: **`collect_set`**
# MAGIC   - コレクション: **`array_contains`** 、 **`element_at`** 、 **`explode`**
# MAGIC   - 文字列: **`split`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df = spark.read.format("delta").load(DA.paths.sales)

display(df)

# COMMAND ----------

# You will need this DataFrame for a later exercise
details_df = (df
              .withColumn("items", explode("items"))
              .select("email", "items.item_name")
              .withColumn("details", split(col("item_name"), " "))
             )
display(details_df)

# COMMAND ----------

# DBTITLE 0,--i18n-ac5b4610-6efc-4e5a-acd8-90933422a950
# MAGIC %md
# MAGIC ### String 関数 (String Functions)
# MAGIC 文字列の操作に使用できる組み込み関数の一部を次に示します。
# MAGIC
# MAGIC | メソッド | 説明|
# MAGIC | --- | --- |
# MAGIC | translate | src 内の文字をreplaceStringの文字で変換する | 
# MAGIC | regexp_replace | regexp に一致する指定した文字列値の部分文字列をすべてrep に置き換える | 
# MAGIC | regexp_extract | 指定した文字列の列から、Java 正規表現でマッチした特定のグループを抽出する|
# MAGIC | ltrim | 指定した文字列の列から先頭の空白文字を削除する|
# MAGIC | lower | 文字列の列を小文字に変換する|
# MAGIC | split | 指定したパターンでstrを分割する|

# COMMAND ----------

# DBTITLE 0,--i18n-3f18adec-4808-4071-93bb-2ec5964512f8
# MAGIC %md
# MAGIC たとえば、 **`email`** 列を解析することにします。 **`split`** 関数を使って **`email`** を分割します。

# COMMAND ----------

from pyspark.sql.functions import split

# COMMAND ----------

display(df.select(split(df.email, '@', 0).alias('email_handle')))

# COMMAND ----------

# DBTITLE 0,--i18n-ab537316-5715-4c11-9df8-a36f70fa9b78
# MAGIC %md
# MAGIC ### コレクション関数 (Collection Functions)
# MAGIC
# MAGIC 配列で使用できる組み込み関数の一部を次に示します。
# MAGIC
# MAGIC | メソッド | 説明|
# MAGIC | --- | --- |
# MAGIC | array_contains | 配列がNULL の場合はNULL、配列に指定値が含まれる場合はtrue、それ以外の場合はfalse を返します。|
# MAGIC | element_at | 指定したインデックスで配列の要素を返します。配列要素には、**1**で始まる番号が付けられます。|
# MAGIC | explode | 指定した配列またはマップ列の要素ごとに新しい行を作成します。|
# MAGIC | collect_set | 重複要素を取り除いたオブジェクトの集合を返します。|

# COMMAND ----------

mattress_df = (details_df
               .filter(array_contains(col("details"), "Mattress"))
               .withColumn("size", element_at(col("details"), 2)))
display(mattress_df)

# COMMAND ----------

# DBTITLE 0,--i18n-f4da035e-b5c1-462d-bb28-b393614dbf54
# MAGIC %md
# MAGIC ### 集約関数 (Aggregate Functions)
# MAGIC
# MAGIC ここでは、通常はGroupedData から配列を作成するために使用できる組み込み集約関数の一部を示します。
# MAGIC
# MAGIC | メソッド | 説明|
# MAGIC | --- | --- |
# MAGIC | collect_list | グループ内のすべての値からなる配列を返します。|
# MAGIC | collect_set | グループ内のすべての一意の値で構成される配列を返します。|

# COMMAND ----------

# DBTITLE 0,--i18n-b0cd9063-d89e-47b6-9848-3da8c7e222f0
# MAGIC %md
# MAGIC 各メールアドレスで注文したマットレスのサイズを見たかったとしましょう。このために、 **`collect_set`** 関数を使用できます。

# COMMAND ----------

size_df = mattress_df.groupBy("email").agg(collect_set("size").alias("size options"))

display(size_df)

# COMMAND ----------

# DBTITLE 0,--i18n-497a00ae-83d5-4460-883f-66ebc8598011
# MAGIC %md
# MAGIC ##UnionとunionByName
# MAGIC <img src="https://files.training.databricks.com/images/icon_warn_32.png" alt="Warning"> The DataFrame <a href="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.DataFrame.union.html" target="_blank">**`union`**</a> メソッドは、標準SQLのように、列の位置によってデータをユニオンします。2 つのDataFrame のスキーマが、列の順序も含めてまったく同じである場合にのみ使用してください。これに対して、DataFrame <a href="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.DataFrame.unionByName.html" target="_blank">**`unionByName`**</a> メソッドは、列の名前によってデータをユニオンします。 これは、SQLのUNION ALLと同じです。 どちらも重複を削除しません。 
# MAGIC
# MAGIC 以下は、2 つのDataFrameが **`union`** できるかスキーマを調べます。

# COMMAND ----------

mattress_df.schema==size_df.schema

# COMMAND ----------

# DBTITLE 0,--i18n-66158320-fd13-4577-b7cb-ad4a57578a40
# MAGIC %md
# MAGIC 単純な **`select`** ステートメントで生成したDataFrameには、 **`union`** を使用できます。

# COMMAND ----------

union_count = mattress_df.select("email").union(size_df.select("email")).count()

mattress_count = mattress_df.count()
size_count = size_df.count()

mattress_count + size_count == union_count

# COMMAND ----------

# DBTITLE 0,--i18n-bfc7136f-f5f9-4c6b-bcaa-2ec8ad759e20
# MAGIC %md
# MAGIC ### クラスルームで使ったリソースの削除 (Clean up classroom)
# MAGIC
# MAGIC
# MAGIC 最後に、クラスルームのクリーンアップを行います。

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
