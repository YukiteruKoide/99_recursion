# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="a951a3d5-c3dd-47f3-baf8-5ac6e51da1b8"/>
# MAGIC
# MAGIC # Pandas Lab
# MAGIC
# MAGIC このラボでは、基本的なデータ操作に<a href="https://pandas.pydata.org/docs/" target="_blank">pandas</a>を使用します。

# COMMAND ----------

# MAGIC %md <i18n value="1eff4d5c-13cc-431f-9c45-e8d1ecb66998"/>
# MAGIC
# MAGIC #### 問題１：`DataFrame`の作成
# MAGIC
# MAGIC 以下の犬の表を表現する　**`df`**　と言う名前の　**`DataFrame`** を作成します。以下にそのデータを掲載します。
# MAGIC
# MAGIC | Name | Age | Breed| 
# MAGIC | ----------- | ----------- | ----------- | 
# MAGIC | Buddy | 3 | Australian Shepherd | 
# MAGIC | Harley | 10 | Labrador | 
# MAGIC | Luna | 2 | Golden Retriever | 
# MAGIC | Bailey | 8 | Chihuahua |

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# ANSWER
data = [["Buddy", 3, "Australian Shepherd"], ["Harley", 10, "Labrador"], ["Luna", 2, "Golden Retriever"], ["Bailey", 8, "Chihuahua"]]
column_names = ["Name", "Age", "Breed"]

df = pd.DataFrame(data=data, columns=column_names)
df

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="73936461-b0a9-47d0-b13c-8dec39331fdb"/>
# MAGIC
# MAGIC <button onclick="myFunction2()" >クリックするとヒントが表示されます。</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   データと列の属性を忘れずに指定してください。
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

# MAGIC %md <i18n value="e287fd23-3bce-450c-9804-35dd232d0e00"/>
# MAGIC
# MAGIC **以下のセルを実行して、回答をチェックしてください**

# COMMAND ----------

assert (df.columns == ["Name", "Age", "Breed"]).all(), "The columns are named incorrectly"
assert [df.iloc[0][x] for x in ["Name", "Age", "Breed"]] == ["Buddy", 3, "Australian Shepherd"], "First row defined incorrectly"
assert [df.iloc[1][x] for x in ["Name", "Age", "Breed"]] == ["Harley", 10, "Labrador"], "Second row defined incorrectly"
assert [df.iloc[2][x] for x in ["Name", "Age", "Breed"]] == ["Luna", 2, "Golden Retriever"], "Third row defined incorrectly"
assert [df.iloc[3][x] for x in ["Name", "Age", "Breed"]] == ["Bailey", 8, "Chihuahua"], "Fourth row defined incorrectly"
print("Test passed!")

# COMMAND ----------

# MAGIC %md <i18n value="4a340577-c141-4e6f-8145-031dfa879b32"/>
# MAGIC
# MAGIC #### 問題２：`dtypes`とは何ですか？
# MAGIC
# MAGIC **`dtypes`** 属性を出力し、各列の型を確認します。

# COMMAND ----------

# ANSWER
df.dtypes

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="be17630c-8f3a-4b0f-bd2a-3ffa71e8cc39"/>
# MAGIC
# MAGIC <button onclick="myFunction2()" >クリックするとヒントが表示されます</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   属性へのアクセスは、object.attribute のように行うことを忘れないでください。
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

# MAGIC %md <i18n value="80828ff9-7279-4648-8d21-c11dbe9586fb"/>
# MAGIC
# MAGIC #### 問題３：列のサブセット
# MAGIC
# MAGIC **`Name`** と **`Age`** 列のみを選択し，新しい変数 **`name_age_df`** としてアサインします。

# COMMAND ----------

# ANSWER
name_age_df = df[["Name", "Age"]]
name_age_df

# COMMAND ----------

# MAGIC %md <i18n value="430aef6a-de3d-4e81-9d4d-edc70c652b0b"/>
# MAGIC
# MAGIC **以下のセルを実行して、回答をチェックしてください**
# MAGIC
# MAGIC 以下のアサーションでは [**iloc**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)を使用して、位置による選択のための整数での位置ベースのインデックスを作成しています。

# COMMAND ----------

assert (name_age_df.columns == ["Name", "Age"]).all(), "The columns are named incorrectly"
assert name_age_df.shape == (4, 2), "There are not the right number of rows or columns"
assert [name_age_df.iloc[0][x] for x in ["Name", "Age"]] == ["Buddy", 3], "First row defined incorrectly"
assert [name_age_df.iloc[1][x] for x in ["Name", "Age"]] == ["Harley", 10], "Second row defined incorrectly"
assert [name_age_df.iloc[2][x] for x in ["Name", "Age"]] == ["Luna", 2], "Third row defined incorrectly"
assert [name_age_df.iloc[3][x] for x in ["Name", "Age"]] == ["Bailey", 8], "Fourth row defined incorrectly"
print("Test passed!")

# COMMAND ----------

# MAGIC %md <i18n value="c99a51f7-7d44-4354-955e-5c338b1ae957"/>
# MAGIC
# MAGIC #### 問題４：新しいカラムの作成
# MAGIC
# MAGIC 犬の1年は、人間の7年に相当するとしましょう。犬の年齢を取り、それを7倍した **`Human Age`** という新しい列を **`df`** に作成します。

# COMMAND ----------

# ANSWER
df["Human Age"] = df["Age"]*7
df

# COMMAND ----------

# MAGIC %md <i18n value="a57f04d2-d9d2-4391-95c2-41311385e754"/>
# MAGIC
# MAGIC **以下のセルを実行して、回答をチェックしてください**

# COMMAND ----------

assert df.shape == (4, 4), "There are not the correct number of rows or columns"
assert (df.columns == ["Name", "Age", "Breed", "Human Age"]).all(), "The columns are named incorrectly"
assert [df.iloc[0][x] for x in ["Name", "Age", "Breed", "Human Age"]] == ["Buddy", 3, "Australian Shepherd", 21], "First row defined incorrectly"
assert [df.iloc[1][x] for x in ["Name", "Age", "Breed", "Human Age"]] == ["Harley", 10, "Labrador", 70], "Second row defined incorrectly"
assert [df.iloc[2][x] for x in ["Name", "Age", "Breed", "Human Age"]] == ["Luna", 2, "Golden Retriever", 14], "Third row defined incorrectly"
assert [df.iloc[3][x] for x in ["Name", "Age", "Breed", "Human Age"]] == ["Bailey", 8, "Chihuahua", 56], "Fourth row defined incorrectly"
print("Test passed!")

# COMMAND ----------

# MAGIC %md <i18n value="9b3bf30d-b799-4d63-9096-fef33ffb9203"/>
# MAGIC
# MAGIC #### 問題5．値を抽出する
# MAGIC
# MAGIC プログラムによってBuddyの **`Breed`** を抽出し、指定された **`breed`** 変数に代入します。

# COMMAND ----------

# ANSWER 
breed = df[df["Name"] == "Buddy"]["Breed"][0]
breed

# COMMAND ----------

# MAGIC %md <i18n value="86d48db8-6cdd-4c7b-93af-f638b9c9cd3a"/>
# MAGIC
# MAGIC **以下のセルを実行して、回答をチェックしてください**

# COMMAND ----------

assert breed == "Australian Shepherd", "Breed is not defined correctly"
print("Test passed!")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
