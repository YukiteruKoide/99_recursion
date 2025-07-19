# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-b6890eab-5e31-49be-88c7-792f32f49a23
# MAGIC %md
# MAGIC # Databricks プラントフォーム (Databricks Platform)
# MAGIC
# MAGIC 基本的な機能を学び、Databricks ワークスペースでの作業に関連する用語を把握します。
# MAGIC
# MAGIC ##### 目的 (Objectives)
# MAGIC 1. 複数の言語でコードを実行
# MAGIC 1. ドキュメントセルの作成
# MAGIC 1. DBFS（Databricks File System）へのアクセス
# MAGIC 1. データベースとテーブルの作成
# MAGIC 1. テーブルへのクエリと結果のプロット
# MAGIC 1. ウィジェットでノートブックのパラメータを追加
# MAGIC
# MAGIC ##### Databricks ノートブック ユーティリティー (Databricks Notebook Utilities)
# MAGIC - <a href="https://docs.databricks.com/notebooks/notebooks-use.html#language-magic" target="_blank">マジックコマンド</a>: **`%python`**, **`%scala`**, **`%sql`**, **`%r`**, **`%sh`**, **`%md`**
# MAGIC - <a href="https://docs.databricks.com/dev-tools/databricks-utils.html" target="_blank">ユーティリティ</a>: **`dbutils.fs`** (**`%fs`**), **`dbutils.notebooks`** (**`%run`**), **`dbutils.widgets`**
# MAGIC - <a href="https://docs.databricks.com/notebooks/visualizations/index.html" target="_blank">ビジュアライゼーション</a>: **`display`**, **`displayHTML`**

# COMMAND ----------

# DBTITLE 0,--i18n-763aac82-c507-44e0-b2a7-f5ebd42cb64c
# MAGIC %md
# MAGIC ### セットアップ (Setup)
# MAGIC Databricksのトレーニングデータセットを<a href="https://docs.databricks.com/data/databricks-file-system.html#mount-storage" target="_blank">マウント</a>し、BedBricks用のデータベースを作成するためにクラスのセットアップを実行します。
# MAGIC
# MAGIC ノートブック内の別のノートブックを実行するために **`%run`** マジックコマンドを使用します。

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-d4b5cfdc-1842-4c68-983a-600956e46644
# MAGIC %md
# MAGIC ### 複数の言語でコードを実行 (Execute code in multiple languages)
# MAGIC ノートブックのデフォルト言語のコードを実行します。

# COMMAND ----------

print("Run default language")

# COMMAND ----------

# DBTITLE 0,--i18n-866eea11-4467-4192-8263-79510da3966d
# MAGIC %md
# MAGIC 言語のマジックコマンドで指定した言語のコードを実行します: **`%python`**, **`%scala`**, **`%sql`**, **`%r`**

# COMMAND ----------

print("Run python")

# COMMAND ----------

# MAGIC %scala
# MAGIC println("Run scala")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Run SQL"

# COMMAND ----------

# MAGIC %r
# MAGIC print("Run R", quote=FALSE)

# COMMAND ----------

# DBTITLE 0,--i18n-905f4010-a884-4d3d-a84e-6cdc5b3ea493
# MAGIC %md
# MAGIC マジックコマンド **`%sh`** を使ってシェルコマンドを実行します。

# COMMAND ----------

# MAGIC %sh ps | grep 'java'

# COMMAND ----------

# DBTITLE 0,--i18n-0a5ea494-a63c-4ea8-b0d9-d374dc1ebb2f
# MAGIC %md
# MAGIC 関数 **`displayHTML`** を使ってHTMLをレンダリングします。 (Python、Scala、Rで利用可能)

# COMMAND ----------

html = """<h1 style="color:orange;text-align:center;font-family:Courier">Render HTML</h1>"""
displayHTML(html)

# COMMAND ----------

# DBTITLE 0,--i18n-03da2bfd-0e21-4650-9a80-97bbfd6b5b4f
# MAGIC %md
# MAGIC ## ドキュメントセルの作成 (Create documentation cells)
# MAGIC
# MAGIC マジックコマンド **`%md`** を使用して、<a href="https://www.markdownguide.org/cheat-sheet/" target="_blank">Markdown</a>としてセルをレンダリングします。
# MAGIC
# MAGIC 以下は、Markdownを使用してドキュメントをフォーマットする方法の例です。このセルをクリックして **`Enter`** を押すと、Markdown構文が表示されます。
# MAGIC
# MAGIC
# MAGIC # 見出し 1 
# MAGIC ### 見出し 3
# MAGIC > 引用
# MAGIC
# MAGIC 1. **太字**
# MAGIC 2. *斜体*
# MAGIC 3. ~~取り消し線~~
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC - <a href="https://www.markdownguide.org/cheat-sheet/" target="_blank">リンク</a>
# MAGIC - `コード`
# MAGIC
# MAGIC ```
# MAGIC {
# MAGIC   "message": "これはコードブロックです",
# MAGIC   "method": "https://www.markdownguide.org/extended-syntax/#fenced-code-blocks",
# MAGIC   "alternative": "https://www.markdownguide.org/basic-syntax/#code-blocks"
# MAGIC }
# MAGIC ```
# MAGIC
# MAGIC ![Spark Logo](https://files.training.databricks.com/images/Apache-Spark-Logo_TM_200px.png)
# MAGIC
# MAGIC | 要素 | Markdown構文 |
# MAGIC |-----------------|-----------------|
# MAGIC | 見出し        | `#H1` `##H2` `###H3` `#### H4` `##### H5` `###### H6` |
# MAGIC | 引用     | `> 引用` |
# MAGIC | 太字            | `**太字**` |
# MAGIC | 斜体          | `*斜体*` |
# MAGIC | 取り消し線   | `~~取り消し線~~` |
# MAGIC | 水平線 | `---` |
# MAGIC | コード            | ``` `コード` ``` |
# MAGIC | リンク            | `[text](https://www.example.com)` |
# MAGIC | 画像           | `[alt text](image.jpg)`|
# MAGIC | 番号付きリスト    | `1.第１項目` <br> `2.第２項目` <br> `3.第３項目` |
# MAGIC | 箇条書きリスト  | `- 第１項目` <br> `- 第２項目` <br> `- 第３項目` |
# MAGIC | コードブロック      | ```` ``` ```` <br> `コードブロック` <br> ```` ``` ````|
# MAGIC | テーブル           |<code> &#124; col &#124; col &#124; col &#124; </code> <br> <code> &#124;---&#124;---&#124;---&#124; </code> <br> <code> &#124; val &#124; val &#124; val &#124; </code> <br> <code> &#124; val &#124; val &#124; val &#124; </code> <br>|

# COMMAND ----------

# DBTITLE 0,--i18n-55bcf039-68d2-4600-ab33-3b68e17cde20
# MAGIC %md
# MAGIC ## DBFS（Databricks File System）へのアクセス (Access DBFS (Databricks File System))
# MAGIC
# MAGIC <a href="https://docs.databricks.com/data/databricks-file-system.html" target="_blank">Databricks File System</a> (DBFS)
# MAGIC は、クラウド オブジェクト ストレージをクラスター上のローカル ファイルおよびディレクトリであるように扱うことができる仮想ファイル システムです。
# MAGIC
# MAGIC マジックコマンド **`%fs`** を使ってDBFS上でファイルシステムコマンドを実行します。
# MAGIC
# MAGIC
# MAGIC <br/>
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_24.png"/>
# MAGIC 下のセルの <strong>FILL_IN</strong> をあなたのメールアドレスに置換してください。

# COMMAND ----------

# MAGIC %fs mounts

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %fs ls dbfs:/tmp

# COMMAND ----------

# MAGIC %fs put dbfs:/tmp/FILL_IN.txt "This is a test of the emergency broadcast system, this is only a test" --overwrite=true

# COMMAND ----------

# MAGIC %fs head dbfs:/tmp/FILL_IN.txt

# COMMAND ----------

# MAGIC %fs ls dbfs:/tmp

# COMMAND ----------

# DBTITLE 0,--i18n-c1a4308d-ee83-4d09-8609-dbf74129c47a
# MAGIC %md
# MAGIC **`%fs`** は <a href="https://docs.databricks.com/dev-tools/databricks-utils.html" target="_blank">DBUtils</a> モジュール **`dbutils.fs`** の略です。

# COMMAND ----------

# MAGIC %fs help

# COMMAND ----------

# DBTITLE 0,--i18n-d096dd27-4253-4242-b882-241a251413d1
# MAGIC %md
# MAGIC Databricks ユーティリティ を直接使用して DBFS 上でファイルシステムコマンドを実行します。

# COMMAND ----------

dbutils.fs.ls("dbfs:/tmp")

# COMMAND ----------

# DBTITLE 0,--i18n-df97995d-6355-4002-adf0-8e27da62ad89
# MAGIC %md
# MAGIC Databricks <a href="https://docs.databricks.com/notebooks/visualizations/index.html#display-function-1" target="_blank">display</a>関数を使ってテーブルの結果を可視化します。

# COMMAND ----------

files = dbutils.fs.ls("dbfs:/tmp")
display(files)

# COMMAND ----------

# DBTITLE 0,--i18n-786321eb-dac1-4fb3-9a1b-e4f6be665b05
# MAGIC %md
# MAGIC 一時ファイルをもう一度見てみましょう...

# COMMAND ----------

file_name = "dbfs:/tmp/FILL_IN.txt"
contents = dbutils.fs.head(file_name)

print("-"*80)
print(contents)
print("-"*80)

# COMMAND ----------

# DBTITLE 0,--i18n-da682b0a-785c-4fbb-998c-9735849e5d66
# MAGIC %md
# MAGIC ## 一つ目のテーブル (Our First Table)
# MAGIC
# MAGIC は **`DA.paths.events`** (事前準備した変数)パスに存在しています。
# MAGIC 下のセルを実行してファイルを確認することができます。

# COMMAND ----------

files = dbutils.fs.ls(DA.paths.events)
display(files)

# COMMAND ----------

# DBTITLE 0,--i18n-fe760001-4ad5-4875-9908-0d2621b2b379
# MAGIC %md
# MAGIC ## でも、ちょっと待って！
# MAGIC
# MAGIC SQLコマンドでPython変数を使用できません。
# MAGIC
# MAGIC 次のトリックでできます！
# MAGIC
# MAGIC Python変数を、SQLコマンドがアクセスできるsparkコンテキストの変数として宣言します。

# COMMAND ----------

spark.conf.set("whatever.events", DA.paths.events)

# COMMAND ----------

# DBTITLE 0,--i18n-9f524915-58be-49e0-b62e-948eac9a57f4
# MAGIC %md
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_24.png"> 
# MAGIC
# MAGIC 上記の例では、誤って他の構成パラメーターを使用しないようにするため、 **`whatever.`** という変数の「名前空間」を与えています。
# MAGIC
# MAGIC **`DA.paths.some_file`** のように、このコース全体を通して、「DA」名前空間を使用しています。

# COMMAND ----------

# DBTITLE 0,--i18n-cc9fe8d7-8380-4412-8e71-0ca40c8849c6
# MAGIC %md
# MAGIC ## テーブルを作成　(Create table)
# MAGIC <a href="https://docs.databricks.com/spark/latest/spark-sql/language-manual/index.html#sql-reference" target="_blank">Databricks SQLコマンド</a>を実行して、DBFS上のBedBricksイベントファイルを使用して **`events`** というテーブルを作成します。

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS events
# MAGIC USING DELTA
# MAGIC OPTIONS (path = "${whatever.events}");

# COMMAND ----------

# DBTITLE 0,--i18n-c5a68136-0804-4ca0-bffb-a42ee61674f6
# MAGIC %md
# MAGIC このテーブルは、クラスの設定で作成したデータベースに保存されています。
# MAGIC
# MAGIC 以下に表示されたデータベース名を確認してください。

# COMMAND ----------

print(f"Database Name: {DA.schema_name}")

# COMMAND ----------

# DBTITLE 0,--i18n-48ad8e5e-247a-494e-90ea-b794075c34d6
# MAGIC %md
# MAGIC ... データベースのテーブルを確認してください。

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN ${DA.schema_name}

# COMMAND ----------

# DBTITLE 0,--i18n-943bbcdc-07b1-4ef1-b6b3-964aee4cd396
# MAGIC %md
# MAGIC UIの`Data`タブでデータベースとテーブルを表示してください。

# COMMAND ----------

# DBTITLE 0,--i18n-8a01566b-882e-431e-bb33-faee48cccef0
# MAGIC %md
# MAGIC ## テーブルへのクエリと結果のプロット (Query table and plot results)
# MAGIC SQLを使用して **`events`** テーブルにクエリを実行します。

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM events

# COMMAND ----------

# DBTITLE 0,--i18n-0ccc0218-d091-4ab5-bb0e-bfa40bbfa541
# MAGIC %md
# MAGIC 以下のクエリを実行し、(+)サインをクリックして可視化を選択します。棒グラフで結果を<a href="https://docs.databricks.com/notebooks/visualizations/index.html#plot-types" target="_blank">プロット</a>して保存します。

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT traffic_source, SUM(ecommerce.purchase_revenue_in_usd) AS total_revenue
# MAGIC FROM events
# MAGIC GROUP BY traffic_source

# COMMAND ----------

# DBTITLE 0,--i18n-422a57bc-d416-4b62-813c-d2e9fe39b36f
# MAGIC %md
# MAGIC ## ウィジェットでノートブックのパラメータを追加 (Add notebook parameters with widgets)
# MAGIC <a href="https://docs.databricks.com/notebooks/widgets.html" target="_blank">ウィジェット</a>を使用して、ノートブックに入力パラメータを追加します。
# MAGIC
# MAGIC SQLを使用してテキスト入力ウィジェットを作成します。

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE WIDGET TEXT state DEFAULT "CA"

# COMMAND ----------

# DBTITLE 0,--i18n-a397f179-d832-47dd-8b5c-c955bd2a1a39
# MAGIC %md
# MAGIC **`getArgument`** 関数を用いてウィジェットの現在の値に取得します。

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM events
# MAGIC WHERE geo.state = getArgument("state")

# COMMAND ----------

# DBTITLE 0,--i18n-463810ae-8c7e-4551-9383-27757387a49e
# MAGIC %md
# MAGIC テキストウィジェットを削除。

# COMMAND ----------

# MAGIC %sql
# MAGIC REMOVE WIDGET state

# COMMAND ----------

# DBTITLE 0,--i18n-4b96b453-7c54-4dec-8099-f53fff57305d
# MAGIC %md
# MAGIC Python、Scala、Rでウィジェットを作成するには、DBUtilsモジュールの **`dbutils.widgets`** を使用します。

# COMMAND ----------

dbutils.widgets.text("name", "Brickster", "Name")
dbutils.widgets.multiselect("colors", "orange", ["red", "orange", "black", "blue"], "Favorite Color?")

# COMMAND ----------

# DBTITLE 0,--i18n-e7c70df9-70a2-4017-8725-0f6e255184b4
# MAGIC %md
# MAGIC ウィジェットの現在の値にアクセスするには、 **`dbutils.widgets`** の関数 **`get`** を使用します。

# COMMAND ----------

name = dbutils.widgets.get("name")
colors = dbutils.widgets.get("colors").split(",")

html = "<div>Hi {}! Select your color preference.</div>".format(name)
for c in colors:
    html += """<label for="{}" style="color:{}"><input type="radio"> {}</label><br>""".format(c, c, c)

displayHTML(html)

# COMMAND ----------

# DBTITLE 0,--i18n-c0cea1c1-bad1-4a9a-bbaf-3bc39cd7ae75
# MAGIC %md
# MAGIC すべてのウィジェットを削除します。

# COMMAND ----------

dbutils.widgets.removeAll()

# COMMAND ----------

# DBTITLE 0,--i18n-dd02334a-23bf-49e5-8147-66984d8892dd
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
