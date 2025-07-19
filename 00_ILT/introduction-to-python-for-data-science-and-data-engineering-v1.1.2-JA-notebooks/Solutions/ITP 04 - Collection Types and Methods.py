# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="d845488d-8461-4ee9-8b24-9bdff213d1fb"/>
# MAGIC
# MAGIC # コレクション型とメソッド (Collection Types and Methods)
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは<br>
# MAGIC
# MAGIC - オブジェクトとメソッドを導入します
# MAGIC - リストを作成します
# MAGIC - 新しいコレクションデータ型のメソッドを使用します

# COMMAND ----------

# MAGIC %md <i18n value="2d0178c2-f2b4-4746-82eb-5b81eec6be0e"/>
# MAGIC
# MAGIC ## オブジェクト (Objects)
# MAGIC
# MAGIC このレッスンでは、まずデータ型が提供する新しい機能をいくつか見ていき、次にいくつかの新しいデータ型に対してそれをどのように使用するかを見てみます。しかし、その前に、いくつかの用語について見ておく必要があります。
# MAGIC
# MAGIC [**オブジェクト**](https://www.w3schools.com/python/python_classes.asp)は、特定のデータ型のインスタンスです。 
# MAGIC
# MAGIC 例えば **`1`** は整数型なので、整数型オブジェクトと呼ぶことにします。 **`"Hello"`** は文字列型なので、文字列型オブジェクトと呼ぶことにします。

# COMMAND ----------

# MAGIC %md <i18n value="753edb8e-797e-4bf2-b6f4-4d4c952512a1"/>
# MAGIC
# MAGIC ## メソッド：より多くの機能 (Methods: More Functionality)
# MAGIC
# MAGIC 復習ですが、データ型は、ある種の**データ**と、データに対して行える**操作**を提供するものです。ここまでは、実は各データ型が提供する操作のごく一部しか見ていないのです。 
# MAGIC
# MAGIC データ型は[**メソッド**](https://www.w3schools.com/python/gloss_python_object_methods.asp)と呼ばれる特別な関数を持ち、より多くの機能を提供します。メソッドは、オブジェクトに対して呼び出すことと、呼び出されたオブジェクトを編集できることを除けば、通常の関数と全く同じです。メソッドは以下のように呼び出します：
# MAGIC
# MAGIC **`object.method_name(arguments)`**
# MAGIC
# MAGIC これは少し難しいので、今回のレッスン全体で取り上げる予定ですが、今知っておくべきことは以下の通りです。
# MAGIC
# MAGIC **メソッドとは、あるデータ型が提供する関数で、そのデータ型のオブジェクトに対して呼び出すことができるものです。これらのメソッドは、呼び出したオブジェクトに対して作用し、そのデータ型が提供する機能をより多く利用できるようにします。**

# COMMAND ----------

# MAGIC %md <i18n value="2ca5b59c-4cb8-4e87-b648-166eee0aedad"/>
# MAGIC
# MAGIC ### 文字列のメソッド (String Methods)
# MAGIC
# MAGIC すでによく知っているデータ型に対するメソッドの例を見てみましょう：文字列。文字列には[**upper()**](https://www.w3schools.com/python/ref_string_upper.asp)というメソッドがあり、文字列を大文字にします。

# COMMAND ----------

greeting = "hello"
print(greeting.upper())
print(greeting)

# COMMAND ----------

# MAGIC %md <i18n value="b83c4e97-70e0-4104-90f1-12ede96a8515"/>
# MAGIC
# MAGIC ### インプレースメソッド (In-place methods)
# MAGIC
# MAGIC メソッドはオブジェクトに作用する関数であり、インプレース（呼び出されたオブジェクト自体を変更する）な操作か、新しいオブジェクトを返すかのどちらかを実行します。
# MAGIC
# MAGIC **`upper()`** メソッドはステートフルなインプレースメソッドではなく、 新しい文字列を返して **`greeting`** 変数を変更しなかったことに注目してください。<a href="https://www.w3schools.com/python/python_ref_string.asp" target="_blank">W3Schools</a>には、Pythonの他の文字列メソッドに関する情報が掲載されています。

# COMMAND ----------

# MAGIC %md <i18n value="bc7aa58a-5ea7-4387-96b7-189b364d56c3"/>
# MAGIC
# MAGIC ### タブ補完 (Tab Completion)
# MAGIC
# MAGIC あるオブジェクトに適用できるメソッドのリストを表示させたい場合は、オブジェクトの後に **`.`** と入力し、タブキーを押すと、そのオブジェクトで利用可能なメソッドのドロップダウンメニューが表示されます。
# MAGIC
# MAGIC 以下、試しに **`greeting`** 文字列オブジェクトで試してみましょう。 **`greeting.`** と入力し、タブキーを押してください。

# COMMAND ----------

# Type . and hit Tab
greeting

# COMMAND ----------

# MAGIC %md <i18n value="5b3151ca-f1d4-430f-8129-3cb28816c364"/>
# MAGIC
# MAGIC ### `help()`
# MAGIC
# MAGIC タブ補完は非常に便利ですが、あるオブジェクトに対して可能な限りすべてのメソッドに目を通そうとすると、それらのメソッドがどのように動作するのか、まだよく分からない場合があります。
# MAGIC
# MAGIC そのドキュメントを調べることもできますし、前回のレッスンで見た [**help()**](https://www.geeksforgeeks.org/help-function-in-python/)関数を使うこともできます。
# MAGIC
# MAGIC 復習になりますが、この **`help()`** 関数は、渡された項目のドキュメントをいくつか表示します。
# MAGIC
# MAGIC 例えば、上記のタブ補完を使用する場合、[**capitalize()**](https://www.w3schools.com/python/ref_string_capitalize.asp)文字列メソッドが表示されますが、それがどのように動作するかはわかりません。

# COMMAND ----------

help(greeting.capitalize)

# COMMAND ----------

greeting.capitalize()

# COMMAND ----------

# MAGIC %md <i18n value="238070d2-fa76-43ef-a14b-2d67ef88af08"/>
# MAGIC
# MAGIC ## コレクションデータ型のメソッド (Methods with Collection Types)
# MAGIC
# MAGIC メソッドについて簡単に理解したところで、より高度なデータ型とそれらが提供するメソッドについて見てみましょう。
# MAGIC
# MAGIC 次に **コレクションデータ型** について見ていきます。名前が示すように、これらのデータ型のデータは、他のデータ型の集合体です。

# COMMAND ----------

# MAGIC %md <i18n value="d028dd16-da40-4c7d-b62e-650e154d1710"/>
# MAGIC
# MAGIC ### コレクションデータ型その 1:リスト (Collection Type 1: Lists)
# MAGIC
# MAGIC リストとは、単に項目を順序に並べたものです。 
# MAGIC
# MAGIC このように角括弧の中にカンマで区切られ並べられた項目の列として定義されます： **`[項目1、項目2、項目3...]。`**
# MAGIC
# MAGIC 項目はどのようなデータ型でも構いませんが、実際には、すべての値が同じデータ型のリストを作成するのが普通です。
# MAGIC
# MAGIC 今朝、みんなが食べた朝食を<a href="https://www.w3schools.com/python/python_lists.asp" target="_blank">リスト</a>にしてみましょう。
# MAGIC
# MAGIC <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Scrambed_eggs.jpg/1280px-Scrambed_eggs.jpg" width="20%" height="10%">

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]
breakfast_list

# COMMAND ----------

# Python can tell us breakfast_list's type
type(breakfast_list)

# COMMAND ----------

# MAGIC %md <i18n value="5ed35859-d9a4-44e0-a152-befc8855bab0"/>
# MAGIC
# MAGIC ここでは **`breakfast_list`** を実行例として使いますが、リスト内の値は以下のようにどのような型でもよいことに注意してください。

# COMMAND ----------

# any type works
["hello", True, 1, 1.5]

# COMMAND ----------

# MAGIC %md <i18n value="5bd3521a-76df-46d3-b5ec-07d22a896321"/>
# MAGIC
# MAGIC #### リストのメソッド (List Methods)
# MAGIC
# MAGIC リストデータ型が提供する **データ** を理解したところで、その **機能** のいくつかを見てみましょう。
# MAGIC
# MAGIC 既存のリストに新しい項目を追加することは、頻繁に行いたいと思うでしょう。 
# MAGIC
# MAGIC リストはそれを行うためだけの[**append()**](https://www.w3schools.com/python/ref_list_append.asp)というメソッドを提供しています。 
# MAGIC
# MAGIC **`append()`** は任意の型の引数を取り、呼び出されたリストを編集して、引数をリストの末尾に貼り付けます。 
# MAGIC
# MAGIC パンケーキ、卵、ワッフルを食べた後に、ヨーグルトも食べたとしましょう。
# MAGIC
# MAGIC ここで **`append()`** を使用して **`breakfast_list`** にヨーグルトを追加します。

# COMMAND ----------

breakfast_list.append("yogurt")
breakfast_list

# COMMAND ----------

# MAGIC %md <i18n value="668b2cdd-8135-439b-bf95-2880346ce49c"/>
# MAGIC
# MAGIC **注意：****`append()`** はインプレースメソッドであることに注意してください。このメソッドは新しいリストを返すのではなく、元の **`breakfast_list`** オブジェクトを編集します。 
# MAGIC
# MAGIC **`+`** も、以下のようにリストに対する結合として定義されています。

# COMMAND ----------

["pancakes", "eggs"] + ["waffles", "yogurt"]

# COMMAND ----------

# MAGIC %md <i18n value="6237eb3c-7a8b-428b-9418-4b397c163484"/>
# MAGIC
# MAGIC **`append()`** を使うのが一般的ですが、 **`+`** を使ってリストに要素を追加することもできます。

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]
breakfast_list = breakfast_list + ["yogurt"]
breakfast_list

# COMMAND ----------

# MAGIC %md <i18n value="a4bcc594-73a3-454d-ab4d-83db2844db10"/>
# MAGIC
# MAGIC これに対する便利なショートカットの操作に **`+=`** があります。
# MAGIC
# MAGIC **`breakfast_list`**`+=`**`["yogurt"］`** は、 **`breakfast_list`**`=`**`breakfast_list`**`+` **`["yogurt"］`** と同じことです。
# MAGIC
# MAGIC **`+=`** 演算子は他のデータ型に対しても有効で、それぞれのデータ型の **`+`** 演算子を利用します。

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]
breakfast_list += ["yogurt"]
breakfast_list

# COMMAND ----------

# MAGIC %md <i18n value="31cf815e-ec37-4313-b36c-84023b9a6f8c"/>
# MAGIC
# MAGIC #### リスト要素のインデックスによるアクセス (List indexing)
# MAGIC
# MAGIC リスト内の特定の１つまたは複数の項目を参照したい場合がよくあります。これを[リスト要素のインデックスによるアクセス](https://www.w3schools.com/python/python_lists_access.asp)といいます。
# MAGIC
# MAGIC リストには、このようにリスト内のあるインデックスにある項目を取得する操作が用意されています。
# MAGIC
# MAGIC       list_name[index]
# MAGIC
# MAGIC Pythonのインデックスは0から始まるので、リストの最初の要素は0、2番目は1、となります。

# COMMAND ----------

breakfast_list[0]

# COMMAND ----------

# MAGIC %md <i18n value="b86f1c49-9cc7-4699-a329-2e60bc68a774"/>
# MAGIC
# MAGIC また、右から左へ-1からカウントして要素を指定するネガティブインデックスも使用できます。 
# MAGIC
# MAGIC したがって、リストの最後の要素は-1、最後から2番目は-2、といった具合になります。

# COMMAND ----------

breakfast_list[-1]

# COMMAND ----------

# MAGIC %md <i18n value="7cefd54e-7d6b-449e-99c0-48809deafc78"/>
# MAGIC
# MAGIC また、以下のようにアクセスしたいインデックスの範囲を指定することも可能です。
# MAGIC
# MAGIC **`list_name[start:stop]`**
# MAGIC
# MAGIC これは、 **`start`** の位置から始まり **`stop`** の手前の位置までの値のリストを返します。

# COMMAND ----------

# Note the stop index is exclusive
breakfast_list[0:2]

# COMMAND ----------

# MAGIC %md <i18n value="bd802cdb-aece-435f-8056-151ab60ce5a7"/>
# MAGIC
# MAGIC startインデックスを指定しない場合、Pythonは先頭から始まるものと見なします。
# MAGIC
# MAGIC stopインデックスを指定しない場合、Pythonは最後の要素が最後であると見なします。

# COMMAND ----------

print(breakfast_list[:2])
print(breakfast_list[1:])

# COMMAND ----------

# MAGIC %md <i18n value="c1232cd7-3bd1-4dad-bc96-97ed5d36c5b1"/>
# MAGIC
# MAGIC また、リスト内のインデックスの値を次のように新しいものに変更することもできます。

# COMMAND ----------

print(breakfast_list)
breakfast_list[0] = "sausage"

print(breakfast_list)

# COMMAND ----------

# MAGIC %md <i18n value="b26f49c7-544d-4cd7-811b-5439f136cdbe"/>
# MAGIC
# MAGIC **`in`** を使って、ある要素が与えられたリストに含まれているかどうかを調べることもできます。これは論理演算子です。

# COMMAND ----------

"waffles" in breakfast_list

# COMMAND ----------

# MAGIC %md <i18n value="589d7a85-089c-4870-abe7-7ad2fd293698"/>
# MAGIC
# MAGIC ### コレクションデータ型その２：辞書 (Collection Type 2: Dictionaries)
# MAGIC
# MAGIC [辞書](https://www.w3schools.com/python/python_dictionaries.asp)は、キーと値のペアの集合体です。辞書を以下のように定義します：
# MAGIC
# MAGIC `{key_1: value_1, key_2: value_2, ...}`
# MAGIC
# MAGIC キーと値はすべて任意の型にすることができます。しかし、それぞれのキーは値に対応するため、*すべてのキーがユニーク*であることが重要です。
# MAGIC
# MAGIC キーが食べ物の種類で、値が朝食に食べたその食べ物の個数である朝食の辞書を作ってみましょう。

# COMMAND ----------

breakfast_dict = {"pancakes": 1, "eggs": 2, "waffles": 3}
breakfast_dict

# COMMAND ----------

# MAGIC %md <i18n value="14aa0189-5d2a-49f5-a497-b1a29839d03c"/>
# MAGIC
# MAGIC #### 辞書のメソッド (Dictionary Methods)
# MAGIC
# MAGIC 辞書には、与えられた引数に対して辞書内の値を取得するためのメソッド [**dict\_object.get()**](https://www.w3schools.com/python/ref_dictionary_get.asp)を提供します。 
# MAGIC
# MAGIC ワッフルを何個食べたか見てみましょう。

# COMMAND ----------

breakfast_dict.get("waffles")

# COMMAND ----------

# MAGIC %md <i18n value="c8653cbc-95a1-474e-8675-bbef76473da7"/>
# MAGIC
# MAGIC あるいは、 **`dict_object[key]`** のような構文も使えます。

# COMMAND ----------

breakfast_dict["waffles"]

# COMMAND ----------

# MAGIC %md <i18n value="de5edaf0-5374-4f84-888d-3a2793cd30fe"/>
# MAGIC
# MAGIC **`breakfast_dict[key]`** に何かを代入することで、リストと同様に辞書を更新することができます。 
# MAGIC
# MAGIC キーが存在する場合、現在の値を上書きします。そうでない場合は、新しいキーと値をペアを作成します。 
# MAGIC
# MAGIC 例えば、ワッフルをもう1個食べて合計4個になったところで、ヨーグルトを食べたとします。

# COMMAND ----------

print(breakfast_dict)
breakfast_dict["waffles"] += 1
breakfast_dict["yogurt"] = 1
print(breakfast_dict)

# COMMAND ----------

# MAGIC %md <i18n value="9492938e-d135-47f8-8256-804d70cc4ff8"/>
# MAGIC
# MAGIC **`+=`** を使ってワッフルの数を増やしていることに注目してください。
# MAGIC
# MAGIC **問題** ： **`+=`** を使ってヨーグルトの数を増やさなかったのはなぜでしょう？

# COMMAND ----------

# MAGIC %md <i18n value="8092da28-ccad-4265-a97e-fb30c6da249d"/>
# MAGIC
# MAGIC あるキーが辞書にあるかどうかを判断するために、[**dict\_name.keys()**](https://www.w3schools.com/python/ref_dictionary_keys.asp)メソッドを使うことができます。これは、辞書にあるキーのリストを返します。 
# MAGIC
# MAGIC リストと同様、キーが辞書にあるかどうかを調べるには **`in`** を使って、キーが辞書にあるかどうかを確認することができます。朝食にベーコンを食べたかどうか、見てみましょう。

# COMMAND ----------

print(breakfast_dict.keys())
print("bacon" in breakfast_dict.keys())

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
