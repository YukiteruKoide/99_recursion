# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="b3cd11bc-171b-4de8-9515-330a470d1c82"/>
# MAGIC
# MAGIC # アジェンダ (Agenda)
# MAGIC ## データサイエンスとデータエンジニアリングのためのPython入門 (Introduction to Python for Data Science & Data Engineering)

# COMMAND ----------

# MAGIC %md <i18n value="d420b695-d64c-4cef-bba6-a32097b84fd4"/>
# MAGIC
# MAGIC ## 1日目 午前
# MAGIC | 時間 | レッスン &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | 内容 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 30分  | **自己紹介と設定**                               | *自己紹介と教材* |
# MAGIC | 30分  | **[Databricks環境]($./ITP 00 - Databricks Environment)** |  *Databricks環境とコース内容の概要*| 
# MAGIC | 10分  | **休憩**                                               ||
# MAGIC | 50分  | **[変数とデータ型]($./ITP 01 - Data Types and Variables) & [ラボ]($./Labs/ITP 01L - Data Types and Variables Lab)**  |  *ビルトインデータ型、変数に値の代入文、関連関数*|
# MAGIC | 10分  | **休憩**                                               ||
# MAGIC | 50分  | **[制御フロー]($./ITP 02 - Control Flow) & [ラボ]($./Labs/ITP 02L - Control Flow Lab)**    | *条件文によるPythonアプリケーションの制御フロー* |

# COMMAND ----------

# MAGIC %md <i18n value="83b8d3bd-8f78-4397-a98a-96c576905e2b"/>
# MAGIC
# MAGIC ## 1日目 午後
# MAGIC | 時間 | レッスン &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | 内容 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 50分  | **[関数]($./ITP 03 - Functions) & [ラボ]($./Labs/ITP 03L - Functions Lab)** | *コードを再利用しパラメータ化するための関数作成と利用* |
# MAGIC | 10分  | **休憩**                                               ||
# MAGIC | 55分  | **[コレクション型とメソッド]($./ITP 04 - Collection Types and Methods) & [Lab]($./Labs/ITP 04L - Collection Types and Methods Lab)**      | *高度なデータ型とメソッド*|
# MAGIC | 10分  | **休憩**                                               ||
# MAGIC | 55分  | **[ループ]($./ITP 05 - Loops) & [ラボ]($./Labs/ITP 05L - Loops Lab)**| *Forループによる制御フロー文* |
# MAGIC | 10分  | **休憩**                                               ||
# MAGIC | 25分  | **[例外]($./ITP 06 - Exceptions)**| *Assert文と例外処理*  |

# COMMAND ----------

# MAGIC %md <i18n value="a7f0af74-9f7f-411f-8a63-f1ee625408ba"/>
# MAGIC
# MAGIC ## 2日目 午前
# MAGIC | 時間 | レッスン &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | 内容 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 20分  | **復習**                               | *1日目の復習* |
# MAGIC | 55分  | **[クラス]($./ITP 07 - Classes) & [ラボ]($./Labs/ITP 07L - Classes Lab)** | *クラスとカスタムデータ型* | 
# MAGIC | 10分  | **休憩**                                               ||
# MAGIC | 40分 | **[クラウドコンピューティング101]($./ITP 08 - Cloud Computing 101)**| *クラウドコンピューティングとDatabricksの関わりの概要*  |
# MAGIC | 25分 |**[ライブラリ]($./ITP 09 - Libraries)**  | *ライブラリ、PyPI、使用方法* |
# MAGIC | 10分  | **休憩**                                               ||
# MAGIC | 30分| **[Pandas Overview]($./ITP 10 - Pandas Overview)**    | *データ操作のための業界標準ライブラリ* |

# COMMAND ----------

# MAGIC %md <i18n value="5ecab748-fb7d-46d0-9758-029833813e9f"/>
# MAGIC
# MAGIC ## 2日目 午後
# MAGIC | 時間 | レッスン &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 35分| **[Pandasラボ]($./Labs/ITP 10L - Pandas Overview Lab)**    | *データ操作のための業界標準ライブラリのラボ* |
# MAGIC | 45分  | **[Pandas上級編]($./ITP 11 - Advanced Pandas)** |  *さらに高度なPandas機能*|
# MAGIC | 10分  | **休憩**                                               ||
# MAGIC | 30分  | **[Pandas上級編ラボ]($./Labs/ITP 11L - Advanced Pandas Lab)** |  *さらに高度なPandas機能ラボ*|
# MAGIC | 10分  | **休憩**                                               ||
# MAGIC | 55分  | **[データの可視化]($./ITP 12 - Data Visualization) & [Lab]($./Labs/ITP 12L - Data Visualization Lab)**      | *Databricks、Pandas、Seabornによるデータの可視化*|
# MAGIC | 30分  | **[SparkでPandasをスケールさせる]($./ITP 13 - Scaling Pandas with Spark)**  | *内部的にSparkを活用するPandasコードの作成*|

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
