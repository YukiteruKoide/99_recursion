# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="1818ed45-df1d-4a39-8074-e2841494477c"/>
# MAGIC
# MAGIC # データ型と変数ラボ (Data Types and Variables Lab)
# MAGIC
# MAGIC ## 練習： (Exercise:)
# MAGIC * 変数 **`num_chocolate`**　を定義し、あなたが食べたいチョコレートバーの数と等しくなるように設定してください。これらは小数を含まない数値（例：整数）でなければなりません。
# MAGIC * 変数 **`name`**　を定義し、それをあなたの名前と等しく設定してください。
# MAGIC * 文字列　**`chocolate_string`**　をf-stringフォーマットを使って次のように定義します：　" **`name`**　would like to eat **`num_chocolate`**　bars of chocolate" 
# MAGIC * 文字列 **`chocolate_string`**　を表示してください。

# COMMAND ----------

# ANSWER
name = "James"
num_chocolate = 10
chocolate_string = f"{name} would like to eat {num_chocolate} bars of chocolate"

print(chocolate_string)

# COMMAND ----------

# MAGIC %md <i18n value="d156910a-4562-4a24-bc6e-2d3ed9826f24"/>
# MAGIC
# MAGIC **回答のチェック** (**Check your work:**)
# MAGIC
# MAGIC ラボでは、ほとんどの問題の後に以下のような　**回答のチェック**　のためのセルを用意しています。問題を解いた後セルを実行して、回答が正しいかどうかを確認してください。 
# MAGIC
# MAGIC 以下で使用する　**assert**　文の使い方を知っている必要はありません。 
# MAGIC
# MAGIC もし、assert文の後の論理式がTrueと評価されない場合、コードは終了し、エラーが発生することになります。

# COMMAND ----------

assert type(name) == str, "Name should be a string"
assert type(num_chocolate) == int, "You have to eat the entire chocolate bar! No floats allowed"
assert chocolate_string == f"{name} would like to eat {num_chocolate} bars of chocolate", "Did you mistype something?"
print("Test passed!")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
