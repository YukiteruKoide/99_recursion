# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-4e68432b-fcb4-473c-83dc-da733742ad49
# MAGIC %md
# MAGIC # Spark SQL
# MAGIC DataFrame API を使用して、Spark SQL の基本的な概念を把握します。
# MAGIC
# MAGIC ##### 目的 (Objectives)
# MAGIC 1. SQL クエリの実行
# MAGIC 1. テーブルからDataFrameを作成
# MAGIC 1. DataFrame変換により同等のクエリを書く
# MAGIC 1. DataFrame アクションを使用して計算の実行
# MAGIC 1. DataFramesとSQL間の変換
# MAGIC
# MAGIC ##### メソッド (Methods)
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/spark_session.html" target="_blank">SparkSession</a>: **`sql`**, **`table`**
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrame</a>:
# MAGIC   - 変換(Transformations):  **`select`**, **`where`**, **`orderBy`**
# MAGIC   - アクション(Actions): **`show`**, **`count`**, **`take`**
# MAGIC   - その他メソッド(Other methods): **`printSchema`**, **`schema`**, **`createOrReplaceTempView`**

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-SQL

# COMMAND ----------

# DBTITLE 0,--i18n-2b97b70b-d032-48cc-a86d-4bcc3bb53c25
# MAGIC %md
# MAGIC 複数のインターフェース
# MAGIC Spark SQL は、複数のインターフェイスを備えた構造化データ処理用のモジュールです。
# MAGIC
# MAGIC Spark SQL と対話するには、次の 2 つの方法があります。
# MAGIC 1. SQL クエリの実行
# MAGIC 1. DataFrame API の操作
# MAGIC ## 複数のインターフェース (Multiple Interfaces)
# MAGIC Spark SQL は、複数のインターフェイスを備えた構造化データ処理用のモジュールです。
# MAGIC
# MAGIC Spark SQLモジュールとやり取りするには、次の2つの方法があります。
# MAGIC 1. SQL クエリの実行
# MAGIC 1. DataFrame APIの利用

# COMMAND ----------

# DBTITLE 0,--i18n-5daeff66-5dae-4f1e-9a1f-d99b613ae624
# MAGIC %md
# MAGIC **Method 1: SQL クエリの実行**
# MAGIC
# MAGIC これは、前のレッスンで Spark SQL を操作した方法です。

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT name, price
# MAGIC FROM products
# MAGIC WHERE price < 200
# MAGIC ORDER BY price

# COMMAND ----------

# DBTITLE 0,--i18n-0f5a4329-12b5-4b81-875c-2722dbdf85d9
# MAGIC %md
# MAGIC **Method 2: DataFrame APIの利用**
# MAGIC
# MAGIC DataFrame APIを利用してSpark SQLクエリを書きます。
# MAGIC
# MAGIC 次のセルは、上記で取得したものと同じ結果を含む DataFrame を返します。

# COMMAND ----------

display(spark
        .table("products")
        .select("name", "price")
        .where("price < 200")
        .orderBy("price")
       )

# COMMAND ----------

# DBTITLE 0,--i18n-643d5cd6-3365-4bda-8f9d-fb3107c20e16
# MAGIC %md
# MAGIC レッスンの後半で DataFrame API の構文について説明しますが、このビルダー デザイン パターンを使用すると、SQLと似た一連の操作を連鎖することができます。

# COMMAND ----------

# DBTITLE 0,--i18n-ad108597-61bc-4dcc-9d3c-8b8a16753636
# MAGIC %md
# MAGIC ## クエリの実行 (Query Execution)
# MAGIC 任意のインターフェイスを使用して同じクエリを表現できます。 Spark SQL エンジンは、Spark クラスターでクエリの最適化と実行のため同じクエリプランを生成します。
# MAGIC
# MAGIC ![クエリ実行エンジン](https://files.training.databricks.com/images/aspwd/spark_sql_query_execution_engine.png)
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_32.png" alt="Note"> Resilient Distributed Dataset (RDD) は、Spark クラスターによって処理されるデータセットの低レベルのものです。 Spark の初期のバージョンでは、<a href="https://spark.apache.org/docs/latest/rdd-programming-guide.html" target="_blank">RDD を直接操作するコード</a>を書く必要がありました。 最新バージョンのSpark では、代わりに高レベルの DataFrame API を使用する必要があります。Spark は自動的に低レベルの RDD 操作にコンパイルします。

# COMMAND ----------

# DBTITLE 0,--i18n-c3b5d922-be36-40a4-b547-f574b52ca0ec
# MAGIC %md
# MAGIC ## Spark API ドキュメント (Spark API Documentation)
# MAGIC
# MAGIC Spark SQL で DataFrame を操作する方法を学ぶために、まず Spark API ドキュメントを見てみましょう。
# MAGIC メインの Spark <a href="https://spark.apache.org/docs/latest/" target="_blank">ドキュメント</a> ページには、Spark の各バージョンの API ドキュメントとガイドへのリンクが含まれています。
# MAGIC
# MAGIC <a href="https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html" target="_blank">Scala API</a> と<a href="https://spark.apache.org/docs/latest/api/python/index.html" target="_blank">Python API</a> が最も使用されており、ドキュメントを参照すると役立つことがよくあります。
# MAGIC Scalaドキュメントはより包括的である傾向があり、Pythonドキュメントはより多くのコード例を含む傾向があります。
# MAGIC
# MAGIC #### Spark SQL モジュールのドキュメントのナビゲート (Navigating Docs for the Spark SQL Module)
# MAGIC Scala API の **`org.apache.spark.sql`** または Python API の **`pyspark.sql`** に移動すると、Spark SQL モジュールのドキュメントがあります。
# MAGIC このモジュールで最初に探索してみるクラスは **`SparkSession`** クラスです。検索バーに「SparkSession」と入力すると、 **`SparkSession`** を見つけます。

# COMMAND ----------

# DBTITLE 0,--i18n-e630c320-f786-4259-a656-9094cfd6c677
# MAGIC %md
# MAGIC ## SparkSession
# MAGIC **`SparkSession`** クラスは、DataFrame API を使用する Spark のすべての機能への唯一のエントリです。
# MAGIC
# MAGIC Databricks ノートブックでは、既にSparkSession が作成され、 **`spark`** という変数に格納されています。

# COMMAND ----------

spark

# COMMAND ----------

# DBTITLE 0,--i18n-d507c25b-0400-447e-a668-9b0a919ed38a
# MAGIC %md
# MAGIC このレッスンの最初の例では、SparkSessionのメソッド **`table`** を使用して **`products`** テーブルから DataFrame を作成しました。これを変数 **`products_df`** に保存しましょう。

# COMMAND ----------

products_df = spark.table("products")

# COMMAND ----------

# DBTITLE 0,--i18n-868ac2d6-e824-4be0-a8d6-cdb2b2ee041b
# MAGIC %md
# MAGIC 以下は、DataFrame を作成するために使用するいくつかのメソッドです。これらはすべて **`SparkSession`** <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/spark_session.html" target="_blank">ドキュメント</a>にあります。
# MAGIC
# MAGIC
# MAGIC #### **`SparkSession`** メソッド
# MAGIC | メソッド | 説明 |
# MAGIC | --- | --- |
# MAGIC | sql | 指定クエリの結果としてDataFrameを返します |
# MAGIC | table | 指定テーブルをDataFrameとして返します |
# MAGIC | read | データを DataFrame として読み取るために使用できる DataFrameReader を返します。 |
# MAGIC | range | ステップ値とパーティション数を使用して、開始値から終了値 (排他的) までの範囲内の要素を含む列を持つ DataFrame を作成します。 |
# MAGIC | createDataFrame |主にテストに使用される、タプルのリストから DataFrame を作成します。 |

# COMMAND ----------

# DBTITLE 0,--i18n-0cb0cd98-a286-45b7-8ec7-d1f2094a1571
# MAGIC %md
# MAGIC SparkSession メソッドを使用して SQL を実行しましょう。

# COMMAND ----------

result_df = spark.sql("""
SELECT name, price
FROM products
WHERE price < 200
ORDER BY price
""")

display(result_df)

# COMMAND ----------

# DBTITLE 0,--i18n-bb9997aa-1f07-4fff-912c-1e4350db83c0
# MAGIC %md
# MAGIC ## DataFrames
# MAGIC DataFrame API のメソッドを使用してクエリを書くと、DataFrameとして結果が返されることを思い出してください。これを変数 **`budget_df`** に格納しましょう。
# MAGIC
# MAGIC **DataFrame** は、名前付き列にグループ化されたデータの分散コレクションです。

# COMMAND ----------

budget_df = (spark
             .table("products")
             .select("name", "price")
             .where("price < 200")
             .orderBy("price")
            )

# COMMAND ----------

# DBTITLE 0,--i18n-2a074b60-9587-43b5-9d57-282b219c6b39
# MAGIC %md
# MAGIC **`display()`** を使用して、DataFrameの結果を出力できます。

# COMMAND ----------

display(budget_df)

# COMMAND ----------

# DBTITLE 0,--i18n-ffcd868b-ce9d-4cd8-bb53-066076a85927
# MAGIC %md
# MAGIC **`schema`** は、データフレームの列名と型を定義します。
# MAGIC **`schema`** 属性を使用して、DataFrameのスキーマにアクセスします。

# COMMAND ----------

budget_df.schema

# COMMAND ----------

# DBTITLE 0,--i18n-fb94b6a7-735e-4050-bedf-53e778b87beb
# MAGIC %md
# MAGIC **`printSchema()`** メソッドを使用して、このスキーマのより適切な出力を表示します。

# COMMAND ----------

budget_df.printSchema()

# COMMAND ----------

# DBTITLE 0,--i18n-414bd505-67bc-4c05-a87b-9adf23d9b50d
# MAGIC %md
# MAGIC ## Transformations
# MAGIC
# MAGIC **`budget_df`** を作成したとき、一連の DataFrame 変換メソッドを使用しました。 **`select`**、**`where`**、**`orderBy`** 
# MAGIC
# MAGIC <strong><code>
# MAGIC   products_df  
# MAGIC   &nbsp;  .select("name", "price")  
# MAGIC   &nbsp;  .where("price < 200")  
# MAGIC   &nbsp;  .orderBy("price")  
# MAGIC </code></strong>
# MAGIC
# MAGIC Transformationsは DataFrame を操作して返すため、変換メソッドを連鎖させて新しい DataFrame を構築できます。
# MAGIC ただし、変換メソッドは **遅延評価**されるため、これらの操作は単独では実行できません。
# MAGIC
# MAGIC 次のセルを実行しても、計算はトリガーされません。

# COMMAND ----------

(products_df
  .select("name", "price")
  .where("price < 200")
  .orderBy("price"))

# COMMAND ----------

# DBTITLE 0,--i18n-d8f72c04-d483-40a6-b91b-854699c12a3e
# MAGIC %md
# MAGIC ## Actions
# MAGIC 逆に、DataFrame アクションは、**計算をトリガー**するメソッドです。
# MAGIC DataFrame 変換の実行をトリガーするには、アクションが必要です。
# MAGIC
# MAGIC **`show`** アクションは、次のセルのtransformationsを実行させます。

# COMMAND ----------

(products_df
  .select("name", "price")
  .where("price < 200")
  .orderBy("price")
  .show())

# COMMAND ----------

# DBTITLE 0,--i18n-43ccc1f1-5398-4715-bcbe-b071d0ac93db
# MAGIC %md
# MAGIC 以下は <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql.html#dataframe-apis" target="_blank">DataFrame</a> actionsの例です。
# MAGIC
# MAGIC ### DataFrame Action Methods  
# MAGIC | メソッド |説明 |
# MAGIC |  --- | --- |
# MAGIC | show | DataFrame の上位 n 行を表形式で表示 |
# MAGIC | count |　DataFrame の行数を返します。 | 
# MAGIC | describe,  summary |数値列と文字列の基本統計を計算 |
# MAGIC | first, head |最初の行を返します |
# MAGIC | collect | DataFrame のすべての行を含む配列を返します |
# MAGIC | take | DataFrame の最初の n 行の配列を返します。|

# COMMAND ----------

# DBTITLE 0,--i18n-a7ef182c-f9d5-41d4-a36b-327b4c3c8d45
# MAGIC %md
# MAGIC **`count`** はDataFrame の行数を返します。

# COMMAND ----------

budget_df.count()

# COMMAND ----------

# DBTITLE 0,--i18n-5c622ec1-48f8-435f-9ee8-08d9de14ec40
# MAGIC %md
# MAGIC **`collect`** は DataFrame のすべての行を含む配列を返します

# COMMAND ----------

display(budget_df)

# COMMAND ----------

budget_df.collect()

# COMMAND ----------

# DBTITLE 0,--i18n-477b58cf-e178-44fe-9495-849f4fed7dfe
# MAGIC %md
# MAGIC ## DataFramesとSQL間の変換 (Convert between DataFrames and SQL)

# COMMAND ----------

# DBTITLE 0,--i18n-e30d48ad-04f4-48e2-8b80-675ab907d99b
# MAGIC %md
# MAGIC **`createOrReplaceTempView`** は、DataFrame に基づいて一時的なビューを作成します。一時ビューの有効期間は、DataFrame の作成に使用された SparkSession に関連付けられています。

# COMMAND ----------

budget_df.createOrReplaceTempView("budget")

# COMMAND ----------

display(spark.sql("SELECT * FROM budget"))

# COMMAND ----------

# DBTITLE 0,--i18n-53a419c0-e7ad-4d43-aa8e-6899cbd43e8d
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
