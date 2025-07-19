# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# Read in the dataset for the lab, along with all functions

from pyspark.sql.functions import *

df = spark.read.format("delta").load(DA.paths.sales)
display(df)

# COMMAND ----------

# DBTITLE 0,--i18n-08f7ee14-cd81-464f-962b-8a2101079235
# MAGIC %md
# MAGIC ### 1. 購買（purchases）からの詳細itemの抽出
# MAGIC - df **`items`** フィールドを分解し、その結果を既存の **`items`** フィールドに置き換えます。
# MAGIC - **`email`** と **`item.item_name`** のフィールドを選択します。
# MAGIC - **`item_name`** の単語を配列に分割し、"details" という列のエイリアス（alias）を付けます。
# MAGIC
# MAGIC 出来上がったDataFrameを **`details_df`** に代入します。

# COMMAND ----------

# TODO

from pyspark.sql.functions import *

details_df = (df
              .withColumn("items", explode("items"))
              .select("email", "items.item_name")
              .withColumn("details", split(col("item_name"), " "))
             )
display(details_df)

# COMMAND ----------

# Run this cell to check your work
assert details_df.count() == 235911

# COMMAND ----------

# DBTITLE 0,--i18n-6cdf4168-211f-445a-8338-069b70b4286b
# MAGIC %md
# MAGIC つまり、<strong>`details`<strong>カラムは、品質、サイズ、オブジェクトタイプを含む配列になったことがわかります。

# COMMAND ----------

# DBTITLE 0,--i18n-e419efc4-edd2-4cf2-a5be-896366a3d872
# MAGIC %md
# MAGIC ### 2. マットレスの購買時のサイズと品質オプションについて抽出します。
# MAGIC - **`details_df`** を、 **`details`** に "Mattress" が含まれるレコードでフィルタリングする。
# MAGIC - 2の位置の要素を取り出して **`size`** 列を追加する。
# MAGIC - 1位の要素を抽出して、 **`quality`** 列を追加する。
# MAGIC
# MAGIC 結果を **`mattress_df`** として保存します。

# COMMAND ----------

# TODO

mattress_df = (details_df
               .filter(array_contains(col("details"), "Mattress"))
               .withColumn("size", element_at(col("details"), 2))
               .withColumn("quality", element_at(col("details"), 1))
              )
display(mattress_df)

# COMMAND ----------

# Run this cell to check your work
assert mattress_df.count() == 208384

# COMMAND ----------

# DBTITLE 0,--i18n-927a03cd-6736-48a9-ace6-85b13cad0355
# MAGIC %md
# MAGIC 次に、枕の購入（pillow purchases）についても同じことを実施します。

# COMMAND ----------

# DBTITLE 0,--i18n-8307241a-65a3-4fc5-afa7-b272a201e602
# MAGIC %md
# MAGIC ### 3. 枕の購買時のサイズと品質オプションについて抽出します。
# MAGIC - **`details_df`** に "Pillow "が含まれるレコードをフィルタリングする。
# MAGIC - 1位の要素を抽出して **`size`** 列を追加する。
# MAGIC - 2の位置の要素を取り出して、 **`quality`** 列を追加する。
# MAGIC
# MAGIC マットレスと枕では、　**`size`** と **`quality`** の位置が入れ替わっていることに注意してください。
# MAGIC
# MAGIC 結果を **`pillow_df`** として保存します。

# COMMAND ----------

# TODO

pillow_df = (details_df
             .filter(array_contains(col("details"), "Pillow"))
             .withColumn("size", element_at(col("details"), 1))
             .withColumn("quality", element_at(col("details"), 2))
            )
display(pillow_df)

# COMMAND ----------

# Run this cell to check your work
assert pillow_df.count() == 27527

# COMMAND ----------

# DBTITLE 0,--i18n-7bd3677a-73a3-4d24-99c0-8facbcee7c82
# MAGIC %md
# MAGIC ### 4. マットレスと枕の日付を組み合わせてください（Combine data for mattress and pillows）
# MAGIC - **`mattress_df`** と **`pillow_df`** の列名による”Union”を実行する。
# MAGIC - **`details`** 列の削除
# MAGIC
# MAGIC 結果を **`union_df`** として保存します。

# COMMAND ----------

# TODO

union_df = mattress_df.unionByName(pillow_df).drop("details")
display(union_df)

# COMMAND ----------

# Run this cell to check your work
assert union_df.count() == 235911

# COMMAND ----------

# DBTITLE 0,--i18n-53e0c35c-a419-47ae-b623-e9f0a4643e64
# MAGIC %md
# MAGIC ### 5. 各ユーザーが購入したサイズと品質のオプションをすべてリストアップしてください。
# MAGIC
# MAGIC - **`union_df`** の行を **`email`** でグループ化する。
# MAGIC   - 各ユーザーの **`size`** の全itemの集合を集約して、列のエイリアス（alias）を "size options" にします。
# MAGIC   - 各ユーザーの **`quality`** の全itemの集合を集約して、列のエイリアス（alias）を "quality options" にする。
# MAGIC
# MAGIC 結果を **`options_df`** として保存します。

# COMMAND ----------

# TODO

options_df = (union_df
              .groupBy("email")
              .agg(collect_set("size").alias("size options"),
                   collect_set("quality").alias("quality options"))
             )
display(options_df)

# COMMAND ----------

# Run this cell to check your work
assert options_df.count() == 210370

# COMMAND ----------

# DBTITLE 0,--i18n-3aba526c-edb8-47c5-b7b8-f734d7c3eefc
# MAGIC %md
# MAGIC ### クラスルームで使ったリソースの削除 (Clean up classroom)
# MAGIC
# MAGIC 最後にクラスルームのクリーンアップを行います。

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
