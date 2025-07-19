-- Databricks notebook source
-- MAGIC %md-sandbox
-- MAGIC
-- MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
-- MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
-- MAGIC </div>
-- MAGIC

-- COMMAND ----------

-- DBTITLE 0,--i18n-246366e0-139b-4ee6-8231-af9ffc8b9f20
-- MAGIC %md
-- MAGIC # Unity Catalog でテーブルを作成して共有する(Create and share tables in Unity Catalog)
-- MAGIC
-- MAGIC このノートブックでは、次のことを学びます。
-- MAGIC * スキーマとテーブルを作成する
-- MAGIC * スキーマとテーブルへのアクセスを制御する
-- MAGIC * Unity Catalogのさまざまなオブジェクトに対する権限付与を調べる

-- COMMAND ----------

-- DBTITLE 0,--i18n-675fb98e-c798-4468-9231-710a39216650
-- MAGIC %md
-- MAGIC ## 設定(Set Up)
-- MAGIC
-- MAGIC 次のセルを実行して、セットアップを実行します。
-- MAGIC
-- MAGIC 共有トレーニング環境での競合を避けるために、これにより、専用の一意のカタログ名が生成されます。
-- MAGIC
-- MAGIC 独自の環境では、独自のカタログ名を自由に選択できますが、その環境内の他のユーザーやシステムに影響を与えないように注意してください。

-- COMMAND ----------

-- MAGIC %run ./Includes/Classroom-Setup-06.2

-- COMMAND ----------

-- DBTITLE 0,--i18n-1f8f7a5b-7c09-4333-9057-f9e25f635f94
-- MAGIC %md
-- MAGIC ## Unity Catalog の 3 レベルの名前空間(Unity Catalog three-level namespace)
-- MAGIC
-- MAGIC ほとんどの SQL 開発者は、次のようにスキーマ内のテーブルを明確にアドレス指定するために 2 レベルの名前空間を使用することに精通しています。
-- MAGIC
-- MAGIC      SELECT * FROM schema.table;
-- MAGIC
-- MAGIC Unity Catalog は、オブジェクト階層のスキーマの上に存在する *catalog* の概念を導入しています。 メタストアは任意の数のカタログをホストでき、さらに任意の数のスキーマをホストできます。 この追加レベルに対処するために、Unity Catalog の完全なテーブル参照は 3 レベルの名前空間を使用します。 次のステートメントはこれを示しています。
-- MAGIC
-- MAGIC      SELECT * FROM カタログ.スキーマ.テーブル;
-- MAGIC     
-- MAGIC SQL 開発者は、テーブルを参照するときに常にスキーマを指定する必要がないように、デフォルトのスキーマを選択する **`USE`** ステートメントにも慣れているでしょう。 Unity Catalog はこれを **`USE CATALOG`** ステートメントで補強します。これは同様にデフォルトのカタログを選択します。
-- MAGIC
-- MAGIC エクスペリエンスを簡素化するために、次のコマンドで確認できるように、カタログが作成され、デフォルトとして設定されていることを確認しました。

-- COMMAND ----------

SELECT current_catalog(), current_database()

-- COMMAND ----------

-- DBTITLE 0,--i18n-7608a78c-6f96-4f0b-a9fb-b303c76ad899
-- MAGIC %md
-- MAGIC ## 新しいスキーマを作成して使用する(Create and use a new schema)
-- MAGIC
-- MAGIC この演習専用の新しいスキーマを作成し、これをデフォルトとして設定して、テーブルを名前だけで参照できるようにします。

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS my_own_schema;
USE my_own_schema;

SELECT current_database()

-- COMMAND ----------

-- DBTITLE 0,--i18n-013687c8-6a3f-4c8b-81c1-0afb0429914f
-- MAGIC %md
-- MAGIC ## Delta アーキテクチャを作成する(Create Delta architecture)
-- MAGIC
-- MAGIC Delta アーキテクチャに従ったスキーマとテーブルの単純なコレクションを作成して入力しましょう。
-- MAGIC * 医療機器から読み取った患者の心拍数データを含むシルバー スキーマ
-- MAGIC * 患者ごとの心拍数データを毎日平均するゴールド スキーマ テーブル
-- MAGIC
-- MAGIC 現時点では、この単純な例にはブロンズ テーブルはありません。
-- MAGIC
-- MAGIC 上記でデフォルトのカタログとスキーマを設定したため、以下にテーブル名を指定するだけでよいことに注意してください。

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS patient_silver;

CREATE OR REPLACE TABLE patient_silver.heartrate (
  device_id  INT,
  mrn        STRING,
  name       STRING,
  time       TIMESTAMP,
  heartrate  DOUBLE
);

INSERT INTO patient_silver.heartrate VALUES
  (23,'40580129','Nicholas Spears','2020-02-01T00:01:58.000+0000',54.0122153343),
  (17,'52804177','Lynn Russell','2020-02-01T00:02:55.000+0000',92.5136468131),
  (37,'65300842','Samuel Hughes','2020-02-01T00:08:58.000+0000',52.1354807863),
  (23,'40580129','Nicholas Spears','2020-02-01T00:16:51.000+0000',54.6477014191),
  (17,'52804177','Lynn Russell','2020-02-01T00:18:08.000+0000',95.033344842),
  (37,'65300842','Samuel Hughes','2020-02-01T00:23:58.000+0000',57.3391541312),
  (23,'40580129','Nicholas Spears','2020-02-01T00:31:58.000+0000',56.6165053697),
  (17,'52804177','Lynn Russell','2020-02-01T00:32:56.000+0000',94.8134313932),
  (37,'65300842','Samuel Hughes','2020-02-01T00:38:54.000+0000',56.2469995332),
  (23,'40580129','Nicholas Spears','2020-02-01T00:46:57.000+0000',54.8372685558)

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS patient_gold;

CREATE OR REPLACE TABLE patient_gold.heartrate_stats AS (
  SELECT mrn, name, MEAN(heartrate) avg_heartrate, DATE_TRUNC("DD", time) date
  FROM patient_silver.heartrate
  GROUP BY mrn, name, DATE_TRUNC("DD", time)
);
  
SELECT * FROM patient_gold.heartrate_stats;

-- COMMAND ----------

-- DBTITLE 0,--i18n-3961e85e-2bba-460a-9e00-12e37a07cb87
-- MAGIC %md
-- MAGIC ## ゴールド スキーマへのアクセスを許可する [オプション](Grant access to gold schema [optional])
-- MAGIC
-- MAGIC ここで、**analysts** グループのユーザーが **gold** スキーマから読み取れるようにします。
-- MAGIC
-- MAGIC このセクションは、*ユーザーとグループの管理* 演習に従って、**analysts** という名前の Unity Catalogグループを作成した場合にのみ実行できることに注意してください。
-- MAGIC
-- MAGIC このセクションを実行するには、コード セルのコメントを外し、順番に実行します。
-- MAGIC また、セカンダリ ユーザーとしていくつかのクエリを実行するように求められます。
-- MAGIC
-- MAGIC そのためには:
-- MAGIC 1. 別のプライベート ブラウジング セッションを開き、*ユーザーとグループの管理* の実行時に作成したユーザー ID を使用して Databricks SQL にログインします。
-- MAGIC 1.*Unity Catalogで SQL エンドポイントを作成*の手順に従って、SQL エンドポイントを作成します。
-- MAGIC 1. その環境で、以下の指示に従ってクエリを入力する準備をします。

-- COMMAND ----------

-- DBTITLE 0,--i18n-e4ec17fc-7dfa-4d3f-a82f-02eca61e6e53
-- MAGIC %md
-- MAGIC **gold** テーブルに対する **SELECT** 権限を付与しましょう。

-- COMMAND ----------

-- GRANT SELECT ON TABLE patient_gold.heartrate_stats to `analysts`

-- COMMAND ----------

-- DBTITLE 0,--i18n-d20d5b94-b672-48cf-865a-7c9aa0629955
-- MAGIC %md
-- MAGIC ### ユーザーとしてテーブルをクエリ
-- MAGIC
-- MAGIC **SELECT** 権限を付与して、セカンダリ ユーザーの Databricks SQL 環境でテーブルのクエリを試行します。
-- MAGIC
-- MAGIC 次のセルを実行して、**gold** テーブルから読み取るクエリ ステートメントを出力します。 出力をコピーして、セカンダリ ユーザーの SQL 環境内の新しいクエリに貼り付け、クエリを実行します。

-- COMMAND ----------

-- MAGIC %python
-- MAGIC print(f"SELECT * FROM {DA.catalog_name}.patient_gold.heartrate_stats")

-- COMMAND ----------

-- DBTITLE 0,--i18n-3309187d-5a52-4b51-9198-7fc54ea9ca84
-- MAGIC %md
-- MAGIC テーブルに対する **SELECT** 権限だけでは不十分なため、これはまだ機能しません。 **USAGE** 権限は、含まれる要素に対しても必要です。 以下を実行して、これを修正しましょう。

-- COMMAND ----------

-- GRANT USAGE ON CATALOG ${DA.catalog_name} TO analysts;
-- GRANT USAGE ON SCHEMA patient_gold TO analysts

-- COMMAND ----------

-- DBTITLE 0,--i18n-a6fcc71b-ceb3-4067-acb2-85504ad4d6ea
-- MAGIC %md
-- MAGIC Databricks SQL 環境でクエリを繰り返します。これら 2 つの許可があれば、操作は成功するはずです。

-- COMMAND ----------

-- DBTITLE 0,--i18n-5dd6b7c1-6fed-4d09-b808-0615a10b2502
-- MAGIC %md
-- MAGIC ## アクセス権限を探索（Explore grants）
-- MAGIC
-- MAGIC **gold** テーブルから始め、Unity Catalog 階層内のいくつかのオブジェクトに対する権限を調べてみましょう。

-- COMMAND ----------

-- SHOW GRANT ON TABLE ${DA.catalog_name}.patient_gold.heartrate_stats

-- COMMAND ----------

-- DBTITLE 0,--i18n-e7b6ddda-b6ef-4558-a5b6-c9f97bb7db80
-- MAGIC %md
-- MAGIC 現在、以前に設定した **SELECT** 権限のみがあります。 では、**silver** のアクセス権限を確認してみましょう。

-- COMMAND ----------

SHOW TABLES IN ${DA.catalog_name}.patient_silver;

-- COMMAND ----------

-- SHOW GRANT ON TABLE ${DA.catalog_name}.patient_silver.heartrate

-- COMMAND ----------

-- DBTITLE 0,--i18n-1e9d3c88-af92-4755-a01c-6e0aefdd8c9d
-- MAGIC %md
-- MAGIC 現在、このテーブルには許可がありません。 所有者だけがこのテーブルにアクセスできます。
-- MAGIC
-- MAGIC 次に、含まれているスキーマを見てみましょう。

-- COMMAND ----------

-- SHOW GRANT ON SCHEMA ${DA.catalog_name}.patient_silver

-- COMMAND ----------

-- DBTITLE 0,--i18n-17125954-7b25-40dc-ab84-5a159198e9fc
-- MAGIC %md
-- MAGIC 現在、このスキーマには権限がありません。
-- MAGIC
-- MAGIC では、カタログを見てみましょう。

-- COMMAND ----------

-- SHOW GRANT ON CATALOG `${DA.catalog_name}`

-- COMMAND ----------

-- DBTITLE 0,--i18n-7453efa0-62d0-4af2-901f-c222dd9b2d07
-- MAGIC %md
-- MAGIC 現在、以前に設定した **USAGE** 許可が表示されます。

-- COMMAND ----------

-- DBTITLE 0,--i18n-b4f88042-e7cb-4a1f-b853-cb328356778c
-- MAGIC %md
-- MAGIC ## クリーンアップ(Clean up)
-- MAGIC
-- MAGIC 次のセルを実行して、この例で作成したスキーマを削除します。

-- COMMAND ----------

-- MAGIC %python
-- MAGIC DA.cleanup()

-- COMMAND ----------

-- MAGIC %md-sandbox
-- MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
-- MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
-- MAGIC <br/>
-- MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
