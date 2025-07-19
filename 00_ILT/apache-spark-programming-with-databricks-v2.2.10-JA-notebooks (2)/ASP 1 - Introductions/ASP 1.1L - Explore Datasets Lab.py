# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-07f4fc7f-00c7-45f0-a3da-d8317e646802
# MAGIC %md
# MAGIC # データセット探索ラボ (Explore Datasets Lab)
# MAGIC
# MAGIC このコースで使用されるデータセットを探索します。
# MAGIC
# MAGIC ### ベッドブリックのケーススタディ (BedBricks Case Study)
# MAGIC このコースでは、マットレスのオンライン小売業者であるBedBricksのクリックストリームデータを探索するケーススタディになります。 
# MAGIC あなたはBedBricksのアナリストで、 **`イベント`** 、 **`売上`** 、 **`ユーザー`** 、 **`製品`** のデータセットを使用しています。
# MAGIC
# MAGIC ##### タスク (Tasks)
# MAGIC 1. マジックコマンドを使用して DBFS 内のデータファイルを表示する
# MAGIC 1. dbtils を使用して DBFS 内のデータファイルを表示する
# MAGIC 1. DBFS のファイルからのテーブルの作成
# MAGIC 1. SQL を実行して BedBricks データセットに関する質問に答える

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-418554c8-03e8-461f-9724-6314c7acd53e
# MAGIC %md
# MAGIC ### 1.マジックコマンドを使用して DBFS 内のファイルを一覧表示する
# MAGIC マジックコマンド **`dbfs: /mnt/dbacademy-users/`** を使用して DBFS ディレクトリにあるファイルを表示してください。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint">自分のものを含む複数のユーザーディレクトリが表示されます。権限によっては、自分のユーザーディレクトリのみが表示される場合があります。

# COMMAND ----------

# MAGIC %fs ls /mnt/dbacademy-users/ 

# COMMAND ----------

# DBTITLE 0,--i18n-8ad4d9c6-75e8-4f02-9962-20045fc781be
# MAGIC %md
# MAGIC ### 2.dbutils を使用して DBFS 内のファイルを一覧表示する。
# MAGIC - **`dbutils`** を使用して上記のディレクトリにあるファイルを取得し、それを変数 **`files`** に割り当てます。
# MAGIC - Databricks display() 関数を使用して、 **`ファイル`** 内の内容を表示します。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint">前と同じように、自分のものを含む複数のユーザーディレクトリが表示されます。

# COMMAND ----------

# TODO
files = dbutils.fs.ls('dbfs:/mnt/dbacademy-users/yukiteru.koide@databricks.com/')
display(files)

# COMMAND ----------

# DBTITLE 0,--i18n-28ce7cfb-287a-47a9-8974-c0a99bedcf2e
# MAGIC %md
# MAGIC ### 3.DBFS のファイルから以下のテーブルを作成する
# MAGIC - spark-context変数 **`DA.paths.users`** を使用して **`users`** テーブルを作成します
# MAGIC - spark-context変数 **`DA.paths.sales`** を使用して **`sales`** テーブルを作成します
# MAGIC - spark-context変数 **`DA.paths.products`** を使用して **`products`** テーブルを作成します
# MAGIC - spark-context変数 **`DA.paths.events`** を使用して **`events`** テーブルを作成します
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png">ヒント: **`events`** テーブルは前のノートブックで作成しましたが、データベースは異なります。

# COMMAND ----------

print(DA.paths.users)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS users USING delta OPTIONS (path "${DA.paths.users}");
# MAGIC CREATE TABLE IF NOT EXISTS sales USING delta OPTIONS (path "${DA.paths.sales}");
# MAGIC CREATE TABLE IF NOT EXISTS products USING delta OPTIONS (path "${DA.paths.products}");
# MAGIC CREATE TABLE IF NOT EXISTS events USING delta OPTIONS (path "${DA.paths.events}");

# COMMAND ----------

# DBTITLE 0,--i18n-fbbfc7b2-2a54-4b81-a17f-77de6aec377f
# MAGIC %md
# MAGIC ワークスペース UI のデータタブを使用して、テーブルが作成されたことを確認します。

# COMMAND ----------

# DBTITLE 0,--i18n-55e585c9-b437-44c6-ac03-f11c7cd9c38b
# MAGIC %md
# MAGIC ### 4.SQLでBedBricks のデータセットを探索する
# MAGIC 次の質問に回答するため、 **`製品`** 、 **`売上`** 、および **`イベント`** テーブルへSQLクエリを実行します。
# MAGIC - BedBricksではどういう製品を販売していますか？
# MAGIC - BedBricksでの取引の平均購入収益はいくらですか？
# MAGIC -BedBricksのウェブサイトにはどのようなイベントが記録されていますか？
# MAGIC
# MAGIC 関連するデータセットのスキーマは、以下のセル内に質問ごとに提供されています。

# COMMAND ----------

# DBTITLE 0,--i18n-60b7be2f-7f11-4e34-bf18-57e39d69f6ca
# MAGIC %md
# MAGIC #### 4.1:BedBricksではどういう製品を販売していますか？
# MAGIC
# MAGIC **`products`** データセットには、BedBricks小売サイトで販売されている製品のID、名前、価格が含まれています。
# MAGIC
# MAGIC | field | type | description
# MAGIC | --- | --- | --- |
# MAGIC | item_id | string | アイテムの識別子 |
# MAGIC | name | string | アイテム名 |
# MAGIC | price | double | アイテム価格 |
# MAGIC
# MAGIC **`products`** テーブルからすべてのレコードを選択する SQLクエリを実行します。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint">12 個の製品が表示されます。

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM products

# COMMAND ----------

# DBTITLE 0,--i18n-535df503-7397-4c6b-a89b-39b310f09ff7
# MAGIC %md
# MAGIC #### 4.2:BedBricksでの取引の平均購入収益はいくらですか？
# MAGIC
# MAGIC **`sales`** データセットには、正常に処理された注文情報が含まれています。 
# MAGIC ほとんどの項目は、販売確定イベントに関連するクリックストリームデータの項目と直接対応しています。
# MAGIC
# MAGIC | field | type | description|
# MAGIC | --- | --- | --- |
# MAGIC | order_id | long | unique identifier |
# MAGIC | email | string | 販売設定が送信された電子メールアドレス |
# MAGIC | transaction_timestamp | long | 注文が処理されたタイムスタンプ（ミリ秒単位で記録）|
# MAGIC | total_item_quantity | long |  注文のアイテム数 |
# MAGIC | purchase_revenue_in_usd | double | 注文の合計利益 |
# MAGIC | unique_items | long | 注文に含まれるユニーク商品数 |
# MAGIC | items | array | JSON データのリストとして提供され、Spark によって構造体の配列として解釈される |
# MAGIC
# MAGIC **`sales`** テーブルから平均 **`purchase_revenue_in_usd`** を計算するSQLクエリを実行します。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint">結果は **`1042.79`** になるはずです。

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT avg(purchase_revenue_in_usd) FROM sales 

# COMMAND ----------

# DBTITLE 0,--i18n-1646e571-2039-4f10-b407-5139b89199ef
# MAGIC %md
# MAGIC #### 4.3:BedBricksのウェブサイトにはどのようなイベントが記録されていますか？
# MAGIC
# MAGIC **`events`** データセットには、データベースを更新して作成された、2 週間分の解析済みの JSON レコードが含まれています。 
# MAGIC 記録は次の場合に受信されます。(1) 新規ユーザーがサイトにアクセスする、(2) ユーザーが初めてメールアドレスを提供する。
# MAGIC
# MAGIC | field | type | description|
# MAGIC | --- | --- | --- |
# MAGIC | device | string | ユーザーデバイスのオペレーティングシステム |
# MAGIC | user_id | string | ユーザーあるいはセッションの識別子 |
# MAGIC | user_first_touch_timestamp | long |マイクロ秒単位でユーザーが初めて記録された時刻 |
# MAGIC | traffic_source | string | 参照元 |
# MAGIC | geo (city, state) | struct |  IP アドレスから取得された都市と州の情報 |
# MAGIC | event_timestamp | long | マイクロ秒単位で記録されたイベント時刻 |
# MAGIC | event_previous_timestamp | long | マイクロ秒単位で記録された前回イベントの時刻 |
# MAGIC | event_name | string | クリックストリームトラッカーに登録されているイベント名 |
# MAGIC | items (item_id, item_name, price_in_usd, quantity, item_revenue in usd, coupon)| array |  ユーザーのカート内の各アイテムに対応する構造体の配列 |
# MAGIC | ecommerce (total_item_quantity, unique_items, purchase_revenue_in_usd)  |  struct  | 購入データ (この項目は、売り上げ確定に対応するイベントのみ値が入っている) |
# MAGIC
# MAGIC **`events`** テーブルから **`event_name`** の異なる値のを選択する SQL クエリを実行する
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint">23 個の異なる **`event_name`** 値が表示されるはずです。

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT DISTINCT event_name FROM events

# COMMAND ----------

# DBTITLE 0,--i18n-d68908dd-7069-4671-850a-db458003aa53
# MAGIC %md
# MAGIC ### クラスルームで使ったリソースの削除 (Clean up classroom)
# MAGIC このレッスンで作成された一時ファイル、テーブル、およびデータベースをクリーンアップします。

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
