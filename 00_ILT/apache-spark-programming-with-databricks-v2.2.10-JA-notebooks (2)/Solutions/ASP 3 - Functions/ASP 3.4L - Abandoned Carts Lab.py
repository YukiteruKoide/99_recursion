# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-4ddb1d34-621f-4f23-8b3d-f6180f1bb7c2
# MAGIC %md
# MAGIC # カゴ落ちラボ (Abandoned Carts Lab)
# MAGIC 購入しなかったユーザーのEメールごとに、カゴ落ちした商品を取得しましょう。
# MAGIC 1. トランザクションからのコンバージョンしたユーザーのEメールの取得
# MAGIC 2. ユーザーIDとEメールの結合
# MAGIC 3. 各ユーザーのカートの商品履歴の取得
# MAGIC 4. カートの商品履歴とEメールの結合
# MAGIC 5. カゴ落ち商品とひもづくEメールの抽出
# MAGIC
# MAGIC ##### メソッド (Methods)
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.join.html#pyspark.sql.DataFrame.join" target="_blank">DataFrame</a>: **`join`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html" target="_blank">組み込み関数</a>: **`collect_set`**, **`explode`**, **`lit`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameNaFunctions.html#pyspark.sql.DataFrameNaFunctions" target="_blank">DataFrameNaFunctions</a>: **`fill`**

# COMMAND ----------

# DBTITLE 0,--i18n-2b181f29-66cc-4e06-bb94-5ac965a1e8ca
# MAGIC %md
# MAGIC ### セットアップ (Setup)
# MAGIC 以下のセルを実行して<strong>`sales_df`</strong>、<strong>`users_df`</strong>、<strong>`events_df`</strong>のデータフレームを作成します。

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# sale transactions at BedBricks
sales_df = spark.read.format("delta").load(DA.paths.sales)
display(sales_df)

# COMMAND ----------

# user IDs and emails at BedBricks
users_df = spark.read.format("delta").load(DA.paths.users)
display(users_df)

# COMMAND ----------

# events logged on the BedBricks website
events_df = spark.read.format("delta").load(DA.paths.events)
display(events_df)

# COMMAND ----------

# DBTITLE 0,--i18n-b0a89a88-a4ad-4fea-a2a3-b132f042d256
# MAGIC %md
# MAGIC ### 1: トランザクションからのコンバージョンしたユーザーのEメールの取得 (Get emails of converted users from transactions)
# MAGIC - <strong>`salesDF`</strong>の <strong>`email`</strong>列を抽出し、重複を削除してください
# MAGIC - 全ての行に<strong>`True`</strong>の値を持つ新しい列<strong>`converted`</strong>を追加してください
# MAGIC
# MAGIC 結果を<strong>`converted_users_df`</strong>として保存してください。

# COMMAND ----------

# ANSWER
from pyspark.sql.functions import *

converted_users_df = (sales_df
                      .select("email")
                      .distinct()
                      .withColumn("converted", lit(True))
                     )
display(converted_users_df)

# COMMAND ----------

# DBTITLE 0,--i18n-29604628-777b-499c-81ef-3a0a02fba146
# MAGIC %md
# MAGIC #### 1.1: 作業結果の確認 (Check Your Work)
# MAGIC
# MAGIC 作成したソリューションが正しいかどうか確認するために以下のセルを実行してください:

# COMMAND ----------

expected_columns = ["email", "converted"]

expected_count = 210370

assert converted_users_df.columns == expected_columns, "converted_users_df does not have the correct columns"

assert converted_users_df.count() == expected_count, "converted_users_df does not have the correct number of rows"

assert converted_users_df.select(col("converted")).first()[0] == True, "converted column not correct"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-7921ccc0-93ff-480d-b47b-1ec5225f1d70
# MAGIC %md
# MAGIC ### 2: ユーザーIDとEメールの結合 (Join emails with user IDs)
# MAGIC - <strong>`converted_users_df`</strong>と<strong>`users_df`</strong>を<strong>`email`</strong>列を使って外部結合してください
# MAGIC - <strong>`email`</strong>がnullではないユーザーを抽出してください
# MAGIC - <strong>`converted`</strong>のnull値を<strong>`False`</strong>で置換してください
# MAGIC
# MAGIC 結果を<strong>`conversions_df`</strong>として保存してください。

# COMMAND ----------

# ANSWER
conversions_df = (users_df
                  .join(converted_users_df, "email", "outer")
                  .filter(col("email").isNotNull())
                  .na.fill(False)
                 )
display(conversions_df)

# COMMAND ----------

# DBTITLE 0,--i18n-4e3a3a42-719c-4e54-8ac7-242a7d4c1149
# MAGIC %md
# MAGIC #### 2.1: 作業結果の確認 (Check Your Work)
# MAGIC
# MAGIC 作成したソリューションが正しいかどうか確認するために以下のセルを実行してください:

# COMMAND ----------

expected_columns = ["email", "user_id", "user_first_touch_timestamp", "converted"]

expected_count = 782749

expected_false_count = 572379

assert conversions_df.columns == expected_columns, "Columns are not correct"

assert conversions_df.filter(col("email").isNull()).count() == 0, "Email column contains null"

assert conversions_df.count() == expected_count, "There is an incorrect number of rows"

assert conversions_df.filter(col("converted") == False).count() == expected_false_count, "There is an incorrect number of false entries in converted column"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-ea3dc5ec-1f2a-4887-88a0-053f91ff981d
# MAGIC %md
# MAGIC ### 3: 各ユーザーのカートの商品履歴の取得 (Get cart item history for each user)
# MAGIC - <strong>`events_df`</strong>の<strong>`items`</strong>フィールドの1レコードを複数行（explode)にして既存の<strong>`items`</strong>フィールドを置き換えてください
# MAGIC - <strong>`user_id`</strong>でグループ化してください
# MAGIC   - 各ユーザーの全ての<strong>`items.item_id`</strong>をセットとして集めて(collect a set)、"cart"という列にしてください
# MAGIC
# MAGIC 結果を<strong>`carts_df`</strong>として保存してください。

# COMMAND ----------

# ANSWER
carts_df = (events_df
            .withColumn("items", explode("items"))
            .groupBy("user_id").agg(collect_set("items.item_id").alias("cart"))
           )
display(carts_df)

# COMMAND ----------

# DBTITLE 0,--i18n-46fe477b-c8da-4b9a-983c-89cf8d2c9ae3
# MAGIC %md
# MAGIC #### 3.1: 作業結果の確認 (Check Your Work)
# MAGIC
# MAGIC 作成したソリューションが正しいかどうか確認するために以下のセルを実行してください:

# COMMAND ----------

expected_columns = ["user_id", "cart"]

expected_count = 488403

assert carts_df.columns == expected_columns, "Incorrect columns"

assert carts_df.count() == expected_count, "Incorrect number of rows"

assert carts_df.select(col("user_id")).drop_duplicates().count() == expected_count, "Duplicate user_ids present"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-6cd1dfc6-79dc-41a4-aaab-4678010f4937
# MAGIC %md
# MAGIC ### 4: カートの商品履歴とEメールの結合 (Join cart item history with emails)
# MAGIC - <strong>`conversions_df`</strong>と<strong>`carts_df`</strong>を<strong>`user_id`</strong>フィールドで左外部結合してください
# MAGIC
# MAGIC 結果を<strong>`email_carts_df`</strong>として保存してください。

# COMMAND ----------

# ANSWER
email_carts_df = conversions_df.join(carts_df, "user_id", "left")
display(email_carts_df)

# COMMAND ----------

# DBTITLE 0,--i18n-993e55d9-76aa-4772-b5ce-078b2cc18a2e
# MAGIC %md
# MAGIC #### 4.1: 作業結果の確認 (Check Your Work)
# MAGIC
# MAGIC 作成したソリューションが正しいかどうか確認するために以下のセルを実行してください:

# COMMAND ----------

expected_columns = ["user_id", "email", "user_first_touch_timestamp", "converted", "cart"]

expected_count = 782749

expected_cart_null_count = 397799

assert email_carts_df.columns == expected_columns, "Columns do not match"

assert email_carts_df.count() == expected_count, "Counts do not match"

assert email_carts_df.filter(col("cart").isNull()).count() == expected_cart_null_count, "Cart null counts incorrect from join"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-bfb161e8-f598-4907-9176-b3ebd7906075
# MAGIC %md
# MAGIC ### 5: Filter for emails with abandoned cart items
# MAGIC - <strong>`email_carts_df`</strong>から<strong>`converted`</strong>がFalseであるユーザーを抽出してください
# MAGIC - カートがnullではないユーザーを抽出してください
# MAGIC
# MAGIC 結果を<strong>`abandoned_carts_df`</strong>として保存してください。

# COMMAND ----------

# ANSWER
abandoned_carts_df = (email_carts_df
                      .filter(col("converted") == False)
                      .filter(col("cart").isNotNull())
                     )
display(abandoned_carts_df)

# COMMAND ----------

# DBTITLE 0,--i18n-36dee8eb-e975-4db1-b4d6-ad3b9cf3e3bd
# MAGIC %md
# MAGIC #### 5.1: 作業結果の確認 (Check Your Work)
# MAGIC
# MAGIC 作成したソリューションが正しいかどうか確認するために以下のセルを実行してください:

# COMMAND ----------

expected_columns = ["user_id", "email", "user_first_touch_timestamp", "converted", "cart"]

expected_count = 204272

assert abandoned_carts_df.columns == expected_columns, "Columns do not match"

assert abandoned_carts_df.count() == expected_count, "Counts do not match"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-913e5176-9e31-4b70-a5fb-e4d7dddde6d8
# MAGIC %md
# MAGIC ### 6: ボーナスアクティビティ (Bonus Activity)
# MAGIC 商品単位でカゴ落ちした数をプロットしてください

# COMMAND ----------

# ANSWER
abandoned_items_df = (abandoned_carts_df
                      .withColumn("items", explode("cart"))
                      .groupBy("items")
                      .count()
                      .sort("items")
                     )
display(abandoned_items_df)

# COMMAND ----------

# DBTITLE 0,--i18n-47be8a6d-17cd-4e34-b1cb-e85d7bf7a710
# MAGIC %md
# MAGIC #### 6.1: 作業結果の確認 (Check Your Work)
# MAGIC
# MAGIC 作成したソリューションが正しいかどうか確認するために以下のセルを実行してください:

# COMMAND ----------

abandoned_items_df.count()

# COMMAND ----------

expected_columns = ["items", "count"]

expected_count = 12

assert abandoned_items_df.count() == expected_count, "Counts do not match"

assert abandoned_items_df.columns == expected_columns, "Columns do not match"
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-75c53b88-3ac3-4dc2-9b99-e3a08e48c5f1
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
