# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# DBTITLE 0,--i18n-a1996ff5-af6a-49a6-9cf6-bf7e2f11d9ff
# MAGIC %md
# MAGIC # 重複データ削除のデータラボ (De-Duping Data Lab)
# MAGIC
# MAGIC この練習問題では、顧客から受け取ったファイルについてETLの処理をします。このファイルは人々に関する以下のような情報を含んでいます：
# MAGIC
# MAGIC * 苗字、ミドルネーム、名前
# MAGIC * 性別
# MAGIC * 生年月日
# MAGIC * 社会保険番号
# MAGIC * 収入
# MAGIC
# MAGIC しかし、顧客から受け取るデータには残念ながらありがちですが、このファイルには重複したレコードが含まれています。さらに悪いことに：
# MAGIC
# MAGIC * いくつかのレコードでは名前が大文字小文字両方が含まれていたり(例 "Carol")、また別のレコードでは全て大文字(例 "CAROL")だったりします。
# MAGIC * 社会保険番号も統一されていません。いくつかのレコードはハイフンで区切られており(例 "992-83-4829")、また別のものはハイフンがなかったりします("992834829")。
# MAGIC
# MAGIC もし全ての名前に関するフィールドが（大文字小文字の違いを無視して）一致していたら、生年月日と収入も一致するようになっており、また社会保険番号もフォーマットを揃えたならば一致するようになっています。
# MAGIC
# MAGIC あなたのタスクは重複レコードを削除することです。特別な要件として:
# MAGIC
# MAGIC * 重複を削除します。それらの１つを残さないといけませんが、どちらレコードを残しても構いません。
# MAGIC * カラムのフォーマットを維持してください。例えば、名前のカラムを全て小文字で出力したら、要件を満たしていないことになります。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint"> 最初、データセットには103,000件のレコードがあります。
# MAGIC 重複性排除をすると、100,000件のレコードとなります。
# MAGIC
# MAGIC 次に、**delta_dest_dir**という変数名で指定されたディレクトリに、デルタフォーマットの１つのファイルで結果を出力してください。
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_32.png" alt="Hint"> データフレームのパーティション数と出力ファイル数の関係について思い出してください。
# MAGIC
# MAGIC ##### メソッド (Methods)
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/io.html" target="_blank">DataFrameReader</a>
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html" target="_blank">DataFrame</a>
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html" target="_blank">Built-In Functions</a>
# MAGIC - <a href="https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/io.html" target="_blank">DataFrameWriter</a>

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup

# COMMAND ----------

# DBTITLE 0,--i18n-c9d419b3-237e-4d75-89ad-c184d40bb7b3
# MAGIC %md
# MAGIC まずファイルを見てみると手掛かりになるでしょう。<strong>`dbutils.fs.head()`</strong>を使ってフォーマットを見てみましょう。

# COMMAND ----------

dbutils.fs.head(f"{DA.paths.datasets}/people/people-with-dups.txt")

# COMMAND ----------

# ANSWER

source_file = f"{DA.paths.datasets}/people/people-with-dups.txt"
delta_dest_dir = f"{DA.paths.working_dir}/people"

# In case it already exists
dbutils.fs.rm(delta_dest_dir, True)

# dropDuplicates() will introduce a shuffle, so it helps to reduce the number of post-shuffle partitions.
spark.conf.set("spark.sql.shuffle.partitions", 8)

# Okay, now we can read this thing
df = (spark
      .read
      .option("header", "true")
      .option("inferSchema", "true")
      .option("sep", ":")
      .csv(source_file)
     )

# COMMAND ----------

# ANSWER
from pyspark.sql.functions import col, lower, translate

deduped_df = (df
             .select(col("*"),
                     lower(col("firstName")).alias("lcFirstName"),
                     lower(col("lastName")).alias("lcLastName"),
                     lower(col("middleName")).alias("lcMiddleName"),
                     translate(col("ssn"), "-", "").alias("ssnNums")
                     # regexp_replace(col("ssn"), "-", "").alias("ssnNums")  # An alternate function to strip the hyphens
                     # regexp_replace(col("ssn"), """^(\d{3})(\d{2})(\d{4})$""", "$1-$2-$3").alias("ssnNums")  # An alternate that adds hyphens if missing
                    )
             .dropDuplicates(["lcFirstName", "lcMiddleName", "lcLastName", "ssnNums", "gender", "birthDate", "salary"])
             .drop("lcFirstName", "lcMiddleName", "lcLastName", "ssnNums")
            )

# COMMAND ----------

# ANSWER

# Now, write the results in Delta format as a single file. We'll also display the Delta files to make sure they were written as expected.

(deduped_df
 .repartition(1)
 .write
 .mode("overwrite")
 .format("delta")
 .save(delta_dest_dir)
)

display(dbutils.fs.ls(delta_dest_dir))

# COMMAND ----------

# DBTITLE 0,--i18n-57d9884d-057e-4815-8814-4e65d842d952
# MAGIC %md
# MAGIC **結果の検証**

# COMMAND ----------

verify_files = dbutils.fs.ls(delta_dest_dir)
verify_delta_format = False
verify_num_data_files = 0
for f in verify_files:
    if f.name == "_delta_log/":
        verify_delta_format = True
    elif f.name.endswith(".parquet"):
        verify_num_data_files += 1

assert verify_delta_format, "Data not written in Delta format"
assert verify_num_data_files == 1, "Expected 1 data file written"

verify_record_count = spark.read.format("delta").load(delta_dest_dir).count()
assert verify_record_count == 100000, "Expected 100000 records in final result"

del verify_files, verify_delta_format, verify_num_data_files, verify_record_count
print("All test pass")

# COMMAND ----------

# DBTITLE 0,--i18n-a532d460-fd0b-44b3-8130-337c413846b7
# MAGIC %md
# MAGIC ## クラスで利用したリソースの削除 (Clean up classroom)
# MAGIC 以下のセルを実行してリソースを削除してください。

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
