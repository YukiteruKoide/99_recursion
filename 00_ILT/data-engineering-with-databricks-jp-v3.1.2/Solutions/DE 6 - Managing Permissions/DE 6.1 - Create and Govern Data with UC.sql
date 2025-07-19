-- Databricks notebook source
-- MAGIC %md-sandbox
-- MAGIC
-- MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
-- MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
-- MAGIC </div>
-- MAGIC

-- COMMAND ----------

-- DBTITLE 0,--i18n-b5d0b5d6-287e-4dcd-8a4b-a0fe2b12b615
-- MAGIC %md
-- MAGIC # Unity Catalog を使用してデータ オブジェクトを作成および管理する（Create and govern data objects with Unity Catalog）
-- MAGIC
-- MAGIC このノートブックでは、次の方法を学習します。
-- MAGIC * カタログ、スキーマ、テーブル、ビュー、およびユーザー定義関数を作成する
-- MAGIC * これらのオブジェクトへのアクセスを制御する
-- MAGIC * 動的ビューを使用してテーブル内の列と行を保護する
-- MAGIC * Unity Catalogでさまざまなオブジェクトの助成金を調べる

-- COMMAND ----------

-- DBTITLE 0,--i18n-63c92b27-28a0-41f8-8761-a9ec5bb574e0
-- MAGIC %md
-- MAGIC ## 前提条件（Prerequisites）
-- MAGIC
-- MAGIC このラボを続行するには、次のことを行う必要があります。
-- MAGIC * カタログを作成および管理するためのメタストア管理者権限を持っている
-- MAGIC * Databricks SQL アクセス権を持つ別のユーザーを含む *analysts* グループを作成する
-- MAGIC    * ノートブックを参照: Unity カタログでのプリンシパルの管理
-- MAGIC * 上記のユーザーがアクセスできる SQL ウェアハウスがある
-- MAGIC    * ノートブックを参照: Unity カタログ アクセス用のコンピューティング リソースの作成

-- COMMAND ----------

-- DBTITLE 0,--i18n-67495bbd-0f5b-4f81-9974-d5c6360fb86c
-- MAGIC %md
-- MAGIC ## 設定（Setup）
-- MAGIC
-- MAGIC 次のセルを実行して、セットアップを実行します。 共有トレーニング環境での競合を回避するために、これにより、お客様専用の一意のカタログ名が生成されます。これはまもなく採用されます。

-- COMMAND ----------

-- MAGIC %run ./Includes/Classroom-Setup-06.1

-- COMMAND ----------

-- DBTITLE 0,--i18n-a0720484-97de-4742-9c38-6c5bd312f3d7
-- MAGIC %md
-- MAGIC ## Unity Catalog の 3 レベルの名前空間（Unity Catalog's three-level namespace）
-- MAGIC
-- MAGIC 次のクエリ例に示すように、SQL の経験がある人なら誰でも、次のようにスキーマ内のテーブルまたはビューをアドレス指定するための従来の 2 レベルの名前空間に精通している可能性があります。
-- MAGIC
-- MAGIC      SELECT * FROM myschema.mytable;
-- MAGIC
-- MAGIC Unity Catalog は、**カタログ** の概念を階層に導入します。 カタログは、スキーマのコンテナーとして、組織がデータを分離するための新しい方法を提供します。 カタログは好きなだけ作成でき、スキーマは好きなだけ含めることができます (**スキーマ**の概念は Unity カタログでは変更されていません。スキーマには、テーブル、ビュー、ユーザー定義関数などのデータオブジェクトが含まれます)。
-- MAGIC
-- MAGIC この追加レベルに対処するために、Unity Catalog の完全なテーブル/ビュー参照は 3 レベルの名前空間を使用します。 次のクエリはこれを示しています。
-- MAGIC
-- MAGIC      SELECT * FROM mycatalog.myschema.mytable;
-- MAGIC
-- MAGIC これは、多くのユースケースで便利です。 例えば：
-- MAGIC
-- MAGIC * 組織内のビジネス ユニットに関連するデータの分離 (販売、マーケティング、人事など)
-- MAGIC * SDLC 要件を満たす (開発、ステージング、製品など)
-- MAGIC * 内部使用のための一時的なデータセットを含むサンドボックスの確立

-- COMMAND ----------

-- DBTITLE 0,--i18n-aa4c68dc-6dc3-4aca-a352-affc98ac8089
-- MAGIC %md
-- MAGIC ### 新しいカタログを作成する
-- MAGIC メタストアに新しいカタログを作成しましょう。 変数 **`${DA.my_new_catalog}`** は、上記のセットアップ セルによって表示され、ユーザー名に基づいて生成された一意の文字列を含みます。
-- MAGIC
-- MAGIC 以下の **`CREATE`** ステートメントを実行し、左側のサイドバーにある **データ** アイコンをクリックして、この新しいカタログが作成されたことを確認します。

-- COMMAND ----------

CREATE CATALOG IF NOT EXISTS ${DA.my_new_catalog}

-- COMMAND ----------

-- DBTITLE 0,--i18n-e1f478c8-bbf2-4368-9cdd-e130d2fb7410
-- MAGIC %md
-- MAGIC ### デフォルトのカタログを選択
-- MAGIC
-- MAGIC SQL 開発者は、デフォルト スキーマを選択するための **`USE`** ステートメントにも精通しているでしょう。これにより、常にスキーマを指定する必要がなくなり、クエリが短縮されます。 名前空間の余分なレベルを処理しながらこの利便性を拡張するために、Unity Catalog は、以下の例に示すように、2 つのステートメントを追加して言語を拡張します。
-- MAGIC
-- MAGIC      USE CATALOG mycatalog;
-- MAGIC      USE SCHEMA myschema;
-- MAGIC     
-- MAGIC 新しく作成したカタログをデフォルトとして選択しましょう。 これで、カタログ参照によって明示的にオーバーライドされない限り、すべてのスキーマ参照がこのカタログにあると見なされます。

-- COMMAND ----------

USE CATALOG ${DA.my_new_catalog}

-- COMMAND ----------

-- DBTITLE 0,--i18n-bc4ad8ed-6550-4457-92f7-d88d22709b3c
-- MAGIC %md
-- MAGIC ### 新しいスキーマを作成して使用する
-- MAGIC 次に、この新しいカタログにスキーマを作成しましょう。 残りのメタストアから分離された一意のカタログを使用しているため、このスキーマに別の一意の名前を生成する必要はありません。 これもデフォルトのスキーマとして設定しましょう。 これで、2 レベルまたは 3 レベルの参照によって明示的に上書きされない限り、すべてのデータ参照は、作成したカタログとスキーマにあると見なされます。
-- MAGIC
-- MAGIC 以下のコードを実行し、左側のサイドバーにある **データ** アイコンをクリックして、作成した新しいカタログにこのスキーマが作成されたことを確認します。

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS example;
USE SCHEMA example

-- COMMAND ----------

-- DBTITLE 0,--i18n-87b6328c-4641-4d40-b66c-f166a4166902
-- MAGIC %md
-- MAGIC ### テーブルとビューを設定する
-- MAGIC
-- MAGIC 必要なコンテナをすべて配置したら、テーブルとビューを設定しましょう。 この例では、模擬データを使用して、心拍数データを含む *silver* 管理テーブルと毎日の患者ごとの心拍数データを平均する *gold* ビューを作成します。
-- MAGIC
-- MAGIC 以下のセルを実行し、左側のサイドバーにある **データ** アイコンをクリックして、**example** スキーマの内容を調べます。 デフォルトのカタログとスキーマを指定したため、以下のテーブルまたはビューの名前を指定するときに 3 つのレベルを指定する必要がないことに留意してください。

-- COMMAND ----------

CREATE OR REPLACE TABLE heartrate_device (device_id INT, mrn STRING, name STRING, time TIMESTAMP, heartrate DOUBLE);

INSERT INTO heartrate_device VALUES
  (23, "40580129", "Nicholas Spears", "2020-02-01T00:01:58.000+0000", 54.0122153343),
  (17, "52804177", "Lynn Russell", "2020-02-01T00:02:55.000+0000", 92.5136468131),
  (37, "65300842", "Samuel Hughes", "2020-02-01T00:08:58.000+0000", 52.1354807863),
  (23, "40580129", "Nicholas Spears", "2020-02-01T00:16:51.000+0000", 54.6477014191),
  (17, "52804177", "Lynn Russell", "2020-02-01T00:18:08.000+0000", 95.033344842);
  
SELECT * FROM heartrate_device

-- COMMAND ----------

CREATE OR REPLACE VIEW agg_heartrate AS (
  SELECT mrn, name, MEAN(heartrate) avg_heartrate, DATE_TRUNC("DD", time) date
  FROM heartrate_device
  GROUP BY mrn, name, DATE_TRUNC("DD", time)
);
SELECT * FROM agg_heartrate

-- COMMAND ----------

-- DBTITLE 0,--i18n-3ab35bc3-e89b-48d0-bcef-91a268688a19
-- MAGIC %md
-- MAGIC 私たちがデータ所有者であるため、上記のテーブルのクエリは期待どおりに機能します。 つまり、クエリしているデータ オブジェクトの所有権を持っています。 ビューとそれが参照しているテーブルの両方の所有者であるため、ビューのクエリも機能します。 したがって、これらのリソースにアクセスするためにオブジェクト レベルの権限は必要ありません。

-- COMMAND ----------

-- DBTITLE 0,--i18n-9ce42a62-c95a-45fb-9d6b-a4d3725110e7
-- MAGIC %md
-- MAGIC ## _Analysts_ グループを作成する（Create the _Analysts_ Group）
-- MAGIC
-- MAGIC 特定のユーザー グループにアクセスを許可するには、そのグループを作成し、アクセス許可レベルを設定する必要があります。 これを行うには、ワークスペースへの管理者アクセスが必要です。

-- COMMAND ----------

-- DBTITLE 0,--i18n-29eeb0ee-94e0-4b95-95be-a8776d20dc6c
-- MAGIC %md
-- MAGIC ## データオブジェクトへのアクセスを許可する（Grant access to data objects）
-- MAGIC
-- MAGIC Unity カタログは、デフォルトで明示的な権限管理モデルを採用しています。 含まれている要素から権限が暗示または継承されることはありません。 したがって、データ オブジェクトにアクセスするには、含まれるすべての要素に対する **USAGE** 権限が必要です。 つまり、含まれているスキーマとカタログです。
-- MAGIC
-- MAGIC *analysts* グループのメンバーが *gold* ビューを照会できるようにしましょう。 これを行うには、次の権限を付与する必要があります。
-- MAGIC 1. カタログとスキーマの USAGE
-- MAGIC 1. データオブジェクト (ビューなど) に対する SELECT

-- COMMAND ----------

-- GRANT USAGE ON CATALOG ${DA.my_new_catalog} TO analysts;
-- GRANT USAGE ON SCHEMA example TO analysts;
-- GRANT SELECT ON VIEW agg_heartrate to analysts

-- COMMAND ----------

-- DBTITLE 0,--i18n-dabadee1-5624-4330-855d-d0c0de1f76b4
-- MAGIC %md
-- MAGIC ### アナリストとしてビューをクエリする
-- MAGIC
-- MAGIC データ オブジェクト階層とすべての適切な許可が整ったら、別のユーザーとして *gold* ビューでクエリを実行してみましょう。 このラボの **前提条件** セクションで、別のユーザーを含む *analysts* というグループがあることについて言及したことを思い出してください。
-- MAGIC
-- MAGIC このセクションでは、そのユーザーとしてクエリを実行して構成を確認し、変更を加えたときの影響を観察します。
-- MAGIC
-- MAGIC このセクションの準備として、**別のブラウザー セッションを使用して Databricks にログインする必要があります**。 これは、プライベート セッション、ブラウザーがプロファイルをサポートしている場合は別のプロファイル、またはまったく別のブラウザーである可能性があります。 ログインの競合が発生するため、同じブラウザ セッションを使用して単に新しいタブまたはウィンドウを開かないでください。
-- MAGIC
-- MAGIC 1. 別のブラウザー セッションで、アナリスト ユーザー資格情報を使用してクラスルーム ワークスペースにログインします。
-- MAGIC 1. **SQL** ペルソナに切り替えます。
-- MAGIC 1. **クエリ** ページに移動し、**クエリの作成** をクリックします。
-- MAGIC 1. *Unity Catalog アクセス用のコンピューティング リソースの作成* デモに従って作成した共有 SQL ウェアハウスを選択します。
-- MAGIC 1. このノートに戻って、続きを読み進めてください。 プロンプトが表示されたら、Databricks SQL セッションに切り替えてクエリを実行します。
-- MAGIC
-- MAGIC 次のセルは、ビューの 3 つのレベルすべてを指定する完全修飾クエリ ステートメントを生成します。これは、変数または既定のカタログとスキーマがセットアップされていない環境で実行するためです。 以下で生成されたクエリを Databricks SQL セッションで実行します。 アナリストがビューにアクセスするためのすべての適切な権限が設定されているため、出力は以前に *gold* ビューをクエリしたときに見たものと同じはずです。

-- COMMAND ----------

SELECT "SELECT * FROM ${DA.my_new_catalog}.example.agg_heartrate" AS Query

-- COMMAND ----------

-- DBTITLE 0,--i18n-7fb51344-7eb4-49a2-916c-6cdee06e534a
-- MAGIC %md
-- MAGIC ### アナリストとしてテーブルをクエリする
-- MAGIC Databricks SQL セッションの同じクエリに戻り、*gold* を *silver* に置き換えて、クエリを実行しましょう。 *silver* テーブルに権限を設定していないため、今回は失敗します。
-- MAGIC
-- MAGIC ビューによって表されるクエリは、基本的にビューの所有者として実行されるため、*gold* のクエリは機能します。 この重要なプロパティにより、いくつかの興味深いセキュリティ ユース ケースが可能になります。 このように、ビューは、基になるデータ自体へのアクセスを提供することなく、機密データの制限されたビューをユーザーに提供できます。 これについては後ほど詳しく説明します。
-- MAGIC
-- MAGIC 現時点では、Databricks SQL セッションで *silver* クエリを閉じて破棄できます。これはもう使用しないためです。

-- COMMAND ----------

-- DBTITLE 0,--i18n-bea5cb66-3642-45b1-8906-906588b99b06
-- MAGIC %md
-- MAGIC ### ユーザー定義関数を作成してアクセスを許可する
-- MAGIC
-- MAGIC Unity Catalog は、スキーマ内のユーザー定義関数も管理できます。 以下のコードは、文字列の最後の 2 文字を除くすべてをマスクする単純な関数を設定し、それを試します。 繰り返しますが、私たちはデータの所有者であるため、許可は必要ありません。

-- COMMAND ----------

CREATE OR REPLACE FUNCTION mask(x STRING)
  RETURNS STRING
  RETURN CONCAT(REPEAT("*", LENGTH(x) - 2), RIGHT(x, 2)
); 
SELECT mask('sensitive data') AS data

-- COMMAND ----------

-- DBTITLE 0,--i18n-d0945f12-4045-471b-a319-376f5f8f25dd
-- MAGIC %md
-- MAGIC *analysts* グループのメンバーが関数を実行できるようにするには、関数で **EXECUTE** が必要であり、前述のスキーマとカタログで必要な **USAGE** 権限も必要です。

-- COMMAND ----------

-- GRANT EXECUTE ON FUNCTION mask to analysts

-- COMMAND ----------

-- DBTITLE 0,--i18n-e74e14a8-d372-44e0-a301-94cc046efd29
-- MAGIC %md
-- MAGIC ### アナリストとして関数を実行する
-- MAGIC
-- MAGIC 次に、Databricks SQL セッションでアナリストとして関数を試します。 以下で生成されたクエリ ステートメントを新しいクエリに貼り付けて、Databricks SQL セッションでこの関数を実行します。 アナリストが関数にアクセスするための適切な許可がすべて設定されているため、出力は上記のようなものになるはずです。

-- COMMAND ----------

SELECT "SELECT ${DA.my_new_catalog}.example.mask('sensitive data') AS data" AS Query

-- COMMAND ----------

-- DBTITLE 0,--i18n-8697f10a-6924-4bac-9c9a-7d91285eb9f5
-- MAGIC %md
-- MAGIC ## 動的ビューでテーブルの列と行を保護する(Protect table columns and rows with dynamic views)
-- MAGIC
-- MAGIC Unity Catalog のビューの処理により、ビューがテーブルへのアクセスを保護できることがわかりました。 ユーザーは、ソース テーブルに直接アクセスしなくても、ソース テーブルのデータを操作、変換、または非表示にするビューへのアクセスを許可されます。
-- MAGIC
-- MAGIC 動的ビューは、クエリを実行するプリンシパルを条件として、テーブル内の列と行のきめ細かいアクセス制御を行う機能を提供します。 動的ビューは、次のようなことを可能にする標準ビューの拡張です。
-- MAGIC * 列の値を部分的に隠すか、完全に編集する
-- MAGIC * 特定の基準に基づく行の省略
-- MAGIC
-- MAGIC 動的ビューによるアクセス制御は、ビューの定義内で関数を使用することによって実現されます。 これらの機能には次のものがあります。
-- MAGIC * **`current_user()`**: ビューをクエリしているユーザーの電子メール アドレスを返します
-- MAGIC * **`is_account_group_member()`**: ビューをクエリしているユーザーが指定されたグループのメンバーである場合に TRUE を返します
-- MAGIC
-- MAGIC 注: ワークスペース レベルのグループを参照する従来の関数 **`is_member()`** の使用は控えてください。 これは、Unity Catalog のコンテキストでは適切な方法ではありません。

-- COMMAND ----------

-- DBTITLE 0,--i18n-8fc52e53-927e-4d6b-a340-7082c94d4e6e
-- MAGIC %md
-- MAGIC ### 列を編集する
-- MAGIC
-- MAGIC アナリストが *gold* ビューから集計されたデータの傾向を確認できるようにしたいが、患者の PII を開示したくないとします。 **`is_account_group_member()`** を使用して *mrn* 列と *name* 列を編集するビューを再定義しましょう。
-- MAGIC
-- MAGIC 注: これは単純なトレーニングの例であり、必ずしも一般的なベスト プラクティスと一致するとは限りません。 本番システムの場合、より安全な方法は、特定のグループのメンバーではないすべてのユーザーの列の値を編集することです。

-- COMMAND ----------

CREATE OR REPLACE VIEW agg_heartrate AS
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
  FROM heartrate_device
  GROUP BY mrn, name, DATE_TRUNC("DD", time)

-- COMMAND ----------

-- DBTITLE 0,--i18n-01381247-0c36-455b-b64c-22df863d9926
-- MAGIC %md
-- MAGIC 許可付与を再発行してください。

-- COMMAND ----------

-- GRANT SELECT ON VIEW agg_heartrate to analysts

-- COMMAND ----------

-- DBTITLE 0,--i18n-a73f7b38-cacb-4a29-afde-ce4f34ace640
-- MAGIC %md
-- MAGIC ビューをクエリしてみましょう。

-- COMMAND ----------

SELECT * FROM agg_heartrate

-- COMMAND ----------

-- DBTITLE 0,--i18n-0bf9bd34-2351-492c-b6ef-e48241339d0f
-- MAGIC %md
-- MAGIC 私たちにとっては、*analysts* グループのメンバーではないため、フィルタリングされていない出力が得られます。
-- MAGIC
-- MAGIC 次に、Databricks SQL セッションに戻り、アナリストとして *gold* ビューでクエリを再実行します。 以下のセルを実行して、このクエリを生成します。
-- MAGIC
-- MAGIC *mrn* および *name* 列の値が編集されていることがわかります。

-- COMMAND ----------

SELECT "SELECT * FROM ${DA.my_new_catalog}.example.agg_heartrate" AS Query

-- COMMAND ----------

-- DBTITLE 0,--i18n-0bb3c639-daf8-4b46-9c28-cafd32a12917
-- MAGIC %md
-- MAGIC ### 行を制限する
-- MAGIC
-- MAGIC ここで、列を集約してマスクするのではなく、単にソースから行を除外するビューが必要だとします。 同じ **`is_account_group_member()`** 関数を適用して、*device_id* が 30 未満の行のみを通過するビューを作成してみましょう。行のフィルタリングは、**`WHERE`** 句として条件を適用することによって行われます。 .

-- COMMAND ----------

CREATE OR REPLACE VIEW agg_heartrate AS
SELECT
  mrn,
  time,
  device_id,
  heartrate
FROM heartrate_device
WHERE
  CASE WHEN
    is_account_group_member('analysts') THEN device_id < 30
    ELSE TRUE
  END

-- COMMAND ----------

-- DBTITLE 0,--i18n-69bc283c-f426-4ba2-b296-346c69de1c20
-- MAGIC %md
-- MAGIC 権限の付与を再発行します。

-- COMMAND ----------

-- GRANT SELECT ON VIEW agg_heartrate to analysts

-- COMMAND ----------

SELECT * FROM agg_heartrate

-- COMMAND ----------

-- DBTITLE 0,--i18n-c4f3366a-4992-4d5a-b597-e140091a8d00
-- MAGIC %md
-- MAGIC 私たちにとって、これは 5 つのレコードすべてを表示します。 次に、Databricks SQL セッションに戻り、アナリストとして *gold* ビューでクエリを再実行します。 レコードの 1 つが欠落していることがわかります。 欠落しているレコードには、フィルターによってキャッチされた *device_id* の値が含まれていました。

-- COMMAND ----------

-- DBTITLE 0,--i18n-dffccf13-5205-44d5-beab-4d08b085f54a
-- MAGIC %md
-- MAGIC ### データマスキング
-- MAGIC
-- MAGIC 動的ビューの最後の使用例の 1 つは、データのマスキング、またはデータの部分的な隠蔽です。 最初の例では、列を完全にマスクしました。 データを完全に置き換えるのではなく、データの一部を表示することを除いて、マスキングは原理的には似ています。 この単純な例では、以前に作成した *mask()* ユーザー定義関数を利用して、アナリスト用に *mrn* 列をマスクしますが、SQL はデフォルトの関数にかなり便利なライブラリを提供します。 さまざまな方法でデータをマスクできます。 可能な場合はそれらを活用することをお勧めします。

-- COMMAND ----------

CREATE OR REPLACE VIEW agg_heartrate AS
SELECT
  CASE WHEN
    is_account_group_member('analysts') THEN mask(mrn)
    ELSE mrn
  END AS mrn,
  time,
  device_id,
  heartrate
FROM heartrate_device
WHERE
  CASE WHEN
    is_account_group_member('analysts') THEN device_id < 30
    ELSE TRUE
  END

-- COMMAND ----------

-- DBTITLE 0,--i18n-735fa71c-0d31-4484-9736-30dc098dee8d
-- MAGIC %md
-- MAGIC Re-issue the grant.

-- COMMAND ----------

-- GRANT SELECT ON VIEW agg_heartrate to analysts

-- COMMAND ----------

SELECT * FROM agg_heartrate

-- COMMAND ----------

-- DBTITLE 0,--i18n-9c3d9b8f-17ce-498f-b6dd-dfb470855086
-- MAGIC %md
-- MAGIC 私たちにとって、これは元のレコードをそのまま表示します。 次に、Databricks SQL セッションに戻り、アナリストとして *gold* ビューでクエリを再実行します。 *mrn* 列のすべての値がマスクされます。

-- COMMAND ----------

-- DBTITLE 0,--i18n-3e809063-ad1b-4a2e-8cc3-b87492c8ffc3
-- MAGIC %md
-- MAGIC ## オブジェクトを探索する(Explore objects)
-- MAGIC
-- MAGIC いくつかの SQL ステートメントを調べて、データ オブジェクトとアクセス許可を調べてみましょう。 *examples* スキーマにあるオブジェクトのストックを取ることから始めましょう。

-- COMMAND ----------

SHOW TABLES

-- COMMAND ----------

SHOW VIEWS

-- COMMAND ----------

-- DBTITLE 0,--i18n-40599e0f-47f9-46da-be2b-7b856da0cba1
-- MAGIC %md
-- MAGIC 上記の 2 つのステートメントでは、選択したデフォルトに依存しているため、スキーマを指定しませんでした。 別の方法として、**`SHOW TABLES IN example`** のようなステートメントを使用して、より明確にすることもできます。
-- MAGIC
-- MAGIC では、階層のレベルを上げて、カタログ内のスキーマのインベントリを作成してみましょう。 ここでも、デフォルトのカタログが選択されているという事実を利用しています。 もっと明確にしたい場合は、**`SHOW SCHEMAS IN ${DA.my_new_catalog}`** のようなものを使用できます。

-- COMMAND ----------

SHOW SCHEMAS

-- COMMAND ----------

-- DBTITLE 0,--i18n-943178c2-9ab3-4941-ac1a-70b63103ecb7
-- MAGIC %md
-- MAGIC もちろん、*example* スキーマは以前に作成したものです。 *default* スキーマは、新しいカタログを作成するときに、SQL 規則に従ってデフォルトで作成されます。
-- MAGIC
-- MAGIC 最後に、メタストア内のカタログを一覧表示しましょう。

-- COMMAND ----------

SHOW CATALOGS

-- COMMAND ----------

-- DBTITLE 0,--i18n-e8579147-7d9a-4b27-b0e9-3ab6c4ec9a0c
-- MAGIC %md
-- MAGIC 予想よりも多くのエントリがある可能性があります。 少なくとも、以下が表示されます。
-- MAGIC * 接頭辞 *dbacademy_* で始まるカタログ。これは前に作成したものです。
-- MAGIC * *hive_metastore* は、メタストア内の実際のカタログではなく、ワークスペースのローカル Hive メタストアの仮想表現です。 これを使用して、ワークスペース ローカル テーブルおよびビューにアクセスします。
-- MAGIC * *main*、新しいメタストアごとにデフォルトで作成されるカタログ。
-- MAGIC * *samples*、Databricks によって提供されるサンプル データセットを提示する別の仮想カタログ
-- MAGIC
-- MAGIC メタストアでの履歴アクティビティによっては、さらに多くのカタログが存在する場合があります。

-- COMMAND ----------

-- DBTITLE 0,--i18n-9477b0a2-3099-4fca-bb7d-f6e298ce254b
-- MAGIC %md
-- MAGIC ### アクセス許可を調べる（Explore permissions）
-- MAGIC
-- MAGIC **`SHOW GRANTS`** を使用してパーミッションを調べてみましょう。*gold* ビューから始めて上に向かって進んでいきます。

-- COMMAND ----------

-- SHOW GRANTS ON VIEW agg_heartrate

-- COMMAND ----------

-- DBTITLE 0,--i18n-98d1534e-a51c-45f6-83d0-b99549ccc279
-- MAGIC %md
-- MAGIC 現在、設定した **SELECT** 権限のみがあります。 では、*silver* の権限付与を確認してみましょう。

-- COMMAND ----------

-- SHOW GRANTS ON TABLE heartrate_device

-- COMMAND ----------

-- DBTITLE 0,--i18n-591b3fbb-7ed3-4e88-b435-3750b212521d
-- MAGIC %md
-- MAGIC 現在、このテーブルには許可がありません。 このテーブルに直接アクセスできるのは、データ所有者である私たちだけです。 私たちがデータ所有者なのでもちろんですが、*gold* ビューにアクセスする権限を持つ人は誰でもこのテーブルに間接的にアクセスできます。
-- MAGIC
-- MAGIC 次に、含まれているスキーマを見てみましょう。

-- COMMAND ----------

-- SHOW GRANTS ON SCHEMA example

-- COMMAND ----------

-- DBTITLE 0,--i18n-ab78d60b-a596-4a19-80ae-a5d742169b6c
-- MAGIC %md
-- MAGIC 今以前に設定した **USAGE** 許可が表示されます。
-- MAGIC
-- MAGIC では、カタログを見てみましょう。

-- COMMAND ----------

-- SHOW GRANTS ON CATALOG ${DA.my_new_catalog}

-- COMMAND ----------

-- DBTITLE 0,--i18n-62f7e069-7260-4a48-9676-16088958cffc
-- MAGIC %md
-- MAGIC 同様に、先ほど許可した **USAGE** が表示されます。

-- COMMAND ----------

-- DBTITLE 0,--i18n-200fe251-2176-46ca-8ecc-e725d8c9da01
-- MAGIC %md
-- MAGIC ## アクセス権を取り消す（Revoke access）
-- MAGIC
-- MAGIC 以前に発行された許可を取り消す機能がなければ、データ ガバナンス プラットフォームは完成しません。 *mask()* 関数へのアクセスを調べることから始めましょう。

-- COMMAND ----------

-- SHOW GRANTS ON FUNCTION mask

-- COMMAND ----------

-- DBTITLE 0,--i18n-9495b822-96bd-4fe5-aed7-9796ffd722d0
-- MAGIC %md
-- MAGIC それでは、この許可を取り消しましょう。

-- COMMAND ----------

-- REVOKE EXECUTE ON FUNCTION mask FROM analysts

-- COMMAND ----------

-- DBTITLE 0,--i18n-c599d523-08cc-4d39-994d-ce919799c276
-- MAGIC %md
-- MAGIC ここで、空になったアクセスをもう一度調べてみましょう。

-- COMMAND ----------

-- SHOW GRANTS ON FUNCTION mask

-- COMMAND ----------

-- DBTITLE 0,--i18n-a47d66a4-aa65-470b-b8ea-d8e7c29fce95
-- MAGIC %md
-- MAGIC Databricks SQL セッションに再度アクセスし、アナリストとして *gold* ビューに対してクエリを再実行します。 これは以前と同じように機能することに注意してください。 これはあなたを驚かせますか？ なぜですか、そうでないのですか？
-- MAGIC
-- MAGIC ビューはその所有者として効果的に実行されていることに注意してください。所有者はたまたま関数とソース テーブルも所有しています。 ビューの所有者がテーブルの所有権を持っているため、アナリストがクエリ対象のテーブルに直接アクセスする必要がなかったのと同じように、関数は同じ理由で引き続き機能します。
-- MAGIC
-- MAGIC では、別のことを試してみましょう。 カタログの **USAGE** を取り消して、アクセス許可の連鎖を断ち切りましょう。

-- COMMAND ----------

-- REVOKE USAGE ON CATALOG ${DA.my_new_catalog} FROM analysts

-- COMMAND ----------

-- DBTITLE 0,--i18n-b1483973-1ef7-4b6d-9a04-931c53947148
-- MAGIC %md
-- MAGIC Databricks SQL に戻り、アナリストとして *gold* クエリを再実行すると、ビューとスキーマに対する適切なアクセス許可があっても、階層の上位にある欠落している特権がこのリソースへのアクセスを中断することがわかります。 これは、Unity Catalog の明示的な権限管理モデルが実際に動作していることを示しています。管理権限は暗示または継承されません。

-- COMMAND ----------

-- DBTITLE 0,--i18n-1ffb00ac-7663-4206-84b6-448b50c0efe2
-- MAGIC %md
-- MAGIC ## 掃除（Clean up）
-- MAGIC
-- MAGIC 次のセルを実行して、以前に作成したカタログを削除しましょう。 **`CASCADE`** 修飾子は、含まれている要素とともにカタログを削除します。

-- COMMAND ----------

USE CATALOG hive_metastore;
DROP CATALOG IF EXISTS ${DA.my_new_catalog} CASCADE;

-- COMMAND ----------

-- MAGIC %python
-- MAGIC DA.cleanup()

-- COMMAND ----------

-- MAGIC %md-sandbox
-- MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
-- MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
-- MAGIC <br/>
-- MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
