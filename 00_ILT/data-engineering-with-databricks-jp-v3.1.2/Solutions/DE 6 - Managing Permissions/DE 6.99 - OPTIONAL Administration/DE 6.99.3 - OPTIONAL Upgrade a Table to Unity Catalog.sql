-- Databricks notebook source
-- MAGIC %md-sandbox
-- MAGIC
-- MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
-- MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
-- MAGIC </div>
-- MAGIC

-- COMMAND ----------

-- DBTITLE 0,--i18n-5d2baeeb-370f-413f-8eb2-5138b4bf046c
-- MAGIC %md
-- MAGIC # テーブルを Unity カタログにアップグレードする(Upgrade a table to Unity Catalog)
-- MAGIC
-- MAGIC このノートブックでは、次のことを学びます。
-- MAGIC * テーブルを既存のレガシー Hive メタストアから Unity Catalogに移行する
-- MAGIC * 他のユーザーがテーブルにアクセスできるように、適切な許可を作成します
-- MAGIC * Unity Catalogへの移行中に、テーブルで単純な変換を実行します

-- COMMAND ----------

-- DBTITLE 0,--i18n-4111c8be-0a37-43fe-9003-be8c9751760b
-- MAGIC %md
-- MAGIC ## 設定(Set Up)
-- MAGIC
-- MAGIC 次のセルを実行して、セットアップを実行します。 共有トレーニング環境での競合を避けるために、これにより、一意の名前のデータベースが作成され、専用に使用されます。 これにより、従来の Hive メタトー内に **movies** というソース テーブルの例も作成されます。

-- COMMAND ----------

-- MAGIC %run ../Includes/Classroom-Setup-06.99.1

-- COMMAND ----------

-- DBTITLE 0,--i18n-96a90022-a7bb-40db-8429-30c31cbbf215
-- MAGIC %md
-- MAGIC このワークスペースのローカルにある従来の Hive メタストア内に、**movies** というテーブルがあり、上記のセル出力に示されている通りユーザー固有のデータベースに存在します。 簡単にするために、データベース名は *DA.my_schema_name* という名前の Hive 変数に格納されます。 その変数を使用して、このテーブルに格納されているデータをプレビューしてみましょう。
-- MAGIC
-- MAGIC この一意のデータベース名を Hive メタストアで使用して、共有トレーニング環境で他のユーザーと干渉する可能性を回避します。

-- COMMAND ----------

SELECT * FROM hive_metastore.`${DA.my_schema_name}`.movies LIMIT 10

-- COMMAND ----------

-- DBTITLE 0,--i18n-7b2f4105-35f5-4a00-8a19-b4db0c11e045
-- MAGIC %md
-- MAGIC ## 宛先を設定する(Set up destination)
-- MAGIC
-- MAGIC Withソース テーブルを用意したら、Unity Catalogでテーブルの移行先を設定しましょう。

-- COMMAND ----------

-- DBTITLE 0,--i18n-24602317-c35b-4876-9f46-952df2c101cf
-- MAGIC %md
-- MAGIC ### 使用する Unity カタログ メタストアを選択します
-- MAGIC
-- MAGIC ユーザー固有の名前でカタログが作成され、変数 **DA.catalog_name** に保存されました。 Unity カタログ メタストアからこのカタログを選択することから始めましょう。 これにより、テーブル参照でカタログを指定する必要がなくなります。

-- COMMAND ----------

USE CATALOG `${DA.catalog_name}`

-- COMMAND ----------

-- DBTITLE 0,--i18n-179e80a6-3a69-4506-89b0-c8b26d86fada
-- MAGIC %md
-- MAGIC ### 使用するデータベースの作成と選択
-- MAGIC
-- MAGIC 独自のカタログを使用しているので、他との干渉を避けるために独自のデータベースを使用することについて心配する必要はありません。
-- MAGIC
-- MAGIC **bronze_datasets** というデータベースを作成しましょう。

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS bronze_datasets

-- COMMAND ----------

-- DBTITLE 0,--i18n-df709457-d477-48eb-9758-54f4ecf17556
-- MAGIC %md
-- MAGIC 次に、新しく作成したデータベースを選択して、宛先テーブルの操作をさらに簡素化しましょう。 繰り返しますが、この手順は必須ではありませんが、アップグレードしたテーブルへの参照がさらに簡素化されます。

-- COMMAND ----------

USE bronze_datasets

-- COMMAND ----------

-- DBTITLE 0,--i18n-adecfe89-ab61-4392-92ea-b3847d0e3d17
-- MAGIC %md
-- MAGIC ## テーブルをアップグレードする(Upgrade the table)
-- MAGIC
-- MAGIC テーブルのコピーは、3 レベルの名前空間を使用してソース テーブルを指定する単純な **CREATE TABLE AS SELECT** (CTAS) 操作に要約されます。 以前に実行された **USE CATALOG** および **USE** ステートメントにより、3 つのレベルを使用して宛先を指定する必要はありません。
-- MAGIC
-- MAGIC 注: 大きなテーブルの場合、すべてのテーブル データがコピーされるため、この操作には時間がかかる場合があります。

-- COMMAND ----------

CREATE OR REPLACE TABLE movies
AS SELECT * FROM hive_metastore.`${DA.my_schema_name}`.movies

-- COMMAND ----------

-- DBTITLE 0,--i18n-64c49876-3551-4528-be7f-aa9973aac059
-- MAGIC %md
-- MAGIC テーブルがコピーされ、新しいテーブルが Unity カタログの管理下に置かれます。 新しいテーブルに権限が付与されているかどうかを簡単に確認してみましょう。

-- COMMAND ----------

SHOW GRANTS ON movies

-- COMMAND ----------

-- DBTITLE 0,--i18n-2ec10faa-827d-41c7-a697-de4c4ab5ba79
-- MAGIC %md
-- MAGIC 現在、アクセス許可は付与されていません。
-- MAGIC
-- MAGIC 次に、元のテーブルの権限を調べてみましょう。 次のセルのコードのコメントを外して実行します。

-- COMMAND ----------

-- SHOW GRANTS ON hive_metastore.`${DA.my_schema_name}`.movies

-- COMMAND ----------

-- DBTITLE 0,--i18n-dc1999a4-7957-40ec-8a99-cf3cab5c3f77
-- MAGIC %md
-- MAGIC このテーブルはレガシー メタストアにあり、レガシー テーブルのアクセス制御が有効になっているクラスターで実行していないため、エラーが発生します。 これは、Unity Catalog の主な利点を強調しています。安全なソリューションを実現するために追加の構成は必要ありません。 Unity カタログはデフォルトで安全です。

-- COMMAND ----------

-- DBTITLE 0,--i18n-bcd994a7-e48a-4c4c-9d8a-df65ea2577d4
-- MAGIC %md
-- MAGIC ## テーブルへのアクセスを許可する [オプション](Grant access to table [optional])
-- MAGIC
-- MAGIC 新しいテーブルを配置したら、**analysts** グループのユーザーがそこから読み取れるようにしましょう。
-- MAGIC
-- MAGIC このセクションは、*ユーザーとグループの管理* 演習に従って、**analysts** という名前の Unity カタログ グループを作成した場合にのみ実行できることに注意してください。
-- MAGIC
-- MAGIC このセクションを実行するには、コード セルのコメントを外し、順番に実行します。 また、セカンダリ ユーザーとしていくつかのクエリを実行するように求められます。 そのためには:
-- MAGIC
-- MAGIC 1. 別のプライベート ブラウジング セッションを開き、*ユーザーとグループの管理* の実行時に作成したユーザー ID を使用して Databricks SQL にログインします。
-- MAGIC 1.*Unity Catalogで SQL エンドポイントを作成*の手順に従って、SQL エンドポイントを作成します。
-- MAGIC 1. その環境で、以下の指示に従ってクエリを入力する準備をします。

-- COMMAND ----------

-- DBTITLE 0,--i18n-1f594ac2-2b40-451a-a5da-3415c3fe7492
-- MAGIC %md
-- MAGIC ### テーブルに対する SELECT 権限を付与する
-- MAGIC
-- MAGIC 最初の要件は、新しいテーブルに対する **SELECT** 権限を **analysts** グループに付与することです。

-- COMMAND ----------

-- GRANT SELECT ON TABLE movies to `analysts`

-- COMMAND ----------

-- DBTITLE 0,--i18n-1e6e597a-349b-4f83-9ee5-509d6d65db1f
-- MAGIC %md
-- MAGIC ### データベースに USAGE 権限を付与する
-- MAGIC
-- MAGIC データベースに対する **USAGE** 権限も必要です。

-- COMMAND ----------

-- GRANT USAGE ON DATABASE `bronze_datasets` TO `analysts`

-- COMMAND ----------

-- DBTITLE 0,--i18n-76a94a64-a0f8-4ed6-914f-0081fe5e0527
-- MAGIC %md
-- MAGIC ### ユーザーとしてテーブルにアクセス
-- MAGIC
-- MAGIC 適切な権限を付与して、セカンダリ ユーザーの Databricks SQL 環境でテーブルからの読み取りを試みます。
-- MAGIC
-- MAGIC 次のセルを実行して、新しく作成されたテーブルから読み取るクエリ ステートメントを出力します。 出力をコピーして、セカンダリ ユーザーの SQL 環境内の新しいクエリに貼り付け、クエリを実行します。

-- COMMAND ----------

-- MAGIC %python
-- MAGIC print(f"SELECT * FROM {DA.catalog_name}.bronze_datasets.movies")

-- COMMAND ----------

-- DBTITLE 0,--i18n-44e957a6-fa12-42d7-b4e3-fce1d9fad020
-- MAGIC %md
-- MAGIC ## アップグレード中にテーブルを変換する(Transform table while upgrading)
-- MAGIC
-- MAGIC テーブルを Unity Catalog に移行すること自体は簡単な操作ですが、Unity Catalog への全体的な移行は、どの組織にとっても大きなものです。 テーブルとスキーマを綿密に検討し、時間の経過とともに変化する可能性がある組織のビジネス要件にまだ対応しているかどうかを検討する絶好の機会です。
-- MAGIC
-- MAGIC 前に見た例では、ソース テーブルの正確なコピーを取得しています。 テーブルの移行は単純な **CREATE TABLE AS SELECT** 操作であるため、**SELECT** で実行できる変換を移行中に実行できます。 たとえば、前の例を拡張して、次の変換を行います。
-- MAGIC * 最初の列に *idx* という名前を割り当てます
-- MAGIC * さらに、**タイトル**、**年**、**予算**、**評価**の列のみを選択します
-- MAGIC * **year** と **budget** を **INT** に変換します (文字列 *NA* のインスタンスを 0 に置き換えます)
-- MAGIC * **評価**を**DOUBLE**に変換

-- COMMAND ----------

CREATE OR REPLACE TABLE movies
AS SELECT
  _c0 AS idx,
  title,
  CAST(year AS INT) AS year,
  CASE WHEN
    budget = 'NA' THEN 0
    ELSE CAST(budget AS INT)
  END AS budget,
  CAST(rating AS DOUBLE) AS rating
FROM hive_metastore.`${da.my_schema_name}`.movies

-- COMMAND ----------

-- DBTITLE 0,--i18n-b477ffe4-c5de-4fe7-8fec-559daf39e100
-- MAGIC %md
-- MAGIC セカンダリ ユーザーとしてクエリを実行している場合は、セカンダリ ユーザーの Databricks SQL 環境で前のクエリを再実行します。 それを確認する：
-- MAGIC 1. テーブルには引き続きアクセスできます
-- MAGIC 1. テーブル スキーマが更新されました

-- COMMAND ----------

-- DBTITLE 0,--i18n-c1b1fada-41b8-41e8-af6f-2454369231db
-- MAGIC %md
-- MAGIC ## クリーンアップ
-- MAGIC
-- MAGIC 次のセルを実行して、この例で使用されたソース データベースとテーブルを削除します。

-- COMMAND ----------

-- MAGIC %python
-- MAGIC DA.cleanup()

-- COMMAND ----------

-- MAGIC %md-sandbox
-- MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
-- MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
-- MAGIC <br/>
-- MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
