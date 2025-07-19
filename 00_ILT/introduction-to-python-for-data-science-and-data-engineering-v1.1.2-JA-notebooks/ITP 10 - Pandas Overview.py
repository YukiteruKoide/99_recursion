# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="3a4f1c43-9316-4e40-91a0-2e61ae23c8a4"/>
# MAGIC
# MAGIC # Pandas
# MAGIC
# MAGIC **<a href="https://pandas.pydata.org/pandas-docs/stable/reference/index.html" target="_blank">pandas</a>** は、高性能で使いやすいデータ構造とデータ分析ツ機能を備え、データサイエンティストの間で人気の高いPythonライブラリです。
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは<br>
# MAGIC * **`pandas`** とは何で、なぜそんなに人気があるのかを説明します
# MAGIC * **`pandas`** の **`DataFrame`** と **`Series`** を作成し操作します
# MAGIC * **`pandas`** オブジェクトに対する操作を実行します
# MAGIC
# MAGIC まず **`pandas`** を、 **`pd`** というエイリアスにてインポートし、 **`pandas`** と毎回入力することなく、ライブラリを参照できるようにします。 **`pandas`** はDatabricksにあらかじめインストールされています。

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md <i18n value="23d65c0c-d3f7-4e13-a0ee-f82272eb4daa"/>
# MAGIC
# MAGIC #### なぜ`pandas`なのか？
# MAGIC
# MAGIC * データによる意思決定がますます増えています。
# MAGIC * Excelは素晴らしいが、以下の場合はどうでしょう...
# MAGIC   - 毎日新しいデータで再実行するために、分析を自動化したいですか？
# MAGIC   - 同僚と共有するためのコードベースを構築したいのですか？
# MAGIC   - ビジネス上の意思決定を行うために、より強固な分析が必要ですか？
# MAGIC   - 機械学習がしたいですか？
# MAGIC * **`pandas`** は、Pythonを使うデータアナリストやデータサイエンティストが使用するコアライブラリの1つです。

# COMMAND ----------

# MAGIC %md <i18n value="68744e01-4fc2-4282-9fae-bf6898d0c264"/>
# MAGIC
# MAGIC ## `DataFrame`
# MAGIC
# MAGIC これまで、異なるデータ型が異なる種類のデータや機能を提供することを見てきました。 
# MAGIC
# MAGIC **`pandas`** は、厳密でプログラムのデータ分析を可能にするデータ型と関数を提供するライブラリです。
# MAGIC - **`pandas`**　のデータ型の中核をなすのは　**`DataFrame`**　と呼ばれるものです。
# MAGIC
# MAGIC [**DataFrame**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)は、名前のついた行と列からなる2次元のテーブルであり、SQLのテーブルに似たものです。 
# MAGIC
# MAGIC - **`DataFrame`** クラスはテーブル内のデータのための **`data`** 属性をもち、これはオブジェクトを作成する際に定義する必要があります。
# MAGIC
# MAGIC 例えば、次のようなテーブルを **`DataFrame`** にしたいとします：
# MAGIC
# MAGIC | Name | Age | Job |
# MAGIC | ----------- | ----------- | ----------- |
# MAGIC | John | 30 | Journalist |
# MAGIC | Mary | 30 | Programmer |
# MAGIC | Abe | 40 | Chef |
# MAGIC
# MAGIC その一つの方法は、リスト内の各リストがデータの行を表すリストのリストを作成することです。

# COMMAND ----------

data = [["John", 30, "Journalist"], ["Mary", 30, "Programmer"], ["Abe", 40, "Chef"]]

df = pd.DataFrame(data=data)
df

# COMMAND ----------

# MAGIC %md <i18n value="96e03931-0ce6-4d71-914f-93f192c90931"/>
# MAGIC
# MAGIC カスタムクラスのオブジェクトを **`object = Class()`** のようにして作成することを思い出してください。 **`DataFrame`** は **`pandas`** で定義されているので、 **`pd.DataFrame()`** とします。

# COMMAND ----------

# MAGIC %md <i18n value="75f28ee2-cedb-477e-ad86-bf4684cff899"/>
# MAGIC
# MAGIC ### 列名の追加 (Adding Column Names)
# MAGIC
# MAGIC 上記の0、1、2という列名はデフォルト値です。任意の列名を指定するために **`DataFrame`** には **`columns`** という別の属性があります。

# COMMAND ----------

cols = ["Name", "Age", "Job"]
df = pd.DataFrame(data=data, columns=cols)
df

# COMMAND ----------

# MAGIC %md <i18n value="12dcbd4f-2636-41b1-a103-88b1a7325494"/>
# MAGIC
# MAGIC ## `Series`
# MAGIC
# MAGIC **`pandas`** が提供するもう一つの主要なデータ型として [**Series**](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) があります。
# MAGIC
# MAGIC **`Series`** は **`DataFrame`** の列の一つです。
# MAGIC
# MAGIC **`Series`** を以下の2つの方法で選択することができます。
# MAGIC
# MAGIC 1. **`df["column_name"]`**
# MAGIC 2. **`df.column_name`**
# MAGIC
# MAGIC Ageの列を以下で選択してみましょう。

# COMMAND ----------

df["Age"]

# COMMAND ----------

df.Age

# COMMAND ----------

# MAGIC %md <i18n value="46985f3d-66e6-4bb3-b305-10e2db222867"/>
# MAGIC
# MAGIC 列の選択には　**`df["column_name"]`**　を使うことが望ましいです。 **`df.column_name`** 記法は、列名にスペースがある場合にはうまく機能しません。

# COMMAND ----------

# MAGIC %md <i18n value="a0b445c2-3e9a-4814-b4c9-249a7d2dabeb"/>
# MAGIC
# MAGIC ## dtypes
# MAGIC
# MAGIC 上の **`Series`** オブジェクトを見ると **`dtype: int64`**というのが目に入るはずです。 
# MAGIC
# MAGIC **`pandas`** の *dtypes*　はdata types(データ型)の略語で、列の値のデータ型を指します。 
# MAGIC
# MAGIC 次に、 **`DataFrame`** と **`Series`** が提供するいくつかのメソッドと機能を見ていきますが、オブジェクト型によって何ができるかが決まるのと同様に、 列の[**dtype**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html)によってできることが決まってきます。
# MAGIC
# MAGIC 例えば、数値列の平均を取ることはできるが、非数値列の平均を取ることはできません。 
# MAGIC
# MAGIC 列の **`dtypes`** が **`pandas`** に固有なものではありますが、最も一般的なものは Python の組み込み型に非常によく似ています。
# MAGIC
# MAGIC 1. **`object`** は単なるテキストであり、文字列と同様です
# MAGIC 2. **`int64`** は整数
# MAGIC 3. **`float64`** は浮動小数点数
# MAGIC 4. **`bool`** は真偽値
# MAGIC
# MAGIC
# MAGIC **`dtypes`** 属性にアクセスすることで、 **`DataFrame`** の全ての列の **`dtypes`** を見ることができます。

# COMMAND ----------

# MAGIC %md <i18n value="b129d939-a308-4682-b818-33498bf83f87"/>
# MAGIC
# MAGIC ## `Series`の操作 (Series Operations)
# MAGIC
# MAGIC dtypeに似た組み込み型に対してできる操作のように、ある特定のdtypeの **`Series`** に対して同様の操作を行うことができます。 
# MAGIC
# MAGIC これらの操作は要素ごとに行われます。 
# MAGIC
# MAGIC 例えば Pythonで整数値を足すことができるのと同様に、 **`int64`** **`Series`** を足すことができます。

# COMMAND ----------

df["Age"] + df["Age"]

# COMMAND ----------

# MAGIC %md <i18n value="eab93237-f960-44fe-9840-6d82497b1e29"/>
# MAGIC
# MAGIC 基本的な整数演算はすべて以下のように使用できます：

# COMMAND ----------

df["Age"] * 3 - 1

# COMMAND ----------

# MAGIC %md <i18n value="e6713871-d93a-4b68-ae8f-a08d14e871c0"/>
# MAGIC
# MAGIC #### **`Series`** からの値の選択 (Selecting a value from a Series)
# MAGIC
# MAGIC 時々、 **`Series`** の値を引き出したいことがあるでしょう。リストからインデックスにより値を取り出すのと同じように、 **`Series`** からインデックスによって値を取り出すことができます。

# COMMAND ----------

df["Age"][0]

# COMMAND ----------

# MAGIC %md <i18n value="1ce3e63c-3e11-4b0a-8078-b6584146c9e5"/>
# MAGIC
# MAGIC ## 列のサブセットを選択する (Selecting a Subset of Columns)
# MAGIC
# MAGIC これまで、指定した列を **`Series`** から選択する方法を見てきました。
# MAGIC
# MAGIC 列のサブセットを **`DataFrame`** として選択することもできます。
# MAGIC
# MAGIC このように列のサブセットを選択することができます：
# MAGIC
# MAGIC **`df[[col_1, col_2, col_3, ...]]`**
# MAGIC
# MAGIC NameとAgeの列だけを選択してみましょう。

# COMMAND ----------

df[["Name", "Age"]]

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
