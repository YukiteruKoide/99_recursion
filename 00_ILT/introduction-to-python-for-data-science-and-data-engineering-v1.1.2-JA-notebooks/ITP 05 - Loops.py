# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="13cdba3e-bd9b-441f-9202-12e26ce9135f"/>
# MAGIC
# MAGIC # ループ (Loops)
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは<br>
# MAGIC
# MAGIC - 制御フローを変える新しい方法、forループを探ります
# MAGIC - リストの絞り込みのためにforループを使います

# COMMAND ----------

# MAGIC %md <i18n value="f5c07310-2b29-4266-9ec2-9b239ebae74f"/>
# MAGIC
# MAGIC ### forループ (For-loops)
# MAGIC
# MAGIC ループは、あるシーケンスに沿って、コードのブロックを繰り返し実行する方法です。
# MAGIC
# MAGIC [**Forループ**](https://www.w3schools.com/python/python_for_loops.asp)を次のように書きます：
# MAGIC
# MAGIC ```
# MAGIC for var_name in list:
# MAGIC     code_block 
# MAGIC ```
# MAGIC
# MAGIC Pythonはリスト内の項目ごとに **`code_block`**　のコードを実行します。リストの先頭から順に **`var_name`**　を毎回、リストの次の項目に割り当てます。

# COMMAND ----------

# MAGIC %md <i18n value="ac31dae5-adc1-4167-b689-87d6bce353e2"/>
# MAGIC
# MAGIC コードがループするたびに **`var_name`**　（以下の例では **`number`**　）は、リストの次の項目の値に設定されます。 
# MAGIC
# MAGIC ステップごとに分解して見てみましょう：
# MAGIC
# MAGIC ステップ1 **`number = 0`**　、リストの最初の要素であり　**`0`**　がセットされて出力されます。
# MAGIC
# MAGIC ステップ2 **`number`**　をリストの次の要素が設定されるので、 **`number = 1`**　となり **`1`**　が出力されます。
# MAGIC
# MAGIC ステップ3 **`number`**　を再びリストの次の要素が設定されるので **`number = 2`**　となり **`2`**　が出力されます。
# MAGIC
# MAGIC これにより、リスト内のすべての項目に対して **`for`**　ループのコードを実行することができます。

# COMMAND ----------

for number in [0, 1, 2]:
    print(number)

# COMMAND ----------

# MAGIC %md <i18n value="90b9748a-7ecc-440c-98ca-5acde97b5212"/>
# MAGIC
# MAGIC コードブロックを何度も実行したいが、リストに対し繰り返し処理を行う必要がない場合は、代わりに [**range()**　](https://www.w3schools.com/python/ref_func_range.asp)を使うことができます。
# MAGIC
# MAGIC **`range()`**　は、開始値と停止値を受け取ります（停止値より小さい値が対象となり、停止値と同じ値は対象ではありません）。デフォルトでは、開始値から始まり停止値-1で終わるように1つずつ増加します。つまり **`range(0, 4)`** は順に右のような値となります：0, 1, 2, 3。
# MAGIC
# MAGIC 例えば、 **`"Hello!"`**　を10回出力してみましょう。

# COMMAND ----------

for element in range(0, 10):
    print("Hello!")

# COMMAND ----------

# MAGIC %md <i18n value="4e3f1154-8637-45de-a4ae-5b285bb87fdd"/>
# MAGIC
# MAGIC ここで **`element`**　は反復毎にその範囲内の各数値に一時的に割り当てられます。

# COMMAND ----------

for element in range(1, 11):
    print(element)

# COMMAND ----------

# MAGIC %md <i18n value="1ff92a97-049b-44a0-ab26-dac4a85ca615"/>
# MAGIC
# MAGIC 問題：0-9ではなく、1-10を表示したい場合、コードをどのように変更したらよいでしょうか？

# COMMAND ----------

# MAGIC %md <i18n value="edd56f68-c314-46f0-9d37-de1ef33a449e"/>
# MAGIC
# MAGIC ループを使って、リストを絞り込むことができます。例えば、4より大きい数字だけを残すように数字のリストを絞り込みたいとします。 
# MAGIC
# MAGIC このためには、空の新しいリストを作成し、数字のリストをループして、4より大きい場合は空のリストに数字を追加します。

# COMMAND ----------

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
final_list = []

for element in numbers_list:
    if element > 4:
        final_list.append(element)
    else:
        pass # do nothing
        
final_list

# COMMAND ----------

squqre_list = []
for i in range(10):
  squqre_list.append(i ** 2)
print(squqre_list)

# COMMAND ----------

squqre_list = [i ** 2 for i in range(10)]
print(squqre_list)

# COMMAND ----------

final_list = [element for element in numbers_list if element > 4]

# COMMAND ----------

# MAGIC %md <i18n value="cb72b94d-ff2f-43ba-8468-5666faa713f3"/>
# MAGIC
# MAGIC ループを使ってリストを絞り込み新しいリストを作成することは、よくある問題であるため、Pythonは非常に便利なショートカットを提供しています。 
# MAGIC
# MAGIC このショートカットは[リスト内包表記](https://www.w3schools.com/python/python_lists_comprehension.asp)と呼ばれており、右のようなものです： **`[var_name for var_name in list if (boolean condition)] `**
# MAGIC
# MAGIC このショートカットを使って、前のセルでやったのと全く同じことをやってみましょう。

# COMMAND ----------

final_list_shortcut = [element for element in numbers_list if element > 4]
final_list_shortcut

# COMMAND ----------

# MAGIC %md <i18n value="42f3bd09-15b7-4cb6-bf4d-61d867f57f8c"/>
# MAGIC
# MAGIC **`numbers_list`**　内の　**`element`**　について、4より大きい **`element`**　を最終的な　**`element`**　のリストに含めるというように、左から右に読んで解釈することになります。
# MAGIC
# MAGIC たとえば、　**`numbers`**　の中で4より大きい　**`element`**　を含めるのではなく、代わりに　**`numbers`**　の中で4より大きい全ての　**`element`** について　**`2 * element`**　を含めたいとします。以下のコードを見てみましょう。

# COMMAND ----------

doubled_list = [2 * element for element in numbers_list if element > 4]
doubled_list

# COMMAND ----------

# MAGIC %md <i18n value="9d0bf7b0-5558-47fe-9a02-342e7f644c66"/>
# MAGIC
# MAGIC 論理式は実際には任意です。リストの全要素を2倍にしてみましょう。

# COMMAND ----------

[2 * element for element in numbers_list]

# COMMAND ----------

# MAGIC %md <i18n value="07060457-fa2d-48b6-b140-c4dbc681af0d"/>
# MAGIC
# MAGIC ### `break`
# MAGIC
# MAGIC 一連のデータについてループの繰り返し処理が終了する前にループを早期に終了させたい場合、 **`break`**　を使うことができます。
# MAGIC
# MAGIC **`break`**　はループのコードブロックの中の独立した行に書かれ、Pythonがその行を実行すると、Pythonはループのコードブロックを終了し、リストに対する反復処理を終了します。 
# MAGIC
# MAGIC これを使い、数値の4まで到達したら **`numbers_list`**　に対する繰り返し処理を終了してみましょう。

# COMMAND ----------

for element in numbers_list:
    if element == 4:
        break
    print(element)

# COMMAND ----------

# MAGIC %md <i18n value="0abb7db5-41c8-4c67-ba08-664507255fa6"/>
# MAGIC
# MAGIC ### `continue`
# MAGIC
# MAGIC **`break`**　が実行されると、ループのコードブロックを終了し、リストに対する反復処理を終了します。もし、ループのコードブロックを早めに終了させたいが、それでも先に進み、ループを継続したい場合は **`continue`**　を使うことができます。 
# MAGIC
# MAGIC **`continue`**　もまた独立した行に書かれ、これが実行されると、Pythonはループコードブロックの実行を終了し、次の繰り返し処理を続行します。

# COMMAND ----------

for element in numbers_list:
    if element == 4:
        continue # 4 is not printed, but the numbers after are
    print(element)

# COMMAND ----------

# MAGIC %md <i18n value="65b05201-3344-43a1-aeee-33911d306bef"/>
# MAGIC
# MAGIC ### Whileループ (While-loops)
# MAGIC
# MAGIC ループには、forループの他にwhileループというものがあります。 
# MAGIC
# MAGIC [**whileループ**](https://www.w3schools.com/python/python_while_loops.asp)はこのように書きます：
# MAGIC
# MAGIC ```
# MAGIC while boolean expression:
# MAGIC     code_block
# MAGIC ```
# MAGIC
# MAGIC Pythonは論理式が　**`False`**　と評価されるまで、ループして、 **`code_block`**　のコードを繰り返し実行します。ループ毎に論理式を再評価し、 **`True`**　であれば再びコードを実行し、そうでなければ終了します。 
# MAGIC
# MAGIC **注意** ：ここで無限ループにならないように注意する必要があります。論理式が永久に **`False`** と評価されなければ、このコードは実行され続け、決して止まることはありません。

# COMMAND ----------

count = 10

while count > 0:
    print(count)
    count = count - 1

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
