# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-26e0e9c0-768d-4b35-9e7c-edf0bbca828b
# MAGIC %md
# MAGIC ## 分析のためのデータアクセスの管理
# MAGIC このモジュールは、Databricks Academy によるData Engineer Learning Pathの一部です。
# MAGIC
# MAGIC #### レッスン
# MAGIC スライド: Unity Catalog (UC) 紹介<br>
# MAGIC DE 6.1 - [UC によるデータの作成と管理]($./DE 6.1 - Create and Govern Data with UC)<br>
# MAGIC DE 6.2L - [UC でテーブルを作成して共有]($./DE 6.2L - Create and Share Tables in Unity Catalog)<br>
# MAGIC DE 6.3L - [ビューの作成とテーブルアクセスの制限]($./DE 6.3L - Create Views and Limit Table Access)<br>
# MAGIC
# MAGIC #### UCによるアドミニストレーション - オプション
# MAGIC DE 6.99 - アドミニストレーション（オプション）<br>
# MAGIC DE 6.99.2 - [UCアクセス用のコンピューティングリソースの作成]($./DE 6.99 - OPTIONAL Administration/DE 6.99.2 - Create compute resources for Unity Catalog access)<br>
# MAGIC DE 6.99.3 - [テーブルをUCにアップグレード]($./DE 6.99 - OPTIONAL Administration/DE 6.99.3 - OPTIONAL Upgrade a Table to Unity Catalog)<br>
# MAGIC
# MAGIC #### 前提条件
# MAGIC * Databricks Lakehouseプラットフォームの初級レベルの知識 (Lakehouseプラットフォームの構造と利点に関する高度な知識)
# MAGIC * SQLの初級レベルの知識 (基本的なクエリを理解し、構築する能力)
# MAGIC
# MAGIC #### 技術的な考慮事項
# MAGIC このコースは Databricks Community Edition では機能できず、Unity Catalog をサポートするクラウドでのみ機能できます。 すべての演習を完全に実行するには、ワークスペースレベルとアカウントレベルの両方での管理アクセスが必要です。 いくつかのオプションタスクを機能させれため、クラウド環境インフラへのさらな詳細アクセス権が必要です。

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
