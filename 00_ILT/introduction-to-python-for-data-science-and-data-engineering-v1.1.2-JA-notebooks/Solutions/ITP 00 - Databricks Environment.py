# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="7eb653c9-12ee-4cf3-b03a-aed5f21fbdf9"/>
# MAGIC
# MAGIC # Databricksの環境 (The Databricks Environment)
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png)このレッスンでは<br>
# MAGIC * Databricksを使い以下のことをします： 
# MAGIC   * クラスターを作成する
# MAGIC   * ノートブックでコードを実行する
# MAGIC   * ノートブックのエクスポート
# MAGIC
# MAGIC   
# MAGIC 参考：
# MAGIC * <a href="https://docs.databricks.com/" target="_blank">AWS</a>、<a href="https://docs.microsoft.com/en-us/azure/databricks/" target="_blank">Azure</a>、<a href="https://docs.gcp.databricks.com/" target="_blank">GCP</a>向けのDatabricksドキュメント

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="0bcfecf1-eb62-41a9-b095-6afa1cc6f92b"/>
# MAGIC
# MAGIC ## クラスターを作成する (Create a Cluster)
# MAGIC
# MAGIC コードを実行する前に、クラスターをセットアップする必要があります(クラスターとは、コードを実行するものです)。 
# MAGIC
# MAGIC ##### ステップ1： 
# MAGIC
# MAGIC 左側のメニューウィンドウで、図のように **クラスター**(Compute)タブをクリックします。
# MAGIC
# MAGIC <img src="http://files.training.databricks.com/images/ITP/ClickCompute.png" style="width:800px;height:400px;">
# MAGIC
# MAGIC ##### ステップ2：
# MAGIC
# MAGIC **クラスターの作成**(Create Cluster)ボタンをクリックします：
# MAGIC
# MAGIC <img src="http://files.training.databricks.com/images/ITP/CreateCluster.png" style="width:1100px;height:300px;">
# MAGIC
# MAGIC ##### ステップ3：
# MAGIC
# MAGIC クラスターの名前を追加し、その**クラスターモードが**Single Nodeに設定されていることを確認します。Single Nodeのクラスターを定義するポリシーがある場合は、それを使用することもできます。このクラスターのデフォルトのタイムアウトも設定することをお勧めします。 
# MAGIC
# MAGIC <img src="http://files.training.databricks.com/images/ITP/NameAndMode.png" style="width:600px;height:600px;">
# MAGIC
# MAGIC ##### ステップ4：
# MAGIC
# MAGIC 最後に、**クラスターを作成**(Create Cluster)をクリックします。
# MAGIC
# MAGIC <img src="http://files.training.databricks.com/images/ITP/CreateClusterFinal.png" style="width:600px;height:600px;">
# MAGIC
# MAGIC
# MAGIC ##### ステップ5：
# MAGIC
# MAGIC これで、ノートブックをクラスターにアタッチすることができます。
# MAGIC
# MAGIC <img src="http://files.training.databricks.com/images/ITP/SelectCluster.png" style="width:1200px;height:300px;">

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="fee29257-b1d9-49e6-a74f-53e1afc5bf29"/>
# MAGIC
# MAGIC ## コードの実行 (Run code)
# MAGIC
# MAGIC * 各ノートブックにはデフォルトの言語が指定されており，ここでは**Pythonが**指定されています。
# MAGIC * 以下のセルを以下のいずれかのオプションで実行します。
# MAGIC   * **CTRL+ENTER**または**CMD+RETURN**
# MAGIC   * **SHIFT+ENTER**または**SHIFT+RETURN**でセルを実行し、次のセルに移動します。
# MAGIC   * **セルを実行** (Run Cell)、**上記をすべて実行** (Run All Above)、**以下のすべてを実行** (Run All Below)のいずれかを使用します。<br/><img style="box-shadow: 5px 5px 5px 0px rgba(0,0,0,0.25); border: 1px solid rgba(0,0,0,0.25);" src="https://files.training.databricks.com/images/notebook-cell-run-cmd.png"/>
# MAGIC
# MAGIC お好みで下のコードを自由にいじってみてください。

# COMMAND ----------

print("I'm running Python!")

# COMMAND ----------

# MAGIC %md <i18n value="0341b4d6-fc23-4ef9-a846-5aab78d85112"/>
# MAGIC
# MAGIC ### マジック コマンド：%md
# MAGIC
# MAGIC 私たちのお気に入りの魔法のコマンド **%md** を使用すると、セルでMarkdown をレンダリングすることができます：
# MAGIC * このセルをダブルクリックすると、編集を開始します。
# MAGIC * 編集を停止するには、**ESCキー** を押します。
# MAGIC
# MAGIC # タイトル1
# MAGIC ## タイトル2
# MAGIC ### タイトル3
# MAGIC
# MAGIC これは、緊急放送システムのテストです。これはあくまでテストです。
# MAGIC
# MAGIC これは、**太字の**文字が入ったテキストです。
# MAGIC
# MAGIC これは、*斜体の*単語が含まれるテキストです。
# MAGIC
# MAGIC これは順序付きリストです
# MAGIC
# MAGIC 0. １回
# MAGIC 0. ２回
# MAGIC 0. ３回
# MAGIC
# MAGIC これは順不同のリストです
# MAGIC
# MAGIC * りんご
# MAGIC * 桃
# MAGIC * バナナ
# MAGIC
# MAGIC リンク/埋め込みHTML：<a href="http://bfy.tw/19zq" target="_blank">Markdownとは何ですか？</a>
# MAGIC
# MAGIC 画像：  
# MAGIC ![スパークエンジン](https://files.training.databricks.com/images/Apache-Spark-Logo_TM_200px.png)
# MAGIC
# MAGIC そしてもちろん、テーブルも。
# MAGIC
# MAGIC | 名前  | 年齢 | 犬種    |
# MAGIC |-------|-----|--------|
# MAGIC | バディ   | 2  | ゴールデンレトリバー   |
# MAGIC | ビンゴ  | 10  | ボーダーコリー |
# MAGIC | モモ  | 3  | ラブ   |

# COMMAND ----------

# MAGIC %md <i18n value="58b85c79-1640-47a8-90c2-325a2bd2e265"/>
# MAGIC
# MAGIC ## さらに学ぶ (Learning more)
# MAGIC
# MAGIC Databricksプラットフォームやノートブックの様々な機能をより深く知るために、ドキュメントを探索することをお勧めします。
# MAGIC * <a href="https://docs.databricks.com/user-guide/index.html" target="_blank"> ユーザーガイド</a>
# MAGIC * <a href="https://docs.databricks.com/user-guide/notebooks/index.html" target="_blank">ユーザーガイド / ノートブック</a>
# MAGIC * <a href="https://docs.databricks.com/administration-guide/index.html" target="_blank">管理ガイド</a>
# MAGIC * <a href="https://docs.databricks.com/release-notes/index.html" target="_blank">リリースノート</a>
# MAGIC * <a href="https://docs.databricks.com/" target="_blank">その他たくさん！</a>

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
