# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="7dbd79c5-128b-44de-bfdf-f4ee82cb7df7"/>
# MAGIC
# MAGIC # ループ(Loop) Lab
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このLabでは<br>
# MAGIC
# MAGIC 前回のレッスンで学んだ、以下のような概念を適用します：
# MAGIC * より高度な制御フローを処理するためのforループの利用
# MAGIC * リストをフィルタリングするためのリスト内包表記の利用

# COMMAND ----------

# MAGIC %md <i18n value="c53aee76-7759-4783-b8cc-c615c9db8637"/>
# MAGIC
# MAGIC ## 練習問題：バート・シンプソン、居残り
# MAGIC
# MAGIC <img src="https://preview.redd.it/386z0p2eh5v21.jpg?auto=webp&s=383ef3536776dc3a34515e6cfd9979f363570a05" width="40%" height="20%">
# MAGIC
# MAGIC バート・シンプソンがまた居残りさせられてます...。彼は **`I will not let my dog eat my homework`** と50回書く必要があります。もちろん、バートは怠け者なので、Pythonでこれを自動化するためにあなたの助けが必要です。 
# MAGIC
# MAGIC **`detention_message`** と **`num_lines`** という、それぞれバートが書く必要のあるメッセージとその回数を引数とする、 **`detention_helper()`** という関数を書きましょう。 
# MAGIC
# MAGIC この関数は **`detention_message`** を **`num_lines`** 回出力します。ただし **`detention_message`** には番号を付けなければなりません。 
# MAGIC
# MAGIC 例えば **`detention_message`** が`I will not let my dog eat my homework`、そして **`num_lines`** が50の場合、関数は次のものをprintします。
# MAGIC
# MAGIC `1.I will not let my dog eat my homework`
# MAGIC
# MAGIC `2.I will not let my dog eat my homework`
# MAGIC
# MAGIC `3.I will not let my dog eat my homework`
# MAGIC
# MAGIC `. . .`
# MAGIC
# MAGIC `50.I will not let my dog eat my homework`
# MAGIC
# MAGIC
# MAGIC ここで私たちは **`detention_message`** と **`num_lines`** をパラメータ化し、彼が再び居残りをする場合に備えます。
# MAGIC
# MAGIC **ヒント**： **`range()`** 関数を思い出してください。ただし、0ではなく1から数え始める必要があります。また、f-stringのフォーマットも役に立ちます。

# COMMAND ----------

def detention_helper(detention_message, num_lines):
    for i in range(num_lines):
        print(f"{i+1}. {detention_message}")

# COMMAND ----------

# MAGIC %md <i18n value="7c5729b0-a8b5-4122-8574-44fa9053877c"/>
# MAGIC
# MAGIC バートの現在の居残り状況に応じた正しい入力で以下の関数を呼び出し、問題文にあるように「I will not let my dog eat my homework」が行番号付きで50回プリントアウトされるのを確認してください。

# COMMAND ----------

# TODO
detention_helper("I will not let my dog eat my homework", 50)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
