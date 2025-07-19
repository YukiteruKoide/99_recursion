# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="92f0d116-aa27-4e1f-9be2-9eb102794cf6"/>
# MAGIC
# MAGIC # データの可視化 (Data Visualization)
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは
# MAGIC 以下の方法を使った **`pandas`** DataFramesのデータ可視化を探ります
# MAGIC - Databricks組み込みのプロット手法 
# MAGIC - **`pandas`** プロットメソッド
# MAGIC - **`seaborn`** プロット機能
# MAGIC
# MAGIC **`pandas`** と Airbnb データセットをインポートしてみましょう。

# COMMAND ----------

# MAGIC %run "./Includes/Classroom-Setup"

# COMMAND ----------

import pandas as pd

# COMMAND ----------

file_path = f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv".replace("dbfs:", "/dbfs")
df = pd.read_csv(file_path)
df.head(3)

# COMMAND ----------

# MAGIC %md <i18n value="46852d14-6b5c-4906-8a87-2d87f099bfeb"/>
# MAGIC
# MAGIC ## 組み込みのプロット手法 (Built-in Plotting)
# MAGIC
# MAGIC Databricksには、Databricksノートブックで使用できるデータ可視化ツールが内蔵されています。 
# MAGIC
# MAGIC これらを利用するために、pandasのDataFrameに対してDatabricksが提供する組み込みの **`display()`** 関数を使ってみましょう
# MAGIC
# MAGIC デフォルトでは、`DataFrame`テーブルとして見るだけです。しかし、"テーブル"の右の"+"から"ビジュアライゼーション"をクリックすると、可視化モードに切り替えることができます。

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md <i18n value="c609e59a-b0ce-40fc-bd71-24e10730b6b6"/>
# MAGIC
# MAGIC ## プロットオプション (Plot Options)
# MAGIC
# MAGIC プロットの種類を変更するために、「Visualization Type」から種類を選択することができます。
# MAGIC
# MAGIC そこから、DataFrameのどの列に対してどのようなプロットをしたいかを指定することができます。
# MAGIC
# MAGIC 例えば、地域ごとの平均寝室数を表示したいとします。 
# MAGIC
# MAGIC そのためには：
# MAGIC
# MAGIC 1. **`neighbourhood`** をX columnに設定します。
# MAGIC 1. **`bedrooms`** をY columnsに追加します。
# MAGIC 1. 集計関数をAverageに変更します。
# MAGIC 1. 「Visualization Type」から棒グラフが選択されていることを確認してください。

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md <i18n value="6d9956db-6e60-4533-966e-1be99415c1b8"/>
# MAGIC
# MAGIC 最初の1000行のプレビューしか初期表示されませんが、 **`保存`** をクリックすると全ての行に対して動作します。

# COMMAND ----------

# MAGIC %md <i18n value="3c4eb78d-05a2-4133-905b-90411fffdb02"/>
# MAGIC
# MAGIC ## pandasのプロット (Pandas Plotting)
# MAGIC
# MAGIC **`pandas`** も、いくつかのプロット機能を提供しています。 
# MAGIC
# MAGIC **`Series`** に **`hist()`** メソッドを使うことでヒストグラムを作成することができます．
# MAGIC
# MAGIC 寝室数のヒストグラムを作成してみましょう。

# COMMAND ----------

df["bedrooms"].hist()

# COMMAND ----------

# MAGIC %md <i18n value="8eec6709-d9aa-499c-ab29-37d51ee8dfc1"/>
# MAGIC
# MAGIC **`bins`** パラメータで引数を渡すことでビンの数を指定することもできます。

# COMMAND ----------

df["bedrooms"].hist(bins=20)

# COMMAND ----------

# MAGIC %md <i18n value="14bed99e-90e8-4a85-bfd5-99be4ff0563e"/>
# MAGIC
# MAGIC pandasを使った箱ひげ図の作成も可能です。
# MAGIC
# MAGIC **`DataFrame`** の **`boxplot([cols])`** メソッドを使用して、指定された列のそれぞれについて箱ひげ図を作成します。

# COMMAND ----------

df.boxplot(["bedrooms", "bathrooms"])

# COMMAND ----------

# MAGIC %md <i18n value="9c6d8ce4-ef18-4c32-b9e1-fe6ada690af5"/>
# MAGIC
# MAGIC # Seaborn
# MAGIC
# MAGIC [seaborn](https://seaborn.pydata.org/)はpandasのDataFramesと連動する非常に人気のあるデータ可視化ライブラリです。 
# MAGIC
# MAGIC 比較的簡単に使えることと、見栄えの良いビジュアライゼーションができることが人気の理由です。
# MAGIC
# MAGIC **`seaborn`** をインポートしてみましょう： **`sns`** をエイリアスとして使用するのが一般的です。

# COMMAND ----------

import seaborn as sns

# COMMAND ----------

# MAGIC %md <i18n value="cec27556-7c8f-4991-89ad-d060836aaf98"/>
# MAGIC
# MAGIC ## 散布図 (Scatter plot)
# MAGIC
# MAGIC まず、散布図を作成してみましょう。 **`bedrooms`** をX軸に、 **`bathrooms`** をY軸にプロットします。 
# MAGIC
# MAGIC これを実行するために **`sns.scatterplot(データ=, x=, y=)`** を呼び出します。
# MAGIC
# MAGIC データパラメータとして **`DataFrame`** を、x と y パラメータに必要な列名を指定します。

# COMMAND ----------

sns.scatterplot(data=df, x="bedrooms", y="bathrooms")

# COMMAND ----------

# MAGIC %md <i18n value="f8901310-8093-4568-944e-ac277d0b3da0"/>
# MAGIC
# MAGIC また、散布図に最良の回帰直線をプロットすることもできます。 
# MAGIC
# MAGIC これは、同じパラメータを、 **`regplot()`** 関数に使用することで実現できます。

# COMMAND ----------

sns.regplot(data=df, x="bedrooms", y="bathrooms")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
