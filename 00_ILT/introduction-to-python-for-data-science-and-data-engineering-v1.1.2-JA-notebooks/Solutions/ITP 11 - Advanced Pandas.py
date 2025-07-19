# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="84a7d8c4-2962-4cfa-b71a-1eb0e9d6a637"/>
# MAGIC
# MAGIC # Pandas上級編 (Advanced Pandas)
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは
# MAGIC * pandasが提供する、より高度な以下の機能を紹介します。
# MAGIC   - 列名を変更する
# MAGIC   - DataFrameにフィルタをかける
# MAGIC   - グループ化・集計関数
# MAGIC   - ソート
# MAGIC   - 列の補完機能

# COMMAND ----------

# MAGIC %md <i18n value="4b32f906-0ced-49ca-aef9-d0ed007c298a"/>
# MAGIC
# MAGIC このレッスンでは、データセットを扱います。以下のセルを実行すると、Databricksのファイルシステム内のデータセットへのパスを定義する変数にアクセスできるようになります。

# COMMAND ----------

# MAGIC %run "./Includes/Classroom-Setup"

# COMMAND ----------

# MAGIC %md <i18n value="5bbc9d31-e52b-4cbd-9e16-6f48fb1c051f"/>
# MAGIC
# MAGIC **`pandas`**　にアクセスすることを忘れないようにしましょう。まず ライブラリを　**`import`**　することが必要です。　**`pip install pandas`**　は必要ありません。なぜなら、すでにインストールされているからです。

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md <i18n value="a6a56c30-96e2-40dd-a36b-57969142819e"/>
# MAGIC
# MAGIC ## データの読み込み (Reading Data)
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/301/sf.jpg" style="height: 200px; margin: 10px; border: 1px solid #ddd; padding: 10px"/>
# MAGIC
# MAGIC これまで、手動で行と列を指定してDataFrameを作成してきました。データセットがCSV（カンマ区切りの形式）ファイルとして保存されていることがよくあります。 
# MAGIC
# MAGIC **`pandas`**　には[**read\_csv(path)**](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)という関数が用意されています。 CSVファイルが保存されているファイルパスを指定すると、そのファイルパスにあるファイルを内容とするDataFrameが返されます。
# MAGIC
# MAGIC <a href="http://insideairbnb.com/get-the-data.html" target="_blank">Inside Airbnb</a>のデータを分析し、サンフランシスコの賃貸市場について理解を深めていきます。データセットを読み込んでみましょう。

# COMMAND ----------

file_path = f"{DA.paths.datasets}/sf-airbnb/sf-airbnb.csv".replace("dbfs:", "/dbfs")
df = pd.read_csv(file_path)

# COMMAND ----------

# MAGIC %md <i18n value="005adbc3-7ac2-4097-b131-e13953b0f178"/>
# MAGIC
# MAGIC データセットの最初の数レコードを見るには、このように呼び出します [**head()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)。行数を指定しない場合は、デフォルトで5行になります。

# COMMAND ----------

df.head(3)

# COMMAND ----------

# MAGIC %md <i18n value="03959db2-4350-4824-8617-ac7a3cd8be51"/>
# MAGIC
# MAGIC 逆に、 [**tail()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html)を呼び出して、最後の数レコードを見ることができます。

# COMMAND ----------

df.tail(3)

# COMMAND ----------

# MAGIC %md <i18n value="f67fb620-5e6a-4576-808a-9f2e5c4a7ba3"/>
# MAGIC
# MAGIC ## 列名の変更 (Renaming Columns)
# MAGIC
# MAGIC [**rename()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)を使って、DataFrame の列の名前を変更することができます。 **`columns`**　パラメータに、古い列名から新しい列名へのマッピングを含む辞書を渡します。
# MAGIC
# MAGIC 上の　**`neighbourhood`**　列を **`neighborhood`**　へと変更しましょう。

# COMMAND ----------

df = df.rename(columns={"neighbourhood": "neighborhood"})
df[["id", "neighborhood"]].head(10)

# COMMAND ----------

# MAGIC %md <i18n value="ac2317e2-da36-4d53-9af2-e0a3a77e86d6"/>
# MAGIC
# MAGIC ## フィルタリング (Filtering)
# MAGIC
# MAGIC ある条件を満たす行の部分集合を選択したい場合がよくありますが、　**`df[bool_array]`**　を指定することで実現できます。 **`bool_array`**　は それぞれの行に対する　**`True`**　と **`False`**　の値からなる　**`Series`**　です。 
# MAGIC
# MAGIC **`True`**　と評価された行は保持され、一方 **`False`**　と評価された行は保持されません。 
# MAGIC
# MAGIC **`host_is_superhost`**　が **`"t"`**　であるすべての行をフィルタリングしてみましょう。これは、airbnbのオーナーがsuperhost(模範的なホスト)であることを意味します。

# COMMAND ----------

filtered_df = df[df["host_is_superhost"] == "t"]
filtered_df[["id", "host_is_superhost"]].head(10)

# COMMAND ----------

# MAGIC %md <i18n value="2fc07a19-40ee-4c02-aef8-47f8d4d5320d"/>
# MAGIC
# MAGIC ここで **`df["host_is_superhost"] == "t"] `**　は真偽値の配列です。それでは、対応する　**True/False**　の行インデックスを見てみましょう。

# COMMAND ----------

df["host_is_superhost"] == "t"

# COMMAND ----------

# MAGIC %md <i18n value="5060945e-605f-4103-b37f-bcce30875d2e"/>
# MAGIC
# MAGIC **`host_is_superhost`**　が "t" でないレコードを検索することもできます。

# COMMAND ----------

df["host_is_superhost"] != "t"

# COMMAND ----------

# MAGIC %md <i18n value="4491d033-fe78-482a-9f84-e64ee89914b4"/>
# MAGIC
# MAGIC ## pandasの論理演算子 (Pandas Boolean Operators)
# MAGIC
# MAGIC 多くの場合、レコードをフィルタリングするために、複数の条件を評価する必要があります。例えば、ホストがスーパーホストで、airbnbのレビューが150件以上あるレコードを全て選択してみましょう。
# MAGIC
# MAGIC これまで見てきた通常の論理演算子の代わりに、[ビット単位の論理演算子](https://www.w3schools.com/python/gloss_python_bitwise_operators.asp)があります。: 
# MAGIC * **`and`** -> **`&`** 
# MAGIC * **`or`** -> **`|`** 
# MAGIC * **`not`** -> **`~`**

# COMMAND ----------

filtered_df = df[(df["host_is_superhost"] == "t") & (df["number_of_reviews"] >= 150)]
filtered_df[["id", "host_is_superhost", "number_of_reviews"]].head(10)

# COMMAND ----------

# MAGIC %md <i18n value="ab96aa56-71eb-41f6-86f5-9cb8694eb956"/>
# MAGIC
# MAGIC ## 集計関数 (Aggregate Functions)
# MAGIC
# MAGIC 集計関数は、Seriesを入力として取り込み、単一の出力を返す関数です。 
# MAGIC
# MAGIC pandasで最もよく使われるのは、数値の　**`Series`**　を受け取り、平均値などの目的の統計量を返すものです。 
# MAGIC
# MAGIC **`number_of_review`**　の平均値、最小値、最大値を見てみましょう：

# COMMAND ----------

print(df["number_of_reviews"].mean())
print(df["number_of_reviews"].min())
print(df["number_of_reviews"].max())

# COMMAND ----------

# MAGIC %md <i18n value="80541416-8c3c-4ed2-9c8c-d3345995c67d"/>
# MAGIC
# MAGIC もうひとつの有用なメソッドは [**describe()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)で、これは与えられた数値の　**`Series`**　の要約統計のレポートを提供します :

# COMMAND ----------

df["number_of_reviews"].describe()

# COMMAND ----------

# MAGIC %md <i18n value="6479f736-b87d-412d-a422-6079e807f12a"/>
# MAGIC
# MAGIC また、このメソッドをDataFrameに使用すると、すべての数値の列に適用されます。

# COMMAND ----------

df[["number_of_reviews", "host_listings_count", "bedrooms"]].describe()

# COMMAND ----------

# MAGIC %md <i18n value="b74fc8a9-76d5-446c-aec9-0a4cbb247bef"/>
# MAGIC
# MAGIC 多くの場合、小数点以下6桁目の値は気にするでしょう。[**round()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html?highlight=round#pandas.DataFrame.round)を呼び出して、結果を四捨五入してみましょう。

# COMMAND ----------

df[["number_of_reviews", "host_listings_count", "bedrooms"]].describe().round(2)

# COMMAND ----------

# MAGIC %md <i18n value="9d6e0cc1-b817-42b0-b18e-02810cdb8711"/>
# MAGIC
# MAGIC ## Group By
# MAGIC
# MAGIC 数値以外の列であるカテゴリーごとに、集計関数の結果を見たいこともあります。 
# MAGIC
# MAGIC 例えば、地域ごとの平均寝室数を確認したいとします。
# MAGIC
# MAGIC これを行うには、まず [**groupby([columns])**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)メソッドを使用して、グループ化したいカテゴリを指定します。今回、　**`neighborhood`**　でグループ化しましょう。

# COMMAND ----------

df.groupby(["neighborhood"])

# COMMAND ----------

# MAGIC %md <i18n value="236d5b5d-cffb-468d-b63d-87920463e92a"/>
# MAGIC
# MAGIC そして、関心のある集計関数を適用します。今回は、関心のある **`bedrooms`**　に　**`mean()`**　を適用しましょう。
# MAGIC
# MAGIC **注意**　ここでは **`[["bedrooms"]]`**　を使って寝室を選択しています。寝室以外にも列を追加することができるからです。

# COMMAND ----------

grouped_df = df.groupby(["neighborhood"])[["bedrooms"]].mean().head(10)
grouped_df

# COMMAND ----------

# MAGIC %md <i18n value="1bf79474-0ec0-4e8b-9c6a-5d9e4fa965f4"/>
# MAGIC
# MAGIC # インデックスのリセット (Reset Index)
# MAGIC 一般に、行インデックスは数字ですが、名前を付けることもできます。上の例では **`neighborhood`**　は列ではなく、行のインデックスになりました。 
# MAGIC
# MAGIC 列を出力すればわかることです。

# COMMAND ----------

grouped_df.columns

# COMMAND ----------

# MAGIC %md <i18n value="775492c1-0ecb-45ea-a22d-c26f21e72dcb"/>
# MAGIC
# MAGIC インデックスを数字にリセットし、現在のインデックスを列に移動させるために [**reset\_index()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html)を使います。

# COMMAND ----------

reset_df = grouped_df.reset_index()
reset_df

# COMMAND ----------

# MAGIC %md <i18n value="c66e2c3c-b5b4-4414-acb8-6da1066bafc9"/>
# MAGIC
# MAGIC ## ソート (Sorting)
# MAGIC
# MAGIC pandasは **`DataFrame`**　や **`Series`**　の行をソートするための[**sort\_values()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)メソッドを提供しています。 
# MAGIC
# MAGIC **`DataFrame`**　に対して使う場合は、どの列でソートするかを　**`df.sort_values([col])`**　のように指定する必要があります。

# COMMAND ----------

sorted_df = df.sort_values(["bedrooms"])
sorted_df[["id","bedrooms"]].head(10)

# COMMAND ----------

# MAGIC %md <i18n value="629120a5-e21a-4fc1-bbc6-26db481023cb"/>
# MAGIC
# MAGIC **`Series`**　に対して使う場合、列は1つしかないので、指定する必要はありません。

# COMMAND ----------

df["bedrooms"].sort_values()

# COMMAND ----------

# MAGIC %md <i18n value="609293f8-6e06-4a1a-9e8b-1c9b8bff472b"/>
# MAGIC
# MAGIC デフォルトでは **`sort_values()`**　は昇順でソートします。　**`ascending=False`**　パラメータを指定すると、降順に変更されます。

# COMMAND ----------

df["bedrooms"].sort_values(ascending=False)

# COMMAND ----------

# MAGIC %md <i18n value="fffcfb0b-b658-4c92-8acf-c2bbb05aa519"/>
# MAGIC
# MAGIC # NaN 
# MAGIC
# MAGIC お気づきかもしれませんが、この　**`DataFrame`**　はNaNを含んでいます。これらは欠損値を示します。 
# MAGIC
# MAGIC 欠損値を処理する方法はいくつかあります。このような値が存在すると、計算処理に支障をきたすことが多いです。
# MAGIC
# MAGIC まず、[**isnull()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html#pandas.DataFrame.isnull)のエイリアスである[**isna()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna)メソッドでチェックすることができるので、 **`sum()`**　メソッドを使用して、存在する NaN の数を数えます。

# COMMAND ----------

nan_df = df[["security_deposit", "notes"]] # subset of columns with NaNs
nan_df

# COMMAND ----------

nan_df.isna().sum()

# COMMAND ----------

# MAGIC %md <i18n value="dfc8960b-9408-4e30-892e-4e60cea3814a"/>
# MAGIC
# MAGIC ## NaNを削除する (Dropping NaN)
# MAGIC
# MAGIC NaNを処理する一つの方法として、NaNを持つ行をすべて削除する方法があります。このために、 [**dropna()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)メソッドを使うことができます。

# COMMAND ----------

nan_df.dropna()

# COMMAND ----------

# MAGIC %md <i18n value="1582be7b-f6e5-4e24-8898-9dca7a1bcd2f"/>
# MAGIC
# MAGIC ### 列の代入 (Impute Columns)
# MAGIC
# MAGIC しかし、レコードを削除すると、多くの情報を捨てることになります。上の例では、3000行以上を削除しています。
# MAGIC
# MAGIC 欠損値のある行を削除する代わりに、 [**fillna()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)を使用し、欠損値を補完し、使用するデフォルト値を指定することができます。

# COMMAND ----------

nan_df.fillna("Missing")

# COMMAND ----------

# MAGIC %md <i18n value="d21dcf8e-0db0-4477-a80f-a96558f1a6f1"/>
# MAGIC
# MAGIC しばしば、異なる列には異なる値を補完したいことがあります。例えば、`数値`の場合、平均値/中央値/その他で補完を行うことができます。`カテゴリ`特徴量の場合、最頻値や特別なカテゴリを用いた補完が一般的です。
# MAGIC
# MAGIC 代わりに　**`security_deposit`**　が欠損していた場合は`$0.00`と指定しましょう。 **`fillna()`**　には、キーとして列名、値として、列に補完するための値を持つ辞書を渡すことができます。 
# MAGIC
# MAGIC 元のDataFrameを更新したい場合は、　**`inplace=True`**　を指定することでできます。

# COMMAND ----------

nan_df.fillna({"security_deposit": "$0.00", "notes": "Missing"}, inplace=False)

# COMMAND ----------

# MAGIC %md <i18n value="5e800ca5-0801-4a83-84fe-ebe88eae9093"/>
# MAGIC
# MAGIC ## CSVへの書き込み (Write to CSV)
# MAGIC
# MAGIC [**to\_csv()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)メソッドを使うことで、以下のように **`pandas`**　DataFrameをCSVファイルに書き込むことができます。

# COMMAND ----------

file_path = DA.paths.working_dir.replace("dbfs:", "/dbfs") + ".csv"
df.to_csv(file_path, index=False)

# COMMAND ----------

# MAGIC %md <i18n value="c1bbcbf6-9c19-450a-ac92-1486f30a3f3c"/>
# MAGIC
# MAGIC **`read_csv`**　で、csv ファイルを再度読み込めます。

# COMMAND ----------

load_df = pd.read_csv(file_path)
load_df.head()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
