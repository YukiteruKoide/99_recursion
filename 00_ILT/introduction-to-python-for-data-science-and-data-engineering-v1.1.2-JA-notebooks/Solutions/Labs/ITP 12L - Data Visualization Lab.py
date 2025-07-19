# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="d6c49d6f-2235-4e65-b012-70bf6850330c"/>
# MAGIC
# MAGIC # データ可視化 Lab
# MAGIC
# MAGIC では、　**`pandas`** と **`seaborn`** をインポートし、avocado データセットをロードしてデータの可視化・解析を行ってみましょう。

# COMMAND ----------

# MAGIC %run "../Includes/Classroom-Setup"

# COMMAND ----------

import pandas as pd
import seaborn as sns

# Set seaborn plot size to be easier to read
sns.set(rc = {"figure.figsize": (15,8)})

# COMMAND ----------

file_path = f"{DA.paths.datasets}/avocado/avocado.csv".replace("dbfs:", "/dbfs")
# Dropping incorrect index column.
df = pd.read_csv(file_path).drop("Unnamed: 0", axis=1) 
df

# COMMAND ----------

# MAGIC %md <i18n value="faba5cfc-f9cd-4012-845c-117fb3f184fa"/>
# MAGIC
# MAGIC ## 問題 1: Databricksでのプロット（Databricks Plotting）
# MAGIC
# MAGIC
# MAGIC Databricksに内蔵されているプロット機能を使って、 **`year`** あたりの平均 **`Volume`** をプロットします。
# MAGIC
# MAGIC
# MAGIC プロットするには、 **`display(df)`** を使用します。

# COMMAND ----------

# ANSWER
display(df)

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="4c4c04ec-8c7c-4dfe-b680-fc6e5e7a254f"/>
# MAGIC
# MAGIC <button onclick="myFunction2()" >クリックするとヒントが表示されます</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC    棒グラフを選択し、プロットオプションを選択し、aggregate関数を平均に設定し、yearをキーにして、Total Volumeを値に設定します。
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

# MAGIC %md <i18n value="0ee316c5-f8b7-441c-9326-05eb0e4fac6e"/>
# MAGIC
# MAGIC ## 問題　2: `pandas` によるプロット（pandas plotting）
# MAGIC
# MAGIC pandas の **`.hist()`** メソッドを用いて、アボカドの **`AveragePrice`** のヒストグラムを作成します。

# COMMAND ----------

# ANSWER
df["AveragePrice"].hist()

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="da21fa24-e730-4641-ace0-100da86d2c4f"/>
# MAGIC
# MAGIC <button onclick="myFunction2()" >クリックするとヒントが表示されます</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   列を選択してシリーズを作成します。それから、その列の Series型に対して .hist() を呼び出します．
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

# MAGIC %md <i18n value="00f37c99-64bb-4b48-b73f-f5b69310645a"/>
# MAGIC
# MAGIC ## 時刻型（Datetime）
# MAGIC
# MAGIC 残念ながら、この **`Date`** カラムはオブジェクト型として表現されています。これは、時刻に基づいた操作を行うために **`Datetime`** 型にしたい場合です (例えば、辞書順ではなく時系列でプロットするなど)。 
# MAGIC
# MAGIC 幸なことに、 `pandas` には [to_datetime()](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html?highlight=to_datetime#pandas.to_datetime) という関数があり、 Series型を受け取って、その型を **`datetime`** に変換してくれます。

# COMMAND ----------

# Notice the dtype of Date
df.dtypes

# COMMAND ----------

df["Date"] = pd.to_datetime(df["Date"])
df.dtypes

# COMMAND ----------

# MAGIC %md <i18n value="40b4972b-d755-4c4f-ac64-02a57ca8e9f2"/>
# MAGIC
# MAGIC ## 問題　3: `seaborn` plotting
# MAGIC
# MAGIC 上記の **`sns`** のエイリアスである **`seaborn`** を使って、アメリカ全土の有機アボカドの総販売量の時間に対する散布図を作成します（例えば、 **`TotalUS`** 地域は **`region`** で、 **`organic`** は **`type`** でフィルターしてください）。X軸に **`Date`** を選択します。

# COMMAND ----------

# ANSWER
plot_df = df[(df["region"] == "TotalUS") & (df["type"] == "organic")]
sns.scatterplot(data=plot_df, x="Date", y="Total Volume")

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="47287cb5-ea6b-43bd-ac47-f84d5355a1a3"/>
# MAGIC
# MAGIC <button onclick="myFunction2()" >クリックするとヒントが表示されます</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   プロット関数は次のようなものです：　sns.scatterplot(data=, x=, y=)
# MAGIC   この関数に渡すために、地域と種類を指定してフィルタリングしたDataFrameを作成します。
# MAGIC
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

# MAGIC %md <i18n value="4fd56628-9c66-44a8-9b2d-bad0552fb619"/>
# MAGIC
# MAGIC ## 問題 4: 従来のアボカドについてはどうか？（What about conventional avocados?）
# MAGIC
# MAGIC 有機アボカドの代わりに従来のアボカドを除いて、同じ散布図を作成します。この2つの間にどんな違いがありますか？軸のスケールに注目してください。

# COMMAND ----------

# ANSWER
d = df[(df["region"] == "TotalUS") & (df["type"] == "conventional")]
sns.scatterplot(data=d, x="Date", y="Total Volume")

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="2e5c4b7b-0b50-41f0-8936-e407defce6dd"/>
# MAGIC
# MAGIC <button onclick="myFunction2()" >クリックするとヒントが表示されます</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC  前と同じコードを使いますが、今回はdf["type"] == "conventional "でフィルタリングすることを確認してください。
# MAGIC
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
