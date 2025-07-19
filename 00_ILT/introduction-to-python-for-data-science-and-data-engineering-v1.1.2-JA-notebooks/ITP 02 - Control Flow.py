# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="5e2b0b7f-f62f-49f4-9178-aa14bf84b5b7"/>
# MAGIC
# MAGIC # 制御フロー （Control flow）
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは<br>
# MAGIC
# MAGIC  - Pythonプログラムの制御フローを変更します
# MAGIC  - 論理式と条件文を組み合わせます

# COMMAND ----------

# MAGIC %md <i18n value="adcf81b0-d6b9-4d96-8952-8535f6b05741"/>
# MAGIC
# MAGIC ## if文 (if-statement)
# MAGIC
# MAGIC Pythonはデフォルトで、コードのすべての行を上から下へ順番に実行します。しかし、どのコードを実行すべきかを制御する条件付きロジックを定義したい場合はどうすればよいでしょうか。 
# MAGIC
# MAGIC Pythonがコードを実行する順序を**制御フロー**と呼び、Pythonには制御フローを変更するための機能があります。 
# MAGIC
# MAGIC Pythonが提供する最初の機能は、**if文**です。 
# MAGIC
# MAGIC [**if文**](https://www.w3schools.com/python/gloss_python_if_statement.asp)は以下のように書きます。
# MAGIC
# MAGIC
# MAGIC     if bool:
# MAGIC         code_1
# MAGIC     else:
# MAGIC         code_2
# MAGIC       
# MAGIC ここでの`bool`は論理式で、評価されると **`True`** または **`False`** に解釈されます。
# MAGIC
# MAGIC これは分かれ道と考えてください。Pythonは先頭の真偽値を読み、もしそれが **`True`** であれば、 **`code_2`** ではなく **`code_1`** を実行します。 
# MAGIC
# MAGIC もし **`False`** である場合、 **`code_1`** をスキップし **`code_2`** を実行します。
# MAGIC
# MAGIC いくつかの例を見てみましょう。

# COMMAND ----------

if True:
    print("True")
else:
    print("False")

# COMMAND ----------

# MAGIC %md <i18n value="d521ae49-84e2-42e1-88e2-ec13549e726d"/>
# MAGIC
# MAGIC ### インデント (Indentation)
# MAGIC
# MAGIC **if文**の[インデント（字下げ)](https://www.w3schools.com/python/gloss_python_if_indentation.asp)に注目してください。これはコードの可読性を高めるという他に、**実はコードを実行するために必要なことなのです。**
# MAGIC
# MAGIC Pythonはインデントを把握し、**if** と**else**ブロックの中にどういうコードがあるのか理解します。 
# MAGIC
# MAGIC Pythonの標準では、インデントはスペース4つであるべきですが **`タブ`** キーはショートカットになります。

# COMMAND ----------

# MAGIC %md <i18n value="694f3cf9-552d-4daa-ab39-8f68e0d28514"/>
# MAGIC
# MAGIC ## 演算子 (Operators)
# MAGIC
# MAGIC さて、**if文**を使えるようになったところで、if文と一緒に使える論理式を見てみましょう。 
# MAGIC
# MAGIC **`and`** 、 **`or`** 、 **`not`** という論理演算子を思い出してください 
# MAGIC
# MAGIC Pythonは **if文** の真偽値を **`True`** または **`False`** と評価し、それに従って動作します。 
# MAGIC
# MAGIC ここまでは、1つのデータ型から構成され、同じ型にデータ評価される式だけを見てきました。
# MAGIC
# MAGIC 例えば、以下です：
# MAGIC
# MAGIC **`Ture or False -> True`**
# MAGIC
# MAGIC **`1 + 2 -> 3`**
# MAGIC
# MAGIC また、あるデータ型から構成され、異なるデータ型に評価される式も存在します。 
# MAGIC
# MAGIC **`<`** 、 **`>`** 、 **`<=`** 、 **`>=`** 、 **`==`** と **`!=`** 演算子は、複数のデータ型に対して定義されていますが、真偽値として評価されます。 
# MAGIC
# MAGIC | <    | > | <= | >= | == | != |
# MAGIC | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
# MAGIC | より小さい   | より大きい    | 〜以下     | 〜以上    | 等しい     | 等しくない      |
# MAGIC | **`a < b -> bool`**    | **`a > b -> bool`**        |**`a <= b -> bool`**   | **`a >= b -> bool`**       |**`a == b -> bool`**   | **`a != b -> bool`**      |
# MAGIC
# MAGIC **注意：** **`=`** は変数の代入に使用されます。 **`==`** は値が一致しているかの比較に使用されます

# COMMAND ----------

print(1 == 1)
print(1.5 != 2.5)
print("abc" == "xyz")
print(True == True)

# COMMAND ----------

# MAGIC %md <i18n value="12aa040d-a993-49d0-b3c8-a19fbc6b0a12"/>
# MAGIC
# MAGIC これらの演算子を使って、値段から昼食を買うべきかどうかを見てみましょう。昼食の予算は15ドルですが、本当においしい料理なら少しオーバーしてもいいかもしれませんね。

# COMMAND ----------

lunch_price = 20

if lunch_price <= 15:
    print("Buy it!")
else:
    print("Too expensive")

# COMMAND ----------

# MAGIC %md <i18n value="a634486b-b213-4e83-b920-288aa64c0dc8"/>
# MAGIC
# MAGIC **if**または**else**ブロックの中のコードは何でもよく、別の**if文**でも大丈夫です。

# COMMAND ----------

if lunch_price <= 15:
    print("Buy it!")
else:
    if lunch_price < 25:
        print("Is it really good?")
    else:
        print("This better be the best food of all time")

# COMMAND ----------

# MAGIC %md <i18n value="ae3c161b-53c5-4e87-99af-43ddf67ea92c"/>
# MAGIC
# MAGIC ## elif
# MAGIC
# MAGIC **elif文**を追加することで、複数の論理式を考慮したif文の拡張が可能です。
# MAGIC
# MAGIC 以下のように記述します：
# MAGIC
# MAGIC
# MAGIC     if bool:
# MAGIC         code_1
# MAGIC     elif bool:
# MAGIC         code_2
# MAGIC     elif bool:
# MAGIC         code_3
# MAGIC     .
# MAGIC     .
# MAGIC     .
# MAGIC     else:
# MAGIC         code_last
# MAGIC       
# MAGIC 複数の**elif文**を入れることができます。 
# MAGIC
# MAGIC Pythonは論理式を先頭から順に評価します。論理式が **`True`** と評価された場合、Pythonは次のコードブロックのコマンドを実行し、それ以降の **elif** 節と **else** 節をすべてスキップします。
# MAGIC
# MAGIC どの論理式も **`True`** に評価されない場合、Pythonは **else** コードブロックを実行します。

# COMMAND ----------

lunch_price = 15

if lunch_price == 10:
    print("10 dollars exactly! Buy it!")
elif lunch_price <= 15:
    print("Buy it!")
elif lunch_price < 25:
    print("Is it really good?")
else:
    print("This better be the best food of all time")

# COMMAND ----------

# MAGIC %md <i18n value="82b070bf-589d-4791-b85c-66f51b170b76"/>
# MAGIC
# MAGIC ## 犬種のおすすめ (Dog Breed Recommendations)
# MAGIC
# MAGIC ユーザーが以下のような情報を提供して、彼らが犬種を選択するのをお手伝いしましょう。
# MAGIC
# MAGIC * **`dog_person`**:犬派かどうかを表す真偽値
# MAGIC * **`cat_person`**:猫派かどうかを表す真偽値
# MAGIC * **`age`**:ユーザーの年齢
# MAGIC
# MAGIC これらの質問に対するユーザーの入力をもとに、おすすめを出力します。 
# MAGIC
# MAGIC アプリケーション側はこのように動作します。
# MAGIC
# MAGIC * ユーザーが成人（18歳未満）でない場合は、保護者に許可を得るよう伝えます。 
# MAGIC
# MAGIC * これ以外の場合、 
# MAGIC
# MAGIC   * 犬派で、かつ猫派の場合、猫との相性が良いゴールデンレトリバー(Golden Retriever)をおすすめします。
# MAGIC   * 犬派であり、猫派でないなら、猫を追いかけることで知られるスコティッシュ・ディアハウンド(Scottish Deerhound)をおすすめします。
# MAGIC   * 猫派であり、犬派でないなら、「見当違いのことをしようとしています」と教えます。
# MAGIC   * 最後に、犬派でも猫派でもない場合、本当にペットが欲しいのかを考えてもらいます。

# COMMAND ----------

dog_person = True
cat_person = True
age = 30

if age < 18:
    print("Ask your parents for permission!")
else:
    if dog_person and cat_person: # implicitly evaluates dog_person == True and cat_person == True, so can omit the == True
        print("Golden Retriever")
    elif dog_person and not cat_person:
        print("Scottish Deerhound")
    elif cat_person and not dog_person:
        print("You're barking up the wrong tree!")
    else:
        print("Are you sure a pet is right for you?")

# COMMAND ----------

# MAGIC %md <i18n value="5ba1204e-82df-4060-8c87-a981b3843075"/>
# MAGIC
# MAGIC また、論理式の順番を意識して、以下のように書くこともできます。最初の　**`True`**　でPythonは止まることを思い出しましょう。

# COMMAND ----------

dog_person = True
cat_person = True
age = 30

if age < 18:
    print("Ask your parents for permission!")
elif dog_person and cat_person:
    print("Golden Retriever")
elif dog_person and not cat_person:
    print("Scottish Deerhound")
elif cat_person and not dog_person:
    print("You're barking up the wrong tree!")
else:
    print("Are you sure a pet is right for you?")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
