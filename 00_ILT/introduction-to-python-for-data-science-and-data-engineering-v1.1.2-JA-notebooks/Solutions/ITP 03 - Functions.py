# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="65df298d-79ae-4ce6-9e3a-b736cde03178"/>
# MAGIC
# MAGIC # 関数 (Functions)
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは<br>
# MAGIC * コードを再利用するための関数の定義と使用をします
# MAGIC   * 引数
# MAGIC   * 型ヒント
# MAGIC *  **`help()`** 関数を呼び出します

# COMMAND ----------

# MAGIC %md <i18n value="568cdf5f-5b84-4bf8-8709-4b58765d2640"/>
# MAGIC
# MAGIC ## 関数 (Functions)
# MAGIC
# MAGIC このレッスンでは、<a href="https://www.w3schools.com/python/python_functions.asp" target="_blank">関数</a>を使用してコードを再利用可能にする方法について説明します。
# MAGIC
# MAGIC 以下のように関数を定義します。
# MAGIC
# MAGIC       def function_name(parameters):
# MAGIC           function_code
# MAGIC
# MAGIC
# MAGIC **`def`** キーワードに注目してください。それに続いて、関数名、括弧内にパラメータ、そしてコロンがあることに注意してください。 
# MAGIC
# MAGIC 実はもう関数は使っています。 **`print()`** はPythonであらかじめ定義されている関数です。

# COMMAND ----------

print(1)

# COMMAND ----------

# MAGIC %md <i18n value="d8d44355-44a5-40a3-b8aa-30931e08d346"/>
# MAGIC
# MAGIC Pythonがコードを実行するとき、関数への呼び出しを見つけると、関数定義の中のコードブロックにジャンプしてそのコードを実行し、関数が呼び出された場所にジャンプして戻り、中断したところから再開します。 
# MAGIC
# MAGIC パラメータを持たない簡単なサンプル関数を書いてみましょう。
# MAGIC
# MAGIC 例えば、10USドルを持っていて、USドルからユーロへの換算をしたいとします。このレッスンを書いている時点では、1ドルはおよそ **0.93** ユーロです。

# COMMAND ----------

def ten_dollars_to_euros():
    print(10.0 * 0.93)
    
ten_dollars_to_euros()

# COMMAND ----------

# MAGIC %md <i18n value="1a38c434-5f42-44fc-9338-b3d92a94548e"/>
# MAGIC
# MAGIC 関数の中にあるコードブロックをインデントしていることに注目してください。**if文**と同じように、どのようなコードが関数内に属するかをPythonに伝えなければなりません。 **`タブ`** を使ってインデントを作成することを思い出してください。
# MAGIC
# MAGIC 次のように関数を呼び出すことができます。この最初の例では**引数**ないので、今は無視します。 
# MAGIC
# MAGIC ``` function_name(arguments) ```

# COMMAND ----------

print("Python ran this line before the function body")

ten_dollars_to_euros()

print("Python ran this line after the function body")

# COMMAND ----------

# MAGIC %md <i18n value="7511c94b-96a6-462c-89d6-af36b14548d7"/>
# MAGIC
# MAGIC ### パラメータ (Parameters)
# MAGIC
# MAGIC 多くの場合、関数に何らかの入力を取り込みたいものです。パラメータは変数であり、関数が実際に必要とする値の仮の名前です。 
# MAGIC
# MAGIC ドルからユーロへの換算の例で考えてみましょう。10ドルをユーロに変換する機能だけでなく、任意のドル額を渡してユーロに変換する機能があれば、より良いですね。 
# MAGIC
# MAGIC 変換したい **`dollar_amount`** を表すパラメータを持つことで、それができます

# COMMAND ----------

def dollars_to_euros(dollar_amount):
    print(dollar_amount * 0.93)

# COMMAND ----------

# MAGIC %md <i18n value="4c927ca4-1ba3-4ee8-a691-9c4a421c99ee"/>
# MAGIC
# MAGIC ### 引数 (Arguments)
# MAGIC
# MAGIC 関数にパラメータがある場合、パラメータにどのような値を持たせるかを指定する必要があります。今回の例では、 **`dollar_amount`** パラメータに値を指定する必要があります。 **`print()`** に、表示するための値を指定したときと同じように、関数を呼ぶ時に括弧の中に値を入れます。
# MAGIC
# MAGIC 関数に渡す値は[**引数**](https://www.w3schools.com/python/gloss_python_function_arguments.asp)と呼ばれています。つまり **`dollars_to_euros(5)`** を実行する時は **`dollar_amount`** パラメータに **`5`** という値を代入し、関数のコードを実行します。

# COMMAND ----------

dollars_to_euros(5.0)
dollars_to_euros(10)
dollars_to_euros(20.0)

# COMMAND ----------

# MAGIC %md <i18n value="fddb317f-15f3-44ea-bd84-2a05d88b80f4"/>
# MAGIC
# MAGIC ### 複数のパラメータ (Multiple Parameters)
# MAGIC
# MAGIC カンマで区切って複数のパラメータを定義することで、複数のパラメータを持つ関数を作成することができます。
# MAGIC
# MAGIC 為替レートが将来的に変更されることを想定して、この関数を呼び出すときに、 **`dollar_amount`** に加えて、 **`conversion_rate`** を指定してみましょう。

# COMMAND ----------

def dollars_to_euros_with_rate(dollar_amount, conversion_rate):
    print(dollar_amount * conversion_rate)

# COMMAND ----------

# MAGIC %md <i18n value="19d2ba46-1dd6-48f6-b538-103e590886c4"/>
# MAGIC
# MAGIC この新しい関数を呼び出す際には、関数の各パラメータに対する値をカンマで区切って指定する必要があります。

# COMMAND ----------

dollars_to_euros_with_rate(10.0, 0.93)
dollars_to_euros_with_rate(5.0, 1.0)
# dollars_to_euros_with_rate(5.0) # This will error

# COMMAND ----------

# MAGIC %md <i18n value="4e5652da-d220-4ca9-9e79-43913bcab298"/>
# MAGIC
# MAGIC #### キーワード引数 (Named Invocation)
# MAGIC
# MAGIC ほとんどの場合、関数に引数を渡すときは、上でやったようにします。一連の引数を与えると、それらは同じ順序で関数のパラメータに代入されます。
# MAGIC
# MAGIC **`dollars_to_euros_with_rate(10, 0.93)`** という呼び出しでは、 **`dollar_amount`** には **`10`** が代入されます。なぜなら **`dollar_amount`** が最初のパラメータであり **`10`** は最初の引数だからです。次に **`conversion_rate = 0.93`** となりますが、これはそれぞれ2番目のパラメータと引数だからです。
# MAGIC
# MAGIC 以下のように、パラメータの名前を明示的に指定して引数を関数に渡すことができます。これはあまり一般的ではありませんが、この方法で行えば、引数の渡される順番は問題になりません。

# COMMAND ----------

dollars_to_euros_with_rate(dollar_amount=10.0, conversion_rate=0.93)
dollars_to_euros_with_rate(conversion_rate=0.93, dollar_amount=10.0)

# COMMAND ----------

# MAGIC %md <i18n value="6bdc03a2-ebb6-4b4d-b5dd-032a434d9694"/>
# MAGIC
# MAGIC ### パラメータのデフォルト値 (Default Parameter Values)
# MAGIC
# MAGIC パラメータに[デフォルト値](https://www.w3schools.com/python/gloss_python_function_default_parameter.asp)を設定しておくと便利な場合があります。 
# MAGIC
# MAGIC ドルからユーロへの変換の例では、特に指定がない限り、 現在の為替レートである **`0.93`** を **`conversion_rate`** に使いたいと思うかもしれません。 
# MAGIC
# MAGIC 以下のようにパラメータにデフォルト値を定義することができます。 
# MAGIC
# MAGIC ``` 
# MAGIC def func(params, param=default_value):
# MAGIC     code
# MAGIC ```

# COMMAND ----------

def dollar_to_euro_with_default(dollar_amount, conversion_rate=0.93):
    print(dollar_amount * conversion_rate)

# COMMAND ----------

# MAGIC %md <i18n value="58cec573-c5dd-48cb-8276-a92362f460f5"/>
# MAGIC
# MAGIC さて，この関数を呼び出すとき，もし **`conversion_rate`** に引数を指定しなければ、 **`0.93`** としてセットされます。

# COMMAND ----------

dollar_to_euro_with_default(10.0)
dollar_to_euro_with_default(10.0, 0.5)

# COMMAND ----------

# MAGIC %md <i18n value="95f77560-18ee-44d0-8b8d-1f3648916c31"/>
# MAGIC
# MAGIC ### 関数の出力 (Function Output)
# MAGIC
# MAGIC ここまでのところ、定義した関数はすべて値を表示するだけです。式として評価すると、有用な結果が出力されないことがわかります。

# COMMAND ----------

a = dollar_to_euro_with_default(10.0)
print(a)

# COMMAND ----------

# MAGIC %md <i18n value="02f39e81-a952-4b78-a668-258e8e4b406f"/>
# MAGIC
# MAGIC この関数は実行され、関数本体が実行されている間は9.3と表示されますが、Pythonに関数を式として評価させようとすると、 **`None`** と評価されます。 **`None`** は、何もないことを表す特殊なデータ型です。 
# MAGIC
# MAGIC Pythonに、関数を現在表示している値を表す式のように評価してもらいたい場合は [**return**](https://www.w3schools.com/python/ref_keyword_return.asp)キーワードを使う必要があります。

# COMMAND ----------

def dollar_to_euro_with_default(dollar_amount, conversion_rate=0.93):
    return dollar_amount * conversion_rate
    

# COMMAND ----------

a = dollar_to_euro_with_default(10.0)
print(a)

# COMMAND ----------

# MAGIC %md <i18n value="97416e6a-ea97-453c-b6a9-79d314c037d6"/>
# MAGIC
# MAGIC さて、 **`return`** キーワードによりPythonは、 **`10.0 * 0.93`** を **`0.93`** と評価するのと同じように **`dollar_to_euro_with_default(10.0)`** を **`0.93`** と評価します。 関数の外部で使用するために関数に生成させたいものはすべて **`return`** の後ろにつける必要があります。Pythonが関数の中の **`return`** に達すると、その関数を終了し、中断していた場所にジャンプします。

# COMMAND ----------

# MAGIC %md <i18n value="aa8d0e9c-37c2-4664-a34d-f10b8d125887"/>
# MAGIC
# MAGIC ### 型ヒント (Type Hints)
# MAGIC
# MAGIC たとえ、その関数が特定のデータ型に対してのみ動作するように書かれていたとしても、関数の引数として任意な型を渡すことができることに注意してください。
# MAGIC
# MAGIC 例えば、Pythonでは **`dollars_to_euros_with_default(True, "abc")`** を呼び出すことができますが、真偽値と文字列との間の乗算が定義されていないため、失敗します。
# MAGIC
# MAGIC この問題に対応するため、関数に[型ヒント](https://docs.python.org/3/library/typing.html)を追加することができます。
# MAGIC
# MAGIC これは，以下のように，パラメータに、コロン、オプションのスペース、データ型を追加することで実現されます。 **`dollar_amount: float`** 。戻り値のデータ型は関数定義行の最後のコロンの前にハイフン、大なり記号、データ型を付けて示すことができます。 **`-> str:`**
# MAGIC
# MAGIC 例えば **`dollars_to_euros_with_default`** が浮動小数点数のみを扱い、浮動小数点数を返すことを示したい場合は、以下のように記述します。

# COMMAND ----------

def dollar_to_euro_with_default(dollar_amount: float, conversion_rate: float = 0.93) -> float:
    return dollar_amount * conversion_rate

# COMMAND ----------

# MAGIC %md <i18n value="39b419fb-8600-4ae3-8b0e-f8019137fde8"/>
# MAGIC
# MAGIC これらの型ヒントに強制力がないことに注意することが重要です。これらはデータ型がそうあるべきことを示すヒントですが、それでも間違った型を関数に渡すと、それを実行しようとします。 
# MAGIC
# MAGIC 主な利点は可読性を高めることであり、コーディング環境によってはエラーを早期に検出するために使用することも可能です。

# COMMAND ----------

# MAGIC %md <i18n value="5c6b9dd2-f667-4272-a2c9-6ecce31df1de"/>
# MAGIC
# MAGIC ### Docstrings
# MAGIC
# MAGIC ドキュメント化により、あなたのコードをよりよく整理し、他の人がより理解しやすいようにできます。コードをドキュメント化する一般的な方法として [**docstring**](https://www.geeksforgeeks.org/help-function-in-python/)があります。 
# MAGIC
# MAGIC docstringは、以下のように3つの引用符の間に置かれる特別なコメントです。関数のドキュメント化にdocstringを使用するには、関数コードの前の関数本体に配置します。

# COMMAND ----------

def dollar_to_euro_with_default(dollar_amount: float, conversion_rate: float = 0.93) -> float:
    """
    Returns Dollar amount to Euros based on a conversion rate
    
    Parameters:
        dollar_amount (float): Dollar amount to be converted to euros
        conversion_rate (float): Dollar to Euro conversion rate. Default:0.93
    
    Returns:
         euro_amount (float): Euro equivalent of Dollar amount based on conversion rate
         """
    euro_amount = dollar_amount * conversion_rate
    return euro_amount

# COMMAND ----------

# MAGIC %md <i18n value="cd94ab20-f634-4dbf-812e-f885691db238"/>
# MAGIC
# MAGIC docstringはコメントとは異なり、Pythonでは属性として保存されます。組み込み関数の **`help()`** は docstring にアクセスし、それを表示します。

# COMMAND ----------

help(dollar_to_euro_with_default)

# COMMAND ----------

# MAGIC %md <i18n value="d5f90617-6c63-4a02-b1c4-af90e815e4a0"/>
# MAGIC
# MAGIC ### スコープ (Scope)
# MAGIC
# MAGIC Pythonでは、コードの特定の領域で定義された変数は、同じ領域内でのみアクセス可能です。これを[スコープ](https://www.w3schools.com/python/python_scope.asp)といいます。 
# MAGIC
# MAGIC 注目すべきは、関数内で定義された変数は、関数内ではアクセス可能ですが、関数外ではアクセスできないことです。つまり、変数のスコープは、その変数が定義された関数内に限定されます。

# COMMAND ----------

def function():
    func_variable = 1
    return func_variable

# COMMAND ----------

function()
# func_variable # Uncomment and this will error

# COMMAND ----------

# MAGIC %md <i18n value="00c7e6a3-c466-4242-8d25-c60efacc9175"/>
# MAGIC
# MAGIC ### 組み込み関数 (Built-in Functions)
# MAGIC
# MAGIC Pythonは、一般的な操作のための<a href="https://docs.python.org/3/library/functions.html" target="_blank">組み込み関数</a>をいくつか提供しています。 
# MAGIC
# MAGIC 注目すべきものとして、すでに見てきた **`print()`** 、 入力の最大値を返す **`max()`** 、入力の長さを返す **`len()`** があります。

# COMMAND ----------

# 2 > 1
print(max(1, 2))

# "abc" is 3 characters long
print(len("abc"))

# COMMAND ----------

# MAGIC %md <i18n value="8dca298f-3225-4e6e-b8ad-e84c72c53f46"/>
# MAGIC
# MAGIC **`help()`** を呼び出すと、組み込み関数のドキュメントを見ることができます。

# COMMAND ----------

help(max)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
