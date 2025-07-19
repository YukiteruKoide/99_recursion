# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="50d4a990-cefe-41dd-a439-12f7706751be"/>
# MAGIC
# MAGIC # クラス (Classes)
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このLabでは<br>
# MAGIC
# MAGIC 前回のレッスンで学んだ、以下のような概念を適用します：
# MAGIC - インスタンス変数を利用して、新しいデータ型のデータを定義する 
# MAGIC - メソッドを利用して、新しいデータ型に機能を追加する

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="37e05756-08e7-4ec8-8583-0cf5d64eea2b"/>
# MAGIC
# MAGIC ## 練習問題：シンプソン
# MAGIC
# MAGIC <img src="https://i.pinimg.com/originals/13/63/37/13633734d116fe188af57fe9da7d095e.jpg" style="height:400">
# MAGIC
# MAGIC 以下の変数とメソッドを持ち、シンプソン家のメンバーを表す **`Simpson`** クラスを定義します。
# MAGIC
# MAGIC * 各Simpsonは **`first_name`** 、 **`name`** 、 **`favorite_food`** を持ちます。 
# MAGIC   * これらの変数を初期化する **`__init__()`** メソッドを定義します。 
# MAGIC   
# MAGIC * `{first_name} Simpson is {age} years old and their favorite food is {favorite_food}`という形式の文字列を返す **`simpson_summary()`** メソッドを定義します。
# MAGIC   * 例えば、`first_name="Homer"`、`age=39`、 `favorite_food="donuts"` の場合、このように返されるはずです：`Homer Simpson is 39 years old and their favorite food is donuts`
# MAGIC   
# MAGIC * 別の **`Simpson`** オブジェクトを受け取り、そのメソッドを呼び出した人が他の人よりも年上の場合 **`True`** 、そうでない場合は **`False`** を返す **`older()`** というメソッドを定義します。

# COMMAND ----------

# ANSWER
class Simpson():
    
    def __init__(self, first_name, age, favorite_food):
        self.first_name = first_name
        self.age = age
        self.favorite_food = favorite_food
        
    def simpson_summary(self):
        return f"{self.first_name} Simpson is {self.age} years old and their favorite food is {self.favorite_food}"
        
    def older(self, other_simpson):
        return self.age > other_simpson.age

# COMMAND ----------

# MAGIC %md <i18n value="b3b3aa47-1699-4d9e-806d-fa84134c143f"/>
# MAGIC
# MAGIC **回答をチェックする**

# COMMAND ----------

homer = Simpson("Homer", 39, "Donuts")
bart = Simpson("Bart", 10, "Hamburgers")
assert homer.first_name == "Homer", "first_name is not set properly"
assert homer.favorite_food == "Donuts", "favorite_food is not set properly"
assert bart.age == 10, "Age is not set properly"
assert homer.simpson_summary() == "Homer Simpson is 39 years old and their favorite food is Donuts", "simpson_summary is incorrect"
assert bart.simpson_summary() == "Bart Simpson is 10 years old and their favorite food is Hamburgers", "simpson_summary is incorrect"
assert homer.older(bart) == True, "Homer is older than Bart"
assert bart.older(homer) == False, "Bart is not older than Homer"
print("Test passed!")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
