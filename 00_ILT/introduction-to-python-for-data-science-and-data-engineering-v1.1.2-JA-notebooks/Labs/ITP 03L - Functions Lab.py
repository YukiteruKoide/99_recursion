# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="344e9b62-1ae2-43aa-99d2-c7c01d2da834"/>
# MAGIC
# MAGIC # 関数（Functions）Lab
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このLabでは<br>
# MAGIC
# MAGIC 前回のレッスンで学んだ、以下のような概念を適用します：
# MAGIC * コードを再利用するための関数の定義と使用 
# MAGIC * **`help()`** 関数を呼び出して、関数について学ぶ

# COMMAND ----------

# MAGIC %md <i18n value="e2d725c2-2e5c-4f6f-b520-a4775b782efb"/>
# MAGIC
# MAGIC #### 問題1：偶数と奇数 (Problem 1: Even vs. Odd)
# MAGIC
# MAGIC まだ学んでいない便利な整数演算子として[剰余演算子(modulo)](https://www.w3schools.com/python/python_operators.asp)があります。これは記号 **`％`**　を使います。剰余演算子は，2つの整数の除算の余りを返します。
# MAGIC
# MAGIC 例えば **`12 % 7`** は **`5`** となりますが、12 を 7 で割ると 1 になり、余りが 5 になるからです。 
# MAGIC
# MAGIC 剰余演算子を使って 、整数 **`num`** を受け取り、偶数なら **`even`** を、それ以外の場合は **`odd`** を返す **`even_or_odd(num)`** という関数を書いてみましょう。偶数はすべて2で割り切れるので余りが0になることを覚えておいてください。  
# MAGIC
# MAGIC **ヒント** 以下のテストケースに合格するために、 **`print`** ではなく **`return`** を使うようにしてください。

# COMMAND ----------

12 % 7

# COMMAND ----------

# TODO

def even_or_odd(num):

  if num % 2 == 0:
    return "even"
  else:
    return "odd"

# COMMAND ----------

# MAGIC %md <i18n value="9bc17154-b90a-4197-a253-f217454795ba"/>
# MAGIC
# MAGIC **回答のチェック**

# COMMAND ----------

assert even_or_odd(2) == "even", "2 is an even number"
assert even_or_odd(42) == "even", "42 is an even number"
assert even_or_odd(1) == "odd", "1 is an odd number"
assert even_or_odd(327) == "odd", "327 is an odd number"
print("Test passed!")

# COMMAND ----------

# MAGIC %md <i18n value="0dfabbb0-d653-4330-9c4c-fb195bc54108"/>
# MAGIC
# MAGIC #### 問題2：Fizz Buzz (Problem 2: Fizz Buzz)
# MAGIC
# MAGIC 偶数と奇数の識別の基礎ができたので、その考えを発展させて、プログラミングの面接で最もよく聞かれる質問の1つであるFizz Buzzに取り組んでみることにしましょう。
# MAGIC
# MAGIC 整数を受け取って以下を実行する、 **`fizz_buzz`** という名前の関数を書いてください。 
# MAGIC
# MAGIC * 入力が整数でない場合(渡すべきでない場合でも間違った型を渡せてしまうことを思い出してください)、 **`"Wrong Type"`** を返します
# MAGIC * 与えられた整数の入力が、5で割り切れ、かつ3で割り切れない場合 **`"Fizz"`** を返します
# MAGIC * 3で割り切れるが5で割り切れない場合 **`"Buzz"`** を返します
# MAGIC * 3と5の両方で割り切れる場合 **`"FizzBuzz"`** を返します
# MAGIC * 3でも5でも割り切れない場合は、入力の数字そのものを返します
# MAGIC
# MAGIC
# MAGIC **ヒント** **`elif`** 文と **`%`** を使いたくなることでしょう。 
# MAGIC
# MAGIC それぞれの条件を確認する順番に注意してください。例えば、入力が整数であるかどうかをチェックしてから、何かで割り切れるかどうかをチェックする必要があります。

# COMMAND ----------


# def fizz_buzz(num: int) -> int:
#   if type(num) != int:
#     return "Wrong Type"
#   if num % 15 == 0:
#     return "FizzBuzz"
#   elif num % 5 == 0:
#     return "Fizz"
#   elif num % 3 == 0:
#     return "Buzz"
#   else:
#     return num
  
def fizz_buzz(num):
    if type(num) != int:
        return "Wrong type"
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Buzz"
    else:
        return num

# COMMAND ----------

# MAGIC %md <i18n value="83606571-52de-44d3-8552-b25632468989"/>
# MAGIC
# MAGIC **回答をチェックする**

# COMMAND ----------

assert fizz_buzz(15) == "FizzBuzz", "15 is divisible by both 5 and 3. Should return 'FizzBuzz'"
assert fizz_buzz(30) == "FizzBuzz", "30 is divisible by both 5 and 3. Should return 'FizzBuzz'"
assert fizz_buzz(5) == "Fizz", "5 is divisible by 5. Should return 'Fizz'"
assert fizz_buzz(25) == "Fizz", "25 is divisible by 5. Should return 'Fizz'"
assert fizz_buzz(3) == "Buzz", "3 is divisible by 3. Should return 'Buzz'"
assert fizz_buzz(81) == "Buzz", "81 is divisible by 3. Should return 'Buzz'"
assert fizz_buzz(23) == 23, "23 is not divisible by 3 or 5. Should return 23"
assert fizz_buzz(23.0) == "Wrong type", "Input is not an integer. Should return `Wrong type'"
assert fizz_buzz(True) == "Wrong type", "Input is not an integer. Should return `Wrong type'"
print("Test passed!")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
