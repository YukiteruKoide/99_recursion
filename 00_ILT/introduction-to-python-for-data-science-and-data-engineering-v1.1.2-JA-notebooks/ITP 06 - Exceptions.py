# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="98014313-352a-4426-b032-c0c48f96180a"/>
# MAGIC
# MAGIC # エラーと例外 (Errors and Exceptions)
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは<br>
# MAGIC
# MAGIC - エラーと例外を学びます
# MAGIC - assert文をレビューします
# MAGIC - 例外処理にtry-catchを適用します

# COMMAND ----------

# MAGIC %md <i18n value="069b8442-7d9f-4418-8bc2-6426248ee458"/>
# MAGIC
# MAGIC ### 構文エラー (Syntax Errors)
# MAGIC
# MAGIC Pythonでは、主に2種類のエラーが存在します。構文エラーと例外です。構文エラーは、コードが不正確にタイプされ、Pythonがそれをどのように解釈するかわからないために投げられるエラーです。 
# MAGIC
# MAGIC 以下の例は、構文エラーを示しています。

# COMMAND ----------

# if print("Hello World") # This is not correct Python code, so it throws a Syntax Error

# COMMAND ----------

# MAGIC %md <i18n value="6fdcf2ae-e9d7-4686-81d7-eec2c9141af1"/>
# MAGIC
# MAGIC ### 例外 (Exceptions)
# MAGIC
# MAGIC Pythonが実行する方法がわかるように適切にフォーマットされたコードがあったとしても、コードが実行される際にエラーに遭遇する可能性があります。このように、コードの実行中に発生するエラーを例外と呼びます。Pythonは私たちがやろうとしていることを理解してくれたが、問題があることを示しています。
# MAGIC
# MAGIC 以下は、例外が起こる例です。

# COMMAND ----------

#  1 / 0

# COMMAND ----------

# MAGIC %md <i18n value="7dea8495-1d7e-448b-bd22-16f243bc753c"/>
# MAGIC
# MAGIC 今回、 **`ZeroDivisionError`** を観察しましたが、これは、ゼロで割ろうとしており、それは定義されていないことを示します。Pythonが提供する例外には、さまざまな問題を示すものがあり、組み込みの例外の全リストは[ここに](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)あります。

# COMMAND ----------

# MAGIC %md <i18n value="215acf78-5049-40ff-b7b5-1050a889b315"/>
# MAGIC
# MAGIC ### 例外処理 (Exception Handling)
# MAGIC
# MAGIC 構文エラーは常にプログラムを終了させ、失敗させますが、Pythonでは例外を処理することができます。これにより、コードブロックを実行しようとしたときに、Pythonが例外や特定の例外に遭遇した場合に何をするかをプログラムすることができます。Pythonで例外を処理するために、 **`try`** 文を使用します。 
# MAGIC
# MAGIC **`try`** 文は以下のように記述します。
# MAGIC
# MAGIC ``` 
# MAGIC try: 
# MAGIC 　　　　code block 
# MAGIC except: 
# MAGIC 　　　　code block
# MAGIC ```
# MAGIC
# MAGIC Pythonが **`try`** 文に出会うと、まず最初に **`try`** コードブロックのコードを実行しようとします。例外に遭遇した場合、これまで見てきたように終了してエラーになるのではなく、代わりに **`except`** 内のコードブロックを実行します。

# COMMAND ----------

try:
    1/0 # Throws an exception
except:
    print("Exception Handled")

# COMMAND ----------

# MAGIC %md <i18n value="daba1041-3381-4a20-9aa5-ee991c67ce4d"/>
# MAGIC
# MAGIC この最後の例では **`try`** ブロックの中で何らかの例外が発生した場合 **`except`** ブロックを実行します。ある特定の例外だけを処理したい場合は、次のように **`except`** キーワードの後にその例外を書きます。
# MAGIC
# MAGIC ```
# MAGIC try:
# MAGIC 　　　　code block
# MAGIC except ExceptionName:
# MAGIC 　　　　code block
# MAGIC ```

# COMMAND ----------

try:
    1/0 # Throws a ZeroDivisionError exception
except ZeroDivisionError:
    print("Exception Handled")

# COMMAND ----------

# try:
#     print(undefined_variable) # Throws a Name Error exception
# except ZeroDivisionError:
#     print("Exception Handled")

# COMMAND ----------

# MAGIC %md <i18n value="9ae04843-cd61-4ba7-9136-6c7c04717982"/>
# MAGIC
# MAGIC もし、複数の特定の例外を処理したい場合は、括弧の中にカンマで区切って一連の例外を記述することができます。 
# MAGIC
# MAGIC 以下の例外発生行を片方ずつコメントアウトしてみて、両方の例外が処理されることに注目してください。

# COMMAND ----------

try:
    1/0 # Throws a ZeroDivisionError exception
    print(undefined_variable) # Throws a Name Error exception
except (ZeroDivisionError, NameError):
    print("Exception Handled")

# COMMAND ----------

# MAGIC %md <i18n value="0ce9ca24-9951-488d-970e-8acbeb86b750"/>
# MAGIC
# MAGIC これにより、ZeroDivisionErrorとNameErrorの両方の例外が処理されるようになりました。

# COMMAND ----------

# MAGIC %md <i18n value="2cbcc8d4-fc13-434f-a1df-1b82a9f7a46c"/>
# MAGIC
# MAGIC ### アサーションエラー (Assertion Error)
# MAGIC
# MAGIC 非常に便利な例外の1つが **`AssertionError`** です。 **`assert`** 文を使って **`AssertionErrors`** を発生させることができます。このコースでは、これらを使ってあなたのラボのコードをチェックしています。 **`assert`** 文は以下のようなものです：
# MAGIC
# MAGIC ``` assert boolean expression, optional message```
# MAGIC
# MAGIC Pythonがこの文を実行すると、最初に論理式(boolean expression)が評価されます。これが **`True`** であれば、Pythonは何もせず、次に進みます。もし **`False`** である場合、オプションのメッセージが指定されていればそれも含めて、AssertionError が投げられます。

# COMMAND ----------

# assert 1 == 1
# assert 1 == 2, "That is not true"

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
