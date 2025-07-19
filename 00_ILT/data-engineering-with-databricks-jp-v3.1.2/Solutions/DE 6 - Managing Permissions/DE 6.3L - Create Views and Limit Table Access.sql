-- Databricks notebook source
-- MAGIC %md-sandbox
-- MAGIC
-- MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
-- MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
-- MAGIC </div>
-- MAGIC

-- COMMAND ----------

-- DBTITLE 0,--i18n-20e4c711-c890-4ef6-bc9b-328f8550ed08
-- MAGIC %md
-- MAGIC # ビューを作成してテーブル アクセスを制限する(Create views and limit table access)
-- MAGIC
-- MAGIC このノートブックでは、次のことを学びます。
-- MAGIC * ビューを作成する
-- MAGIC * ビューへのアクセスを管理する
-- MAGIC * 動的ビュー機能を使用して、テーブル内の列と行へのアクセスを制限します

-- COMMAND ----------

-- DBTITLE 0,--i18n-ede11fd8-42c7-4b13-863e-30eb9eee7fc3
-- MAGIC %md
-- MAGIC ## 設定(Set Up)
-- MAGIC
-- MAGIC 次のセルを実行して、セットアップを実行します。 共有トレーニング環境での競合を避けるために、これにより、一意の名前のデータベースが作成され、専用に使用されます。 これにより、Unity カタログ メタトーレ内に **silver** というサンプル テーブルも作成されます。

-- COMMAND ----------

-- DBTITLE 0,--i18n-e7942e1d-097f-43a5-a1d7-d54af274b859
-- MAGIC %md
-- MAGIC 注: このノートブックは、Unity カタログ メタストアに *main* という名前のカタログがあることを前提としています。 別のカタログをターゲットにする必要がある場合は、先に進む前にノートブック **Classroom-Setup** を編集してください。

-- COMMAND ----------

-- MAGIC %run ./Includes/Classroom-Setup-06.3

-- COMMAND ----------

-- DBTITLE 0,--i18n-ef87e152-8e6a-4fd9-8cc7-579545aa01f9
-- MAGIC %md
-- MAGIC **silver** テーブルの内容を調べてみましょう。
-- MAGIC
-- MAGIC 注: セットアップの一環として、デフォルトのカタログとデータベースが選択されているため、テーブルまたはビューの名前を指定するだけで、レベルを追加する必要はありません。

-- COMMAND ----------

SELECT * FROM silver.heartrate_device

-- COMMAND ----------

-- DBTITLE 0,--i18n-f9c4630d-c04d-4ec3-8c20-8afea4ec7e37
-- MAGIC %md
-- MAGIC ## ゴールド ビューを作成する（Create gold view）
-- MAGIC
-- MAGIC シルバー テーブルを用意したら、シルバーからデータを集計するビューを作成し、メダリオン アーキテクチャのゴールド レイヤーに適したデータを表示します。

-- COMMAND ----------

CREATE OR REPLACE VIEW gold.heartrate_avgs AS (
  SELECT mrn, name, MEAN(heartrate) avg_heartrate, DATE_TRUNC("DD", time) date
  FROM silver.heartrate_device
  GROUP BY mrn, name, DATE_TRUNC("DD", time))

-- COMMAND ----------

-- DBTITLE 0,--i18n-2eb72987-961a-4020-b775-1e5e29c08a1a
-- MAGIC %md
-- MAGIC ゴールド ビューを調べてみましょう。

-- COMMAND ----------

SELECT * FROM gold.heartrate_avgs

-- COMMAND ----------

-- DBTITLE 0,--i18n-f5ccd808-ffbd-4e06-8ca2-c03dd80ad8e2
-- MAGIC %md
-- MAGIC ## ビューへのアクセスを許可する [オプション](Grant access to view [optional])
-- MAGIC
-- MAGIC 新しいビューを配置したら、**analysts** グループのユーザーがクエリできるようにしましょう。
-- MAGIC
-- MAGIC
-- MAGIC このセクションは、*ユーザーとグループの管理* 演習に従って、**analysts** という名前の Unity カタログ グループを作成した場合にのみ実行できることに注意してください。
-- MAGIC
-- MAGIC このセクションを実行するには、コード セルのコメントを外し、順番に実行します。 また、セカンダリ ユーザーとしていくつかのクエリを実行するように求められます。 これをする：
-- MAGIC
-- MAGIC 1. 別のプライベート ブラウジング セッションを開き、*ユーザーとグループの管理* の実行時に作成したユーザー ID を使用して Databricks SQL にログインします。
-- MAGIC 1.*Unity カタログで SQL エンドポイントを作成*の手順に従って、SQL エンドポイントを作成します。
-- MAGIC 1. その環境で、以下の指示に従ってクエリを入力する準備をします。

-- COMMAND ----------

-- SHOW GRANT ON VIEW gold.heartrate_avgs

-- COMMAND ----------

-- SHOW GRANT ON TABLE silver.heartrate_device

-- COMMAND ----------

-- DBTITLE 0,--i18n-9bf38439-6ad4-4db5-bb4f-fe70b8e4cfec
-- MAGIC %md
-- MAGIC ### ビューに対する SELECT 権限を付与する
-- MAGIC
-- MAGIC 最初の要件は、ビューに対する **SELECT** 権限を **analysts** グループに付与することです。

-- COMMAND ----------

-- GRANT SELECT ON VIEW gold.heartrate_avgs to `analysts`

-- COMMAND ----------

-- DBTITLE 0,--i18n-fbb44902-4662-4d9a-ab11-462a2b07a665
-- MAGIC %md
-- MAGIC ### カタログとデータベースに USAGE 権限を付与する
-- MAGIC
-- MAGIC テーブルと同様に、ビューをクエリするには、カタログとデータベースに対する **USAGE** 権限も必要です。

-- COMMAND ----------

-- GRANT USAGE ON CATALOG ${DA.catalog_name} TO `analysts`;
-- GRANT USAGE ON DATABASE gold TO `analysts`

-- COMMAND ----------

-- DBTITLE 0,--i18n-cfe19914-4f92-47da-a250-2d350a39736f
-- MAGIC %md
-- MAGIC ### ユーザーとしてビューをクエリ
-- MAGIC
-- MAGIC 適切な権限を付与して、セカンダリ ユーザーの Databricks SQL 環境でビューのクエリを試行します。
-- MAGIC
-- MAGIC 次のセルを実行して、ビューから読み取るクエリ ステートメントを出力します。 出力をコピーして、セカンダリ ユーザーの SQL 環境内の新しいクエリに貼り付け、クエリを実行します。

-- COMMAND ----------

-- MAGIC %python
-- MAGIC print(f"SELECT * FROM gold.heartrate_avgs")

-- COMMAND ----------

-- DBTITLE 0,--i18n-330f0448-6bef-42bc-930d-1716886c97fb
-- MAGIC %md
-- MAGIC 予想どおり、クエリが成功し、出力が上記の出力と同じになることに注意してください。
-- MAGIC
-- MAGIC **`gold.heartrate_avgs`** を **`silver.heartrate_device`** に置き換えて、クエリを再実行します。 クエリが失敗することに注意してください。 これは、ユーザーが **`silver.heartrate_device`** テーブルに対する **SELECT** 権限を持っていないためです。

-- COMMAND ----------

-- MAGIC %python
-- MAGIC print(f"SELECT * FROM silver.heartrate_device ")

-- COMMAND ----------

-- DBTITLE 0,--i18n-7c6916be-d36a-4655-b95c-94402222573f
-- MAGIC %md
-- MAGIC **`heartrate_avgs`** は **`heartrate_device`** から選択するビューであることを思い出してください。 では、 **`heartrate_avgs`** に対するクエリはどのように成功するのでしょうか? Unity Catalog は、そのビューの *所有者* が **`silver.heartrate_device`** に対する **SELECT** 権限を持っているため、クエリの通過を許可します。 保護しようとしている基礎となるテーブルへの直接アクセスを許可せずに、テーブルの行または列をフィルターまたはマスクできるビューを実装できるため、これは重要なプロパティです。 次に、このメカニズムの動作を確認します。

-- COMMAND ----------

-- DBTITLE 0,--i18n-4ea26d47-eee0-43e9-867b-4b6913679e41
-- MAGIC %md
-- MAGIC ## 動的ビュー(Dynamic views)
-- MAGIC
-- MAGIC 動的ビューを使用すると、次のようなきめ細かいアクセス制御を構成できます。
-- MAGIC * 列または行のレベルでのセキュリティ。
-- MAGIC * データマスキング。
-- MAGIC
-- MAGIC アクセス制御は、ビューの定義内で関数を使用することによって達成されます。 これらの機能には次のものがあります。
-- MAGIC * **`current_user()`**: 現在のユーザーのメールアドレスを返します
-- MAGIC * **`is_account_group_member()`**: 現在のユーザーが指定されたグループのメンバーである場合に TRUE を返します
-- MAGIC
-- MAGIC 注: 従来の互換性のために、現在のユーザーが指定されたワークスペース レベルのグループのメンバーである場合に TRUE を返す関数 **`is_member()`** もあります。 Unity カタログに動的ビューを実装する場合は、この関数を使用しないでください。

-- COMMAND ----------

-- DBTITLE 0,--i18n-b39146b7-362b-46db-9a59-a8c589e94392
-- MAGIC %md
-- MAGIC ### 列を制限する
-- MAGIC
-- MAGIC **`is_account_group_member()`** を適用して **`SELECT`** 内の **`CASE`** ステートメントを介して **analysts** グループのメンバーの PII を含む列をマスクします。
-- MAGIC
-- MAGIC 注: これは、このトレーニング環境のセットアップに合わせた簡単な例です。 本番システムでは、特定のグループのメンバーではないユーザーの行を制限することをお勧めします。

-- COMMAND ----------

CREATE OR REPLACE VIEW gold.heartrate_avgs AS
SELECT
  CASE WHEN
    is_account_group_member('analysts') THEN 'REDACTED'
    ELSE mrn
  END AS mrn,
  CASE WHEN
    is_account_group_member('analysts') THEN 'REDACTED'
    ELSE name
  END AS name,
  MEAN(heartrate) avg_heartrate,
  DATE_TRUNC("DD", time) date
  FROM silver.heartrate_device
  GROUP BY mrn, name, DATE_TRUNC("DD", time)

-- COMMAND ----------

-- DBTITLE 0,--i18n-c5c4afac-2736-4a57-be57-55535654a227
-- MAGIC %md
-- MAGIC 次に、更新されたビューで許可を再発行しましょう。

-- COMMAND ----------

-- GRANT SELECT ON VIEW gold.heartrate_avgs to `analysts`

-- COMMAND ----------

-- DBTITLE 0,--i18n-271fb0d5-34f1-435f-967e-4cc650facd01
-- MAGIC %md
-- MAGIC ビューをクエリしてみましょう。これにより、フィルター処理されていない出力が得られます (現在のユーザーが **analysts** グループに追加されていないと仮定します)。

-- COMMAND ----------

SELECT * FROM gold.heartrate_avgs

-- COMMAND ----------

-- DBTITLE 0,--i18n-1754f589-d48f-499d-b352-3fa735305eb9
-- MAGIC %md
-- MAGIC Databricks SQL 環境で以前に実行したクエリを再実行します (**`silver`** を **`gold_dailyavg`** に戻します)。 PII がフィルタリングされていることに注意してください。 ビューによって保護されているため、このグループのメンバーが PII にアクセスする方法はなく、基になるテーブルに直接アクセスすることはできません。

-- COMMAND ----------

-- DBTITLE 0,--i18n-f7759fba-c2f8-4471-96f7-aa1ea5a6a00b
-- MAGIC %md
-- MAGIC ### 行を制限する
-- MAGIC
-- MAGIC **`is_account_group_member()`** を適用して行を除外しましょう。 この場合、**analysts** グループのメンバーに限定されたタイムスタンプと心拍数の値を、デバイス ID が 30 未満の行に返す新しいゴールド ビューを作成します。
-- MAGIC 行のフィルタリングは、**`SELECT`** の **`WHERE`** 句として条件を適用することで実行できます。

-- COMMAND ----------

CREATE OR REPLACE VIEW gold_allhr AS
SELECT
  mrn,
  time,
  device_id,
  heartrate
FROM silver.heartrate_device
WHERE
  CASE WHEN
    is_account_group_member('analysts') THEN device_id < 30
    ELSE TRUE
  END

-- COMMAND ----------

-- GRANT SELECT ON VIEW gold_allhr to `analysts`

-- COMMAND ----------

SELECT * FROM gold_allhr

-- COMMAND ----------

-- DBTITLE 0,--i18n-63255ec6-2317-455c-9665-e1c2069546f4
-- MAGIC %md
-- MAGIC Databricks SQL 環境で以前に実行したクエリを再実行します (**`gold_dailyavg`** を **`gold_allhr`** に変更します)。 デバイス ID が 30 以上の行は出力から省略されていることに注意してください。

-- COMMAND ----------

-- DBTITLE 0,--i18n-d11e2467-cd67-411e-bedd-4ebe55301985
-- MAGIC %md
-- MAGIC ### データマスキング
-- MAGIC
-- MAGIC 動的ビューの最後の使用例は、データをマスクすることです。 つまり、データのサブセットを通過させますが、マスクされたフィールド全体を推測できないように変換します。
-- MAGIC
-- MAGIC ここでは、行フィルタリングと列フィルタリングのアプローチを組み合わせて、行フィルタリング ビューをデータ マスキングで強化します。 ただし、列全体を文字列 **REDACTED** で置き換えるのではなく、SQL 文字列操作関数を使用して **mrn** の最後の 2 桁を表示し、残りをマスクします。
-- MAGIC
-- MAGIC 必要に応じて、SQL はデータをマスクするために利用できるさまざまな文字列操作関数のライブラリを提供します。 以下に示すアプローチは、この単純な例を示しています。

-- COMMAND ----------

CREATE OR REPLACE VIEW gold_allhr AS
SELECT
  CASE WHEN
    is_account_group_member('analysts') THEN CONCAT("******", RIGHT(mrn, 2))
    ELSE mrn
  END AS mrn,
  time,
  device_id,
  heartrate
FROM silver.heartrate_device
WHERE
  CASE WHEN
    is_account_group_member('analysts') THEN device_id < 30
    ELSE TRUE
  END

-- COMMAND ----------

-- GRANT SELECT ON VIEW gold_allhr to `analysts`

-- COMMAND ----------

SELECT * FROM gold_allhr

-- COMMAND ----------

-- DBTITLE 0,--i18n-c379505f-ebad-474d-9dad-92fa8a7a7ee9
-- MAGIC %md
-- MAGIC Databricks SQL 環境で、**gold_allhr** に対してクエリを最後にもう一度実行します。 一部の行がフィルター処理されていることに加えて、**mrn** 列がマスクされ、最後の 2 桁のみが表示されることに注意してください。 これにより、記録を既知の患者と関連付けるのに十分な情報が提供されますが、それ自体では PII が漏えいすることはありません。

-- COMMAND ----------

-- DBTITLE 0,--i18n-8828d381-084f-43fa-afc3-a5a2ba170aeb
-- MAGIC %md
-- MAGIC ## クリーンアップ(Clean up)
-- MAGIC 次のセルを実行して、この例で使用されたアセットを削除します。

-- COMMAND ----------

-- MAGIC %python
-- MAGIC DA.cleanup()

-- COMMAND ----------

-- MAGIC %md-sandbox
-- MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
-- MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
-- MAGIC <br/>
-- MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
