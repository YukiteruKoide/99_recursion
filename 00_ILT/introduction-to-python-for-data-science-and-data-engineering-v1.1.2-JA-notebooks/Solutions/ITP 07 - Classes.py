# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="3fb78239-dd9c-4c5d-b4dc-6049604db4b2"/>
# MAGIC
# MAGIC # クラス（Classes）
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) このレッスンでは　<br>
# MAGIC - クラス(Class)と呼ばれる新しいデータを定義する方法
# MAGIC - インスタンス(Instance)属性を利用して、クラスのデータを定義
# MAGIC - メソッド(Method)を使用してクラスに機能を追加する

# COMMAND ----------

# MAGIC %md <i18n value="f8f3096e-b29e-4c8e-8874-96451f47002a"/>
# MAGIC
# MAGIC ## クラス（Classes）
# MAGIC
# MAGIC From [W3Schools](https://www.w3schools.com/python/python_classes.asp): 
# MAGIC ```
# MAGIC Pythonはオブジェクト指向のプログラミング言語です。Pythonではほとんどすべてのものがオブジェクトであり、そのプロパティやメソッドを持ちます。
# MAGIC
# MAGIC クラスはオブジェクトのコンストラクタのようなもので、オブジェクトを作成するための「設計図」です。
# MAGIC ```
# MAGIC
# MAGIC 関数（Functions）を使って作業するとき、異なるパラメータを一つの同じコードに適用することで、この関数を再利用できます。**クラスは、コードとデータの両方に再利用可能な青写真を提供するため、関数の一歩先と考えることができます**。
# MAGIC
# MAGIC ここまで、基本的な組み込み型と、より高度なコレクション型について見てきました。また、必要に応じて独自の[**classes**](https://www.w3schools.com/python/python_classes.asp)を定義することもできます。
# MAGIC
# MAGIC クラスを定義するには、次のように記述します。
# MAGIC
# MAGIC
# MAGIC ```
# MAGIC class ClassName():
# MAGIC     <code block>
# MAGIC ```
# MAGIC
# MAGIC これまで、私たちは通常 `snake_case` という規約を使用してきました。しかし、[Python style guides](https://peps.python.org/pep-0008/)では、クラスを定義する際には、すべての単語を大文字にし、スペースを入れずに、 `CapWords` を使用することを推奨しています。
# MAGIC
# MAGIC **注意**:　**`pass`** はPythonに何もしないように指示します。私たちは事実上、何もしないdogを定義していることになります。

# COMMAND ----------

# Create the blue print
class Dog():
    pass

# COMMAND ----------

# MAGIC %md <i18n value="b326ce06-9f66-46f3-a134-03579d30867a"/>
# MAGIC
# MAGIC これまで見てきた組み込み型では、クラスからオブジェクトを作成することは組み込まれていました。もし **`1`** や **`"hello"`** と書くと、Python はそれらがどのような型であるかを知っていて、 `int` や `str` オブジェクトを生成してくれます。
# MAGIC
# MAGIC しかし、自分で定義したクラスについては、以下のようにオブジェクトを作成する必要があります。
# MAGIC
# MAGIC
# MAGIC **`object_name = ClassName()`**
# MAGIC
# MAGIC 技術的には、これはオブジェクトの特定のバージョンを作成するため、クラスの「インスタンス化」と呼ばれます。これで **`Dog`** クラスができました。それでは、 **`Dog`** オブジェクトを作って、それを **`my_dog`** として呼んでみましょう。

# COMMAND ----------

# Instantiate the blueprint and save it to the variable
my_dog = Dog()

type(my_dog)

# COMMAND ----------

# MAGIC %md <i18n value="58c970b2-4bd1-4b0b-8533-b0794b07eed3"/>
# MAGIC
# MAGIC ##メソッドを用いたコードの再利用（Code Reuse with Methods）
# MAGIC
# MAGIC さて、何もしない **`Dog`** を作ることができたので、機能を追加してみましょう!
# MAGIC
# MAGIC クラスの機能は[**methods**](https://www.w3schools.com/python/gloss_python_object_methods.asp)によって定義されます。これは前回のレッスンで見たとおりです。
# MAGIC
# MAGIC 注意点として、　**method**は、オブジェクトに作用する特別な関数で、　**`object.method(arg)`**　のように呼び出します。
# MAGIC
# MAGIC メソッドの定義は、2つの違いを除けば、通常の関数の定義と同様です。
# MAGIC
# MAGIC 1.　クラスの定義の中にメソッドの定義をネストします。
# MAGIC 1. **`self`** という名前のパラメータを指定し、その後に追加のパラメータを指定しなければなりません。
# MAGIC
# MAGIC これは次のようになります。
# MAGIC
# MAGIC
# MAGIC ```
# MAGIC class ClassName():
# MAGIC
# MAGIC     def method_name(self, args):
# MAGIC         method code
# MAGIC ```
# MAGIC
# MAGIC 今のところ **`self`** パラメータは無視することにしますが、しばらくしたらまた戻ってきます。
# MAGIC 簡単な例を見てみましょう。名前を受け取ってそれを返すメソッドを書いてみます。

# COMMAND ----------

class UpdatedDog():
    
    def return_name(self, name):
        return f"name: {name}"

# COMMAND ----------

# MAGIC %md <i18n value="5de3ea33-9f20-4ca7-913c-f08dba3ba9ca"/>
# MAGIC
# MAGIC では、更新した **`Dog`** クラスのオブジェクトを作成して、メソッドを呼び出してみましょう。このようにメソッドを呼び出すことを忘れないでください。　**`object.method(args)`**
# MAGIC
# MAGIC 注意点として、特別なパラメーターである　**`self`**　を忘れないでください。

# COMMAND ----------

my_updated_dog = UpdatedDog()

my_updated_dog.return_name("Rex")

# COMMAND ----------

# MAGIC %md <i18n value="1dd48eff-d93e-4f8e-9373-ae10de48af4d"/>
# MAGIC
# MAGIC `self` についてはどでしょうか？
# MAGIC
# MAGIC メソッドは関数と違って、呼び出されたオブジェクトに作用することができます。メソッドは、呼び出したオブジェクトを参照できる必要があります。これが **`self`** が指すものです。
# MAGIC
# MAGIC **`object.method(self, args)`** を呼び出すと、Pythonによって自動的にオブジェクト自身が **`self`** パラメータに渡されます。

# COMMAND ----------

class DogWithSelf():
    
    def print_self(self):
        print(self)
        
dog_with_self = DogWithSelf()

print(dog_with_self)
dog_with_self.print_self() # prints the same object

# COMMAND ----------

# MAGIC %md <i18n value="56944397-f05e-4cdd-bced-940be45e1872"/>
# MAGIC
# MAGIC **`new_dog`** オブジェクトを表示した後、 **`new_dog`** の **`print_self()`** メソッドを呼び出すと、同じオブジェクトが表示されることに注意してください。
# MAGIC
# MAGIC これは、 **`new_dog`** が **`print_self()`** で **`self`** の引数として渡されたからです。

# COMMAND ----------

# MAGIC %md <i18n value="a3aea935-bc40-4fc2-aeb0-f3d5d7c45eb2"/>
# MAGIC
# MAGIC ##属性によるデータキャッシュ(Data Caching with Attributes)
# MAGIC
# MAGIC このクラスでは、データを保存するための何らかの方法が必要です。 **クラス内に変数が格納されている場合、それは属性と呼ばれます。** 属性とは、オブジェクトのインスタンスごとに定義される変数にすぎません。どのインスタンスも同じ名前の属性を持ちますが、通常は異なる値に設定されます。
# MAGIC
# MAGIC
# MAGIC ```
# MAGIC class ClassName():
# MAGIC
# MAGIC     def __init__(self, arg):
# MAGIC         self.arg = arg
# MAGIC ```
# MAGIC
# MAGIC Pythonには **`__init__(self)`** という特別なメソッドがあり、オブジェクトが初期化される際に自動的に呼び出されます。このメソッドはクラスの属性を構築するため、クラスの*コンストラクタメソッド*と呼ばれることがあります。
# MAGIC
# MAGIC 例えば、 **`Dog`** クラスで、すべての犬のオブジェクトに名前と色を付けたいとします。これを実現するために、クラスの属性として **`name`** と **`color`** を作成します。
# MAGIC
# MAGIC そして、すべての **`Dog`** オブジェクトは name と color 属性を持ちますが、これらはオブジェクトごとに異なる値を設定することができますので、それぞれのDogオブジェクトに独自の名前と色を持たせることができます。

# COMMAND ----------

class DogWithAttributes():

    def __init__(self, name, color):
        print("This ran automatically!")
        self.name = name
        self.color = color

dog_with_attributes = DogWithAttributes("Rex", "Orange")

# COMMAND ----------

# MAGIC %md <i18n value="a6ca39f1-ceb0-42ff-aa95-fac34ef7ba1b"/>
# MAGIC
# MAGIC `__init__()` メソッドが自動的に呼び出されると、これらの変数がオブジェクトのインスタンスである `self` に保存されます。メソッドにアクセスしたのと同じように、括弧()を使わずに属性にアクセスすることができます。

# COMMAND ----------

dog_with_attributes.name

# COMMAND ----------

# MAGIC %md <i18n value="3d8f5672-e9d4-4bd4-9c14-91756c1cbb4f"/>
# MAGIC
# MAGIC メソッド定義では、　**`self.attribute_name`** を使用して属性にアクセスできます。これは、　**`self`**　がメソッドを呼び出すオブジェクトを指すためで、インスタンス化の際にどんな名前を付けたかに関係ありません。

# COMMAND ----------

class DogWithAttributesAndMethod():
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def return_name(self):
        return self.name
        
my_dog = DogWithAttributesAndMethod("Rex", "Blue")
my_dog.return_name()

# COMMAND ----------

# MAGIC %md <i18n value="4ec0fb49-f058-4c68-be13-aac66e9e5fe3"/>
# MAGIC
# MAGIC これで、機能を追加するのに必要なツールはすべて揃いました! 例えば、Dogの名前を変更する機能を追加したいとしましょう。このように、　**`name`**　属性を更新するだけでよいのです

# COMMAND ----------

class DogWithAttributesAndMethods():
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def return_name(self):
        return self.name
        
    def update_name(self, new_name):
        self.name = new_name
        
my_dog = DogWithAttributesAndMethods("Rex", "Blue")
print(f"Here's my name now: {my_dog.return_name()}")

my_dog.update_name("Brady")
print(f"Here's my name after updating it: {my_dog.return_name()}")

# COMMAND ----------

# MAGIC %md <i18n value="f781f535-f48d-4fb6-a110-c52e5a6c4039"/>
# MAGIC
# MAGIC ## より高度なクラス(More Advanced Classes)
# MAGIC  
# MAGIC クラスは多くのメソッドと属性を持つことができます。また、他のクラスの属性にアクセスすることもできます。
# MAGIC
# MAGIC `return_both_names` メソッドを見て、クラスがどのように他のクラスの属性を使用できるかを見てみましょう。

# COMMAND ----------

class DogFinal():
    
    def __init__(self, name_str, color_str):
        self.name = name_str
        self.color = color_str
        
    def return_name(self):
        return self.name
        
    def update_name(self, new_name):
        self.name = new_name
        
    def return_both_names(self, other_dog_object):
        return self.name + " and " + other_dog_object.name
        
dog_1 = DogFinal("Rex", "Blue")
dog_2 = DogFinal("Brady", "Purple")

dog_1.return_both_names(dog_2)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
