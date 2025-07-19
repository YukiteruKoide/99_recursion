# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="9ad87fe1-fe24-4e65-b474-b126fe0cd797"/>
# MAGIC
# MAGIC # ライブラリ (Libraries)
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは<br>
# MAGIC - Databricks の **%run** 機能を学びます
# MAGIC - ライブラリとPyPIの紹介をします

# COMMAND ----------

# MAGIC %md <i18n value="d2d8408c-f293-45e1-a6a7-68b5fd4e5ea5"/>
# MAGIC
# MAGIC ### %run
# MAGIC
# MAGIC これまでは、1つのノートブックで個々のセルを実行したり、ノートブックツールバーの「**すべて実行**」を使って実行可能なコマンドセルを上から下へ順番に実行したりしてきました。
# MAGIC
# MAGIC Databricksは、あるノートブックが*別の*ノートブックにある実行可能なコマンドセルをすべて実行できるようにするための **%run** マジックコマンドをサポートしています。
# MAGIC
# MAGIC このとき、他のノートブックの状態、つまりそのノートブックで定義されているすべてのクラス、関数、変数にアクセスすることもできます。
# MAGIC
# MAGIC **%run**マジックコマンドはコマンドセルの先頭に記述し、他のノートブックへのパスをその後に記述する必要があります。コマンドセル内で、 **%run** マジックコマンドの前後にPythonのコードを記述することは **できません** 。

# COMMAND ----------

# MAGIC %run ./Includes/run_example

# COMMAND ----------

# MAGIC %md <i18n value="099718a4-1515-4d0a-b2b5-a0f5a1541129"/>
# MAGIC
# MAGIC このサンプルノートブックは、名前を受け取って挨拶を返す関数 **`greet()`** を定義しています。そのノートブックの状態にアクセスできるようになったので、ノートブックで定義されていなくても **`greet()`** を使うことができます。これは、メインのノートブックを散らかさずにヘルパー関数を定義し、テストするのに便利な方法です。

# COMMAND ----------

greet("Bob")

# COMMAND ----------

# MAGIC %md <i18n value="450fa743-e6f9-4dd3-95ae-da18a436fa7c"/>
# MAGIC
# MAGIC ### PyPI と Python ライブラリ
# MAGIC
# MAGIC このように、有用な定義のコレクションをライブラリに保存して、さまざまなファイルからアクセスするという考え方は、Databricks環境を超えて有用なものです。実際、Pythonがシステムにインストールされると、通常、[Python標準ライブラリ](https://docs.python.org/3/library/)と呼ばれる便利なユーティリティのコレクションも含まれています。さらに、開発者は作成したライブラリをオンライン上にアップロードすることで、Pythonコミュニティと共有することができます。 
# MAGIC
# MAGIC <a href="https://pypi.org/" target="_blank">PyPI</a>は、Python Package Indexの略で、開発者がライブラリをアップロードして共有し、ユーザーがそれをダウンロードするための中心的なリポジトリです。さまざまな用途に対応する数千ものライブラリが含まれています。中には、特定のユースケースで業界標準となり、業界内のコードの標準化に役立っているものもあります。 
# MAGIC
# MAGIC
# MAGIC デフォルトでは、Pythonはこれらのライブラリにアクセスすることはできません。プログラムで使用するライブラリをインポートする前に、まずPyPIからお使いのシステムにライブラリをインストールする必要があります。

# COMMAND ----------

# MAGIC %md <i18n value="868481bc-9374-4770-b046-a27e395e4bc8"/>
# MAGIC
# MAGIC #### pip
# MAGIC
# MAGIC pipは、PyPIから実際にライブラリをダウンロードする際に最もよく使われるツールです。通常、Pythonのインストールに含まれています。 
# MAGIC
# MAGIC コマンドラインまたはターミナルで、次のように入力します **`pip install <パッケージ名>`**　。例えば有名なライブラリである **`numpy`** をインストールしたい場合、次のように記述します **`pip install numpy`** 。
# MAGIC
# MAGIC Databricksの環境は少し違います。 **`pip install <パッケージ名>`** とターミナルに入力するのではなく **`%pip install <パッケージ名>`** をセルに入力します。Databricks セルは Python コードを期待しています。 **`%pip`** は、代わりにpipコマンドを期待するように指示します。
# MAGIC
# MAGIC **注意**：Databricksでは、このタイプのコマンドはPythonターミナルを再起動するので、前に実行したコードの結果が失われないように、ノートブックの先頭で使用するのがベストです。

# COMMAND ----------

# MAGIC %pip --help

# COMMAND ----------

# MAGIC %md <i18n value="4c16a8f1-d12a-4ce0-bbd5-053280b4e96b"/>
# MAGIC
# MAGIC 次のコードセルはPythonインタプリタを再起動するので、`greet()`にアクセスするためには`./Includes/run_example`ノートブックを再実行する必要があることを意味します。

# COMMAND ----------

# MAGIC %pip install numpy

# COMMAND ----------

# MAGIC %md <i18n value="a1d330d7-a006-4079-809b-02a4736f497f"/>
# MAGIC
# MAGIC 幸い、私たちのDatabricks環境には、 **`numpy`** を含むいくつかの便利なライブラリがあらかじめインストールされていますので、必要なものだけをインポートすればよいのです。
# MAGIC
# MAGIC 例えば、ある数値の平方根を取る関数が欲しいとします。Pythonには組み込まれていませんが、<a href="https://numpy.org/doc/stable/" target="_blank">numpy</a>にはあります。
# MAGIC
# MAGIC 最初のステップは、 **`numpy`** で定義された機能を使用することをPythonに伝えることです。システムにインストールされているライブラリをインポートする最も簡単な方法は、次のように **`import`** 文を使うことです。

# COMMAND ----------

import numpy

# COMMAND ----------

# MAGIC %md <i18n value="be36835e-e871-4d95-a546-004b0c36031f"/>
# MAGIC
# MAGIC さて、インポートされた **`numpy`** ライブラリに定義された関数にアクセスするには 次のように書きます。 **`numpy.function_name(引数)`** 。
# MAGIC
# MAGIC これを、numpyで次のように定義されている平方根関数で見てみましょう **`sqrt(引数)`** 。

# COMMAND ----------

numpy.sqrt(4.0)

# COMMAND ----------

# MAGIC %md <i18n value="cad7f412-9c0a-4bb6-9808-5e94bb9fca43"/>
# MAGIC
# MAGIC ライブラリをインポートする際にも、エイリアスを作成することができます。

# COMMAND ----------

import numpy as np

np.sqrt(4.0)

# COMMAND ----------

# MAGIC %md <i18n value="1df20310-0c7a-4315-a514-fcdf70bddcd9"/>
# MAGIC
# MAGIC また、ライブラリから特定の関数をインポートすることも可能です。

# COMMAND ----------

from numpy import sqrt

sqrt(4.0)

# COMMAND ----------

# MAGIC %md <i18n value="7ca81733-cafe-43fc-af1a-f6e81ef82cbd"/>
# MAGIC
# MAGIC #### `help()`
# MAGIC
# MAGIC **`help()`** 関数に渡された項目のドキュメントを表示できることを思い出してください。 **`help()`** は、ライブラリとそのライブラリで定義されたものの両方に対して使うことができます。

# COMMAND ----------

help(np)

# COMMAND ----------

help(np.sqrt)

# COMMAND ----------

# MAGIC %md <i18n value="017e2ccc-17b6-4711-a356-a7895414a943"/>
# MAGIC
# MAGIC ライブラリの作成はこの入門講座の範囲外ですが、それらが定義する関数やクラスはすべて、これまで見てきたのと同じ方法で定義されていることは覚えておいてください。

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
