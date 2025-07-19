# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="266e48b3-da9c-4871-bff6-de6a20af9379"/>
# MAGIC
# MAGIC # データ型と変数 (Data Types and Variables)
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは<br>
# MAGIC
# MAGIC - 以下のようなPythonの基本的な概念を探求します： 
# MAGIC     * データ型
# MAGIC     * 変数
# MAGIC     * 値の出力
# MAGIC    
# MAGIC 推奨されるリソース
# MAGIC * <a href="https://www.oreilly.co.jp/books/9784873118451/" target="_blank">Pythonによるデータ分析入門 (Wes McKinney著)</a>
# MAGIC * <a href="https://www.pythoncheatsheet.org/" target="_blank">Pythonリファレンスシート</a>
# MAGIC * <a href="https://docs.python.org/ja/3/tutorial/" target="_blank">Python公式チュートリアル</a>
# MAGIC
# MAGIC <a href="https://forums.databricks.com/static/markdown/help.html" target="_blank">markdownのセル</a>のドキュメント

# COMMAND ----------

# MAGIC %md <i18n value="ea37c4fe-4a41-4348-95b7-356b6516ab19"/>
# MAGIC
# MAGIC ### 計算 (Calculation)
# MAGIC
# MAGIC まずは、Pythonを使って、いくつかの数式を計算してみましょう。

# COMMAND ----------

1+1

# COMMAND ----------

# MAGIC %md <i18n value="ffaf9e58-9e73-4788-9ee9-bc72b7947bef"/>
# MAGIC
# MAGIC ### コメント (Comments)
# MAGIC
# MAGIC markdownのセルに加えて、[コメント](https://www.w3schools.com/python/python_comments.asp)によってコードに注釈を加えることができます。コメントは任意ですが、文脈の中でコード行の説明をするのに役立ちます。実行されることはありません。
# MAGIC
# MAGIC Pythonにおいて **`#`** はコメントを表す予約キーワードです。その行に続く文字は、コメントの一部として扱われます。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_24.png" alt="ヒント：">ノートブックのセルでコードの複数行を選択している場合、`ctrl + /`を押すと、そのコードブロックのコメントやアンコメントを行うことができます。以下に、ご自身のコメントを入れてみてください。

# COMMAND ----------

# This is our first line of Python code!
1+1

# COMMAND ----------

# MAGIC %md <i18n value="320b8d41-2b38-4158-ab74-ab765b41fc3a"/>
# MAGIC
# MAGIC ## データ型 (Data Types)
# MAGIC
# MAGIC Pythonは基本的な [**データ型**](https://www.w3schools.com/python/python_datatypes.asp)を提供し、それぞれに独自の操作を行うことができます。 
# MAGIC
# MAGIC そのいくつかと、それぞれに適用できる操作について見ていきましょう。

# COMMAND ----------

# MAGIC %md <i18n value="6ccd9a87-0eeb-48c5-a88b-8b2e7d5c3a04"/>
# MAGIC
# MAGIC ### データ型その１：整数 (Type1: Integers)
# MAGIC
# MAGIC 整数（int）は少数を含まない数値のことです。 
# MAGIC
# MAGIC **データ**：整数値（例：-2、-1、0、1、2...）
# MAGIC
# MAGIC **操作の例**：+、-、\*、/

# COMMAND ----------

# Integer expression
2 * 3 + 5 - 1

# COMMAND ----------

# MAGIC %md <i18n value="2761447d-8388-4c05-a989-c33fb441f19d"/>
# MAGIC
# MAGIC ### データ型その２：浮動小数点数 (Type2: Float)
# MAGIC
# MAGIC 浮動小数点数（float）とは、小数を含む数値のことです。 
# MAGIC
# MAGIC **データ**：小数を含む数値（例：-2.342、-1.3、0.45、1.1、2.2 ...)
# MAGIC
# MAGIC **操作の例**：+、-、\*、/

# COMMAND ----------

1.2 * 2.3 + 5.5

# COMMAND ----------

# MAGIC %md <i18n value="e0e8ddc7-7b39-43fc-b3d0-0f0ca04fba86"/>
# MAGIC
# MAGIC もし何かの型かわからない場合は、それを **`type()`** に渡してみましょう。

# COMMAND ----------

type(1.2)

# COMMAND ----------

# MAGIC %md <i18n value="cb9195f7-0b63-4fae-8591-cf11bbd126f1"/>
# MAGIC
# MAGIC 問題：`1.`は浮動小数点数でしょうか、整数でしょうか？その型を確認することでテストしてみましょう。

# COMMAND ----------

type(1.)

# COMMAND ----------

# MAGIC %md <i18n value="91074620-9816-473f-b513-0fe927585dd7"/>
# MAGIC
# MAGIC ### データ型その３：文字列 (Type3: Strings)
# MAGIC
# MAGIC 文字列（str）は、引用符（すなわち **`""`** または **`''`** )で囲まれた文字の列です。単なるテキストですが、数字や句読点などを含むことができます。
# MAGIC
# MAGIC 例えば、`"Hello World！"`または`'Hello World！'`です。
# MAGIC
# MAGIC **データ**：テキスト（例"Hello"、"I love Python"、"3.14abc")
# MAGIC
# MAGIC **操作の例**：結合 (+)
# MAGIC
# MAGIC 整数や浮動小数点数に`+`演算子を使うと値が加算されますが、文字列の場合は結合されることに注意してください。データ型によって操作が異なります。

# COMMAND ----------

# String expression
"Hello" + "123"

# COMMAND ----------

# MAGIC %md <i18n value="d71e6c1e-14c6-4d5e-9e33-2ef510c3780a"/>
# MAGIC
# MAGIC 結合操作では、スペースは挿入され**ない**ことに注意してください。もし"Hello 123"としたい場合は、文字列の中にスペースを入れなければなりません。

# COMMAND ----------

# String expression with a space
"Hello" + " " + "123"

# COMMAND ----------

# MAGIC %md <i18n value="d00a31cd-6762-4c37-b09d-fd626f20a36a"/>
# MAGIC
# MAGIC 問題：浮動小数点数と文字列を足すと、どんな結果になるのでしょうか？以下のコードをアンコメントして実行してみてください。

# COMMAND ----------

# "Hello" + 123

# COMMAND ----------

# MAGIC %md <i18n value="6f69c9be-49dc-44f7-abbf-52ea2e8de36e"/>
# MAGIC
# MAGIC ### データ型その４：真偽値 (Type 4: Boolean)
# MAGIC
# MAGIC 真偽値（bool）は2値のデータ型です。 **`True`** と **`False`** の2つの真偽値があるだけです。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_warn_24.png" alt="注意">Pythonは大文字と小文字を区別するので、これら真偽値は先頭のみ大文字でなければなりません。 **`true`** や **`FALSE`** のような変数を使おうとするとPythonのエラーとなります。
# MAGIC
# MAGIC **データ**：True、False
# MAGIC
# MAGIC **操作の例**：論理演算（or、and、not など）

# COMMAND ----------

True or False

# COMMAND ----------

True and False

# COMMAND ----------

not False

# COMMAND ----------

# MAGIC %md <i18n value="d9f7c5fe-f1e6-408a-be83-4b6b33936f5f"/>
# MAGIC
# MAGIC ## 変数 (Variables)
# MAGIC
# MAGIC ある式の結果を[変数](https://www.w3schools.com/python/python_variables.asp)に格納し、その変数を用いてその式の結果を参照することができるのです。同じ値を何度も再利用する予定がある場合、非常に便利です。変数の代入は1行に1つだけにしてください。
# MAGIC
# MAGIC **`variable_name = expression`**
# MAGIC
# MAGIC <a href="https://www.w3schools.com/python/gloss_python_variable_names.asp#:~:text=Rules%20for%20Python%20variables%3A,0%2D9%2C%20and%20_%20" target="_blank">W3 Schools</a>からPython変数名に関するいくつかの注意点です。
# MAGIC * 変数名は文字かアンダースコアで始めなければならない 
# MAGIC * 変数名は数字で始めることはできない 
# MAGIC * 変数名には英数字とアンダースコア (A-z、0-9、_ ) しか使えない 
# MAGIC * 変数名は大文字と小文字を区別する ( **`age`** 、 **`Age`**、**`AGE`** は3つの異なる変数です)

# COMMAND ----------

a = 3
b = 2
c = a*b

c

# COMMAND ----------

# MAGIC %md <i18n value="53daff57-613e-41eb-b552-847085596e94"/>
# MAGIC
# MAGIC 問題： **`b`** の値を更新すると **`c`** はどうなるでしょう?

# COMMAND ----------

b = 4
c

# COMMAND ----------

# MAGIC %md <i18n value="ca3ddabd-7b46-4e00-8abc-21633d3f6e6a"/>
# MAGIC
# MAGIC ### 変数の状態 (Variable State)
# MAGIC
# MAGIC 変数は、同じノートブック内のセルにまたがってアクセスできます。クラスタを再起動したり、クラスタからノートブックをデタッチ(detach)したりすると、コードは失われませんが、変数の状態は失われます。 
# MAGIC
# MAGIC **練習**：このノートをデタッチ(detach)して、再アタッチ(reatach)してみてください。それでも上記のコマンドを正常に実行できますか？

# COMMAND ----------

# MAGIC %md <i18n value="a95f37de-1376-49d8-bd9a-a434561608f3"/>
# MAGIC
# MAGIC ### 弱い型付け言語 (Weakly Typed Languages)
# MAGIC
# MAGIC
# MAGIC Pythonは*弱い型付け*言語です。つまり、どんな変数もどんなデータ型の値でも保持することができ、変数を上書きしてどんなデータ型の値でも持つことができるのです。つまり、変数に、元の値とは異なるデータ型の新しい値を代入することができるのです。
# MAGIC
# MAGIC 一方、C言語やJavaなどの*強い型付け*言語では、このようなことはできません。

# COMMAND ----------

b = "Hello World"
b

# COMMAND ----------

# MAGIC %md <i18n value="79b5dfd2-134e-419f-8086-72d76d0bdd80"/>
# MAGIC
# MAGIC ### 命名規則 (Naming Conventions)
# MAGIC
# MAGIC Python の変数はほとんどどのようにでも命名できますが、変数名には **`snake_case`** を使うのがPython の一般的な規則です。つまり、文字はすべて小文字にし、スペースは`_`文字に置き換えます。
# MAGIC
# MAGIC 例えば **`my_first_variable`** は **`MyFirst_variable`** より良い変数名です。 
# MAGIC
# MAGIC 変数の再利用は避けるようにしましょう。例えば、家の住所を指す変数名として **`address`** を使用し、その後でIPアドレスを指すものとして **`address`** を使用したくはならないでしょう。その代わりに **`house_address`** と **`ip_address`** を使いたいところです。
# MAGIC
# MAGIC また、Pythonのコードを読みやすく、理解しやすくするために、内容を説明するような変数名をつけるようにしましょう。
# MAGIC
# MAGIC また、長すぎる変数名は使わないでください。あなたは本当にプログラムの中で **`first_appearance_of_the_word_in_this_file`** を何度も入力したいと思いますか？

# COMMAND ----------

my_first_variable = 2

# COMMAND ----------

# MAGIC %md <i18n value="1fc8e260-5dd1-4b1f-87b5-23b1469eae3e"/>
# MAGIC
# MAGIC ## Print文 (Print Statements)
# MAGIC
# MAGIC DatabricksやJupyterノートブックでは、セル内で最後に実行された行の結果が自動的に出力されます。
# MAGIC
# MAGIC 最後の行の評価以外のものを出力させたい場合は **`print`** 文を使う必要があります。
# MAGIC
# MAGIC 使用するには、次のように書きます。 **`print(式)`** と書くと、式の値が表示されます。

# COMMAND ----------

a = 1
b = 2

a # This line isn't printed because it's not the last line of code
b

# COMMAND ----------

print(a)
print(b)

# COMMAND ----------

# MAGIC %md <i18n value="7f5bcd26-b2d4-4085-9215-df0c7613cb6f"/>
# MAGIC
# MAGIC 変数の値の出力のほか、文字列の出力も可能です。

# COMMAND ----------

print("Hello world")

# COMMAND ----------

# MAGIC %md <i18n value="748550c6-43bd-4265-9cff-420420ab476d"/>
# MAGIC
# MAGIC #### f-stringでの書式設定 (f-string Formatting)
# MAGIC
# MAGIC また、[f-string](https://www.w3schools.com/python/python_string_formatting.asp)書式設定により、変数と文字列を一緒に出力することができます。引用符の前に、 **`f`** をつけ変数を中括弧で囲んでください。構文は次のようになります。 **`f "optional text {insert_variable_here} optional text"`** 。

# COMMAND ----------

name = "Robin"
age = 30

print(f"My name is {name} and I am {age} years old")

# COMMAND ----------

# MAGIC %md <i18n value="973e1c76-964d-41f4-894f-98bad1ffb5b1"/>
# MAGIC
# MAGIC **おめでとうございます。Pythonの最初のレッスンが終了しました!**

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
