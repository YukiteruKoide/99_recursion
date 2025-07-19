# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="4db476c9-19cb-4f89-ba8b-105c88ebcdea"/>
# MAGIC
# MAGIC # 制御フロー (Control Flow)
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このLabでは<br>
# MAGIC
# MAGIC 前回のレッスンで学んだPythonの基本的な制御フローの概念を応用して、以下のようなことを行います：
# MAGIC
# MAGIC * **`if`** と **`else`** 文
# MAGIC * その他の論理演算子
# MAGIC * 型チェック

# COMMAND ----------

# MAGIC %md <i18n value="67b30eef-2bb7-405b-b750-905b74557169"/>
# MAGIC
# MAGIC ### 食べ物の提案 (Food Recommender)
# MAGIC
# MAGIC このラボでは、次のような食事の提案のための制御フローロジックを書きましょう。ユーザーは次のような入力を行います：
# MAGIC
# MAGIC *  **`temperature`** ：外気温を表す浮動小数点数（単位：華氏）
# MAGIC *  **`sunny`** :外の天気が良ければ **`True`** 、そうでなければ **`False`** に設定される真偽値。 
# MAGIC
# MAGIC 以下の提案を出力(print)するようなシステムを作成してください：
# MAGIC
# MAGIC * 外気温が60度以上あり、晴れている場合は、`ice cream`をお勧めします。
# MAGIC * 外気温が60度以上でも、晴れていなければ、`dumplings`をお勧めします。
# MAGIC * 60度以下であれば、天候に関係なく、`hot tea`をお勧めします。

# COMMAND ----------

# TODO
temperature = 50
sunny = True

if temperature >= 60 and sunny:
  print('ice cream')
elif temperature >= 60 and not sunny:
  print('dumplings')
else:
  print('hot tea')


# COMMAND ----------

# MAGIC %md <i18n value="50e00f9a-3fe3-41c6-8f52-d5526cb52e67"/>
# MAGIC
# MAGIC **`temperature`** と **`sunny`** の値を変えてみて、適切な食品を推奨しているかどうか確認してみてください。

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
