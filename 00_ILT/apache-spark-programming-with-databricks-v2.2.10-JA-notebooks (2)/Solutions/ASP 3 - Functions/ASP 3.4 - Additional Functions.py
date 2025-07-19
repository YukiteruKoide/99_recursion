# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-c8b680c1-52ff-46a1-95a8-017dd1faf468
# MAGIC %md
# MAGIC # その他の関数 (Additional Functions)
# MAGIC
# MAGIC ##### 目的 (Objectives)
# MAGIC 1. 組み込み関数を適用して新しい列にデータを生成する
# MAGIC 1. データフレームのNA関数を適用してnull値を扱う
# MAGIC 1. データフレームを結合する
# MAGIC
# MAGIC ##### メソッド （Methods)
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.join.html#pyspark.sql.DataFrame.join" target="_blank">DataFrame Methods </a>: **`join`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameNaFunctions.html#pyspark.sql.DataFrameNaFunctions" target="_blank">DataFrameNaFunctions</a>: **`fill`**, **`drop`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html" target="_blank">Built-In Functions</a>:
# MAGIC   - 集約 (Aggregate): **`collect_set`**
# MAGIC   - コレクション (Collection): **`explode`**
# MAGIC   - 集約以外やその他 (Non-aggregate and miscellaneous): **`col`**, **`lit`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

sales_df = spark.read.format("delta").load(DA.paths.sales)
display(sales_df)

# COMMAND ----------

# DBTITLE 0,--i18n-0fc5aedb-0dcd-4ce5-affb-742c6f476b4d
# MAGIC %md
# MAGIC ### 集約以外やその他の関数 (Non-aggregate and Miscellaneous Functions)
# MAGIC これらは集約以外やその他の組み込み関数のいくつかのものです。
# MAGIC
# MAGIC | メソッド | 説明 |
# MAGIC | --- | --- |
# MAGIC | col / column | 与えられた列名に基づいてColumnを返します |
# MAGIC | lit | リテラル値からなるColumnを作成します |
# MAGIC | isnull | 列がnullの場合trueを返します |
# MAGIC | rand | [0.0, 1.0)の区間で均一で独立同分布なランダムな値の列を生成します |

# COMMAND ----------

# DBTITLE 0,--i18n-36663576-e486-4760-9b82-988bedeea35a
# MAGIC %md
# MAGIC <strong>`col`</strong>関数を使って特定の列を選択できます。

# COMMAND ----------

gmail_accounts = sales_df.filter(col("email").endswith("gmail.com"))

display(gmail_accounts)

# COMMAND ----------

# DBTITLE 0,--i18n-a503922e-7844-4001-8748-28d229a9a559
# MAGIC %md
# MAGIC <strong>`lit`</strong>は値から列を作るのに使うことができ、列の追加に役立ちます。

# COMMAND ----------

display(gmail_accounts.select("email", lit(True).alias("gmail user")))

# COMMAND ----------

# DBTITLE 0,--i18n-2b3829c9-d241-46df-9d6d-823fa84ba889
# MAGIC %md
# MAGIC ### DataFrameNaFunctions
# MAGIC <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameNaFunctions.html#pyspark.sql.DataFrameNaFunctions" target="_blank">DataFrameNaFunctions</a>はデータフレームのサブモジュールで、null値を扱うメソッドを備えています。データフレームのna属性にアクセスすることでDataFrameNaFunctionsのインスタンスを取得できます。
# MAGIC
# MAGIC | メソッド | 説明 |
# MAGIC | --- | --- |
# MAGIC | drop | null値が1つでもある(any)、全てnull値(all)、あるいは特定の数以上null値がある行を除いた新たなデータフレームを返す。オプションで特定の列のサブセットだけを考慮することも可能 |
# MAGIC | fill | null値を指定した値で置換する。オプションで特定の列のサブセットを指定することも可能 |
# MAGIC | replace | 値を別の値で置換した新しいデータフレームを返す。オプションで特定の列のサブセットを指定することも可能 |

# COMMAND ----------

# DBTITLE 0,--i18n-e4a09833-ad6b-4e7b-b782-e832fd8752a8
# MAGIC %md
# MAGIC 以下でnull/NA値の行を削除する前後の行数を確認できます。

# COMMAND ----------

print(sales_df.count())
print(sales_df.na.drop().count())

# COMMAND ----------

# DBTITLE 0,--i18n-76375049-bcf6-40f3-95e6-cdf8721a2b5e
# MAGIC %md
# MAGIC 行数が同じなので、nullの列がないことがわかります。itemsの1レコードを複数行にして（explode)、items.couponのような列でnullのものを見つける必要があります。

# COMMAND ----------

sales_exploded_df = sales_df.withColumn("items", explode(col("items")))
display(sales_exploded_df.select("items.coupon"))
print(sales_exploded_df.select("items.coupon").count())
print(sales_exploded_df.select("items.coupon").na.drop().count())

# COMMAND ----------

# DBTITLE 0,--i18n-e97ff3e5-0c2f-40c4-b73c-a6b558264191
# MAGIC %md
# MAGIC <strong>`na.fill`</strong>を使ってクーポンコードが無いところを補完することができます。

# COMMAND ----------

display(sales_exploded_df.select("items.coupon").na.fill("NO COUPON"))

# COMMAND ----------

# DBTITLE 0,--i18n-a61ddd73-4269-47f4-90ec-65035cdd2261
# MAGIC %md
# MAGIC ### データフレームの結合 (Joining DataFrames)
# MAGIC データフレームの<a href="https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.DataFrame.join.html?highlight=join#pyspark.sql.DataFrame.join" target="_blank"><strong>`join`</strong></a>メソッドにより、与えられた結合条件に基づいて2つのデータフレームを結合することができます。
# MAGIC
# MAGIC いくつかの異なるタイプのjoinがサポートされています:
# MAGIC
# MAGIC "name"という共通の列の値が等しい場合に内部結合(inner join)する(つまり、等結合)<br/>
# MAGIC **`df1.join(df2, "name")`**
# MAGIC
# MAGIC "name"と"age"という共通の列の値が等しい場合に内部結合する<br/>
# MAGIC **`df1.join(df2, ["name", "age"])`**
# MAGIC
# MAGIC "name"という共通の列の値が等しい場合に完全外部結合（Full outer join)する<br/>
# MAGIC **`df1.join(df2, "name", "outer")`**
# MAGIC
# MAGIC 明示的な列の等式に基づいて左外部結合(Left outer join)する<br/>
# MAGIC **`df1.join(df2, df1["customer_name"] == df2["account_name"], "left_outer")`**

# COMMAND ----------

# DBTITLE 0,--i18n-9e8fb941-044c-4640-8fad-9278a8c26a84
# MAGIC %md
# MAGIC 上で得られたgmail_accountsと結合するためにユーザーデータを読み込みます。

# COMMAND ----------

users_df = spark.read.format("delta").load(DA.paths.users)
display(users_df)

# COMMAND ----------

joined_df = gmail_accounts.join(other=users_df, on='email', how = "inner")
display(joined_df)

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
