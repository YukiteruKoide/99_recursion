# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="1736b729-f36e-45fe-9340-bef22ff58167"/>
# MAGIC
# MAGIC # Advanced Pandas Lab
# MAGIC
# MAGIC 練習問題：2018年、有機アボカドの平均総販売量が最も多いのはアメリカのどの地域か？

# COMMAND ----------

# MAGIC %run "../Includes/Classroom-Setup"

# COMMAND ----------

# MAGIC %md <i18n value="e460c1e8-54fb-4175-9482-ac1ee5be0945"/>
# MAGIC
# MAGIC まず　pandas を　import しましょう

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md <i18n value="77f86875-8f35-4c68-a04c-1f99482cc0ce"/>
# MAGIC
# MAGIC ## CSVファイルの読み込み（Read CSV）
# MAGIC
# MAGIC 有機アボカドの平均販売総量が最も多い地域を決定するために、[アボカド価格](https://www.kaggle.com/datasets/neuromusic/avocado-prices)に関するデータセットを使用することにします。
# MAGIC
# MAGIC データを読み込むためのコードを用意しました。

# COMMAND ----------

file_path = f"{DA.paths.datasets}/avocado/avocado.csv".replace("dbfs:", "/dbfs")
df = pd.read_csv(file_path).drop("Unnamed: 0", axis=1) # drop unnamed index column from data
df.head(3)

# COMMAND ----------

# MAGIC %md <i18n value="c6d6129e-db7a-41e5-a14d-077dc501de1d"/>
# MAGIC
# MAGIC ## 問題１: データ分析
# MAGIC
# MAGIC さて、DataFrame　を用意したので、分析を始める準備ができました。目標は、2018年の有機オーガニックアボカドの販売に関する平均総量が最も高いのは米国のどの地域かを判断することです。
# MAGIC
# MAGIC **`type`と`year`**　でフィルタリングして、2018年のオーガニックに関する販売量を見つけ、その結果を **`filtered_df`** に代入します。

# COMMAND ----------

# TODO
filtered_df = df[(df["type"] == "organic") & (df["year"] == 2018)]
filtered_df

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="bf6590ba-46e2-4cf7-aecb-405818023d33"/>
# MAGIC
# MAGIC <button onclick="myFunction2()" > クリックするとヒントが表示されます</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC boolean　配列の作成時には、and 演算子に & を使用することを忘れないでください、
# MAGIC   df[(bool_array) & (bool_array)]。
# MAGIC   
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

assert filtered_df.shape == (648, 13), "There are not the correct number of rows or columns"
assert filtered_df["year"].min() == 2018, "Only look at 2018 data"
assert len(filtered_df[filtered_df["type"] == "conventional"]) == 0, "There should be no rows about non-organic avocado sales"
print("Test passed!")

# COMMAND ----------

# MAGIC %md <i18n value="7555f96b-93e7-414a-9064-b0827ecaf1e6"/>
# MAGIC
# MAGIC ##　問題２: 答えとなる地域を見つける
# MAGIC
# MAGIC 次に、　**`filtered_df`** を使用して、2018年の有機アボカド販売の平均総量が最も多い上位10地域を出力します。
# MAGIC * これを行うには、各行が **`region`** とその地域の有機アボカドの平均 **`Total Volume`** からなる **`filtered_df`** を使用して DataFrame を作成します。
# MAGIC * そのDataFrameを降順にソートし、最初の10行を保持します。
# MAGIC * 出力は **`final_df`** 変数に代入されます。

# COMMAND ----------

# ANSWER
final_df = filtered_df.groupby(["region"])[["Total Volume"]].mean().sort_values(["Total Volume"], ascending=False).head(10)
final_df

# COMMAND ----------

testing_df = final_df.reset_index() if final_df.index.name == "region" else final_df
assert type(testing_df) == pd.DataFrame, "final_df should be a DataFrame, make sure it is not a Series. If it is a Series, make sure to use [['Total Volume']] instead of ['Total Volume']"
assert (testing_df.columns == ["region", "Total Volume"]).all(), "The only columns should be region and Total Volume. Make sure to use reset_index and that region is not currently the index column"
assert len(testing_df) == 10, "Only return the top 10 rows"
assert testing_df.iloc[0].values[0] == "TotalUS", "TotalUS should be the on the top row"
assert round(testing_df.iloc[0].values[1], 2) == 1510487.83, "TotalUS should have an average Total Volume of around 1510488"
assert testing_df.iloc[9].values[0] == "LosAngeles", "LosAngeles should be the on the 10th row"
assert round(testing_df.iloc[9].values[1], 2) == 102628.31, "LosAngeles should have an average Total Volume of around 102628"
print("Test passed!")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>

# COMMAND ----------


