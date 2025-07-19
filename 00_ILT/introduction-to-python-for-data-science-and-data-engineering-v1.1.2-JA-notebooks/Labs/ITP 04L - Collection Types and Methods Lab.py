# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="2e588f6c-a1c4-4184-888c-25dd7f246cf4"/>
# MAGIC
# MAGIC # コレクション型とメソッド(Collection Types and Methods) Lab
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このLabでは<br>
# MAGIC
# MAGIC 前回のレッスンで学んだ、以下のような概念を適用します：
# MAGIC * 新しいコレクション型でのオブジェクトとメソッドの使用

# COMMAND ----------

# MAGIC %md <i18n value="f43f90db-5f06-4f7b-bbe1-e4a4a27a1984"/>
# MAGIC
# MAGIC #### 問題1a：夕食
# MAGIC
# MAGIC "potatoes, peppers, onions"という要素をこの順番で持つ **`dinner_list`** というリストを提供します。

# COMMAND ----------

# TODO
dinner_list = ["potatoes", "peppers", "onions"]

# COMMAND ----------

# MAGIC %md <i18n value="5382a8a7-3300-468e-8f1d-8009c6c3bb8c"/>
# MAGIC
# MAGIC #### 問題1b：夕食 
# MAGIC
# MAGIC しかし、実際に食べたのは普通のpotatoesではなくsweet potatoesなので、リストの最初の要素を"sweet potatoes"に変更します。

# COMMAND ----------

dinner_list[0] = ("sweet potatoes")

# COMMAND ----------

dinner_list

# COMMAND ----------

assert dinner_list == ['sweet potatoes', 'peppers', 'onions'], "dinner_list should be ['sweet potatoes', 'peppers', 'onions']"
print("Test passed!")

# COMMAND ----------

# MAGIC %md <i18n value="768e4c64-8466-4084-87b0-51a55f63c26f"/>
# MAGIC
# MAGIC #### 問題1c：夕食 
# MAGIC 最後に、ご飯(rice)も食べたので、"rice"をリストの最後に追加してください。

# COMMAND ----------

# TODO
dinner_list.append("rice")

# COMMAND ----------

assert dinner_list == ['sweet potatoes', 'peppers', 'onions', 'rice'], "dinner_list should be ['sweet potatoes', 'peppers', 'onions', 'rice']"
print("Test passed!")

# COMMAND ----------

# MAGIC %md <i18n value="04208057-4d9e-4b91-a12c-1c811d2940bf"/>
# MAGIC
# MAGIC #### 問題2a：夕食の辞書
# MAGIC
# MAGIC **`dinner_dict`** という辞書を作成し、`"sweet potatoes":3`, `"peppers":4`, `"onions":1` という、夕食に食べたものを表すペアを入れましょう。

# COMMAND ----------

# TODO
dinner_dict = {"sweet potatoes":3, "peppers":4, "onions":1}

# COMMAND ----------

assert dinner_dict["sweet potatoes"] == 3, "We had 3 sweet potatoes"
assert dinner_dict["peppers"] == 4, "We had 4 peppers"
assert dinner_dict["onions"] == 1, "We had 1 onion"
print("Tests passed!")

# COMMAND ----------

# MAGIC %md <i18n value="01f79df2-b253-4e4d-949b-868d08287636"/>
# MAGIC
# MAGIC #### 問題2b：夕食の辞書の更新
# MAGIC
# MAGIC よくよく考えてみると、実は`sweet potatoes`は2本しかなかったのです。そして、認めたくはなかったが、`ice cream`も1つ食べました。
# MAGIC
# MAGIC それらの変更を反映させるために、辞書を更新してみてください。

# COMMAND ----------

# TODO
dinner_dict["sweet potatoes"] = 2
dinner_dict["ice cream"] = 1

# COMMAND ----------

# MAGIC %md <i18n value="ea6adf37-9c45-44fa-a1ae-9f3452f05db8"/>
# MAGIC
# MAGIC **回答をチェックする**

# COMMAND ----------

assert dinner_dict["sweet potatoes"] == 2, "We had 2 sweet potatoes"
assert dinner_dict["ice cream"] == 1, "We had 1 ice cream (but don't tell!)"
print("Tests passed!")

# COMMAND ----------

# MAGIC %md <i18n value="0d94c470-0a24-4071-8e23-d71d610eb80e"/>
# MAGIC
# MAGIC ### 問題3：セット
# MAGIC
# MAGIC プログラマーにとって非常に価値のあるスキルは、知らないデータ型のドキュメントを見て、その使い方を理解することができることです。 
# MAGIC
# MAGIC この演習では、 **Sets** という新しいコレクション型について学習していただきます。 
# MAGIC
# MAGIC <a href="https://docs.python.org/ja/3/tutorial/datastructures.html#sets" target="_blank">ここに</a>掲載されている資料を参考に、次の問題を完成させてください。
# MAGIC
# MAGIC 以下のセットを作成します：
# MAGIC * **`ingredient_set_1`** "carrots"、"onions"、"potatoes"が材料
# MAGIC * **`ingredient_set_2`** "broccoli"、"carrots"、"rice"が材料
# MAGIC * **`ingredient_3`** "sweet potatoes"、"carrots"、"corn"が材料
# MAGIC
# MAGIC  **`ingredient_intersection_set`** という、3つのセット全てに出現する成分のみを含む新しいセットをプログラムで作成します。

# COMMAND ----------

# ingredient sets
ingredient_set_1 = {"carrots", "onions", "potatoes"}
ingredient_set_2 = {"broccoli", "carrots", "rice"}
ingredient_set_3 = {"sweet potatoes", "carrots", "corn"}

# intersection set
ingredient_intersection_set = ingredient_set_1 & ingredient_set_2 & ingredient_set_3

# COMMAND ----------

# MAGIC %md <i18n value="4f4f2578-063d-41c5-bffb-3fefadbe7380"/>
# MAGIC
# MAGIC **回答をチェックする**

# COMMAND ----------

assert ingredient_intersection_set == {"carrots"}, "Only carrots occurs in all the ingredients"
assert "broccoli" in ingredient_set_2, "Did you forget your broccoli?"

print("Test passed!")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
