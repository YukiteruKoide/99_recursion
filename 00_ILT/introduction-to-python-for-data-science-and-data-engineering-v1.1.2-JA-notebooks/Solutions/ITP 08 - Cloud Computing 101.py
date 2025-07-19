# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="a18d57e2-019d-45b4-9ba4-b704a190ff0a"/>
# MAGIC
# MAGIC # クラウドコンピューティング１０１（Cloud Computing 101）
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) このレッスンでは<br>
# MAGIC - ローカル vs. オンプレミス vs. クラウドコンピューティングの対比
# MAGIC - クラウドコンピューティングの基本
# MAGIC - クラウドベースでSparkを利用したDatabricksの利用法

# COMMAND ----------

# MAGIC %md <i18n value="4e55ca41-dc1d-4f3f-9162-8b418a85c60e"/>
# MAGIC
# MAGIC #### ローカル環境（Local Execution）
# MAGIC
# MAGIC ローカル環境とは、コードを実行するためにローカルマシンの計算能力だけを利用することです。例えば、データサイエンティストがラップトップでJupyterノートブックを実行することです。
# MAGIC
# MAGIC
# MAGIC <img src="https://s3.us-west-2.amazonaws.com/files.training.databricks.com/courses/Python/LocalPicture.png" >

# COMMAND ----------

# MAGIC %md <i18n value="7d43d290-d840-449b-875e-063186261763"/>
# MAGIC
# MAGIC #### オンプレ環境（On-Prem）
# MAGIC
# MAGIC オンプレミスとは、on-premiseの略です。これは、誰かが複数のコンピュータを管理し、互いに通信してデータを保存し、コードを実行する状況を指します。この場合、1台のマシンよりもはるかに高い計算能力とストレージを提供します。
# MAGIC
# MAGIC
# MAGIC 以下は、オンプレミス環境を示す図です。
# MAGIC
# MAGIC <img src="https://s3.us-west-2.amazonaws.com/files.training.databricks.com/courses/Python/OnPremPicture.png">

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="232b8ed7-36c8-4e48-88d3-5c17143e3d76"/>
# MAGIC
# MAGIC #### クラウド環境（Cloud）
# MAGIC
# MAGIC オンプレミスでシステムを管理するのは難しく、コストがかかり、拡張性も低い。そこで、クラウドプロバイダーからストレージとコンピュータパワーを借りるという方法がよく使われています。
# MAGIC これらのプロバイダーは、通常、Amazon、Microsoft、Googleなどの大手テクノロジー企業です。
# MAGIC
# MAGIC この場合、ユーザーはウェブブラウザや他のアプリケーションからデータや計算にアクセスするだけで、実際のデータや計算は、これらの企業が管理するデータセンターと呼ばれる大規模なマシンの倉庫に保存・実行されています。これをクラウドベースの設定と呼んでいます。
# MAGIC
# MAGIC クラウドストレージを利用すれば、自社でデータセンターを作ったり管理したりする必要がないため、より安価で簡単に利用することができます。また、簡単に拡張することができます。その時々に必要なだけのストレージと計算能力を購入し、使い終わったら電源を切ればいいだけです。
# MAGIC
# MAGIC <img src="https://s3.us-west-2.amazonaws.com/files.training.databricks.com/courses/Python/CloudPicture.png" style="width:800px;height:500px;">

# COMMAND ----------

# MAGIC %md <i18n value="a5697312-b91f-4f54-bb69-2b835a9bd278"/>
# MAGIC
# MAGIC #### 仮想マシン（Virtual Machines）
# MAGIC
# MAGIC クラウドベースの環境では、クラウド プロバイダーが管理するコンピューターを使用して、コードを実行したりデータを保存したりします。
# MAGIC
# MAGIC このようにコードを実行するには、これらのコンピューターで **仮想マシン** を使用します。
# MAGIC
# MAGIC 仮想マシンは、同じコンピューター上の他の仮想マシンから、CPU、メモリー、ネットワーク、ディスクストレージを分離しています。
# MAGIC
# MAGIC クラウドコンピュータ上で仮想マシンを借りることで、同じく仮想マシンを借りている他のユーザーとの情報共有を気にすることなく、そのコンピュータが提供するリソースを利用することができるのです。

# COMMAND ----------

# MAGIC %md <i18n value="a74616ce-3011-4c79-b0f9-f72fbfbb032e"/>
# MAGIC
# MAGIC #### クラウドストレージ（Cloud Storage）
# MAGIC
# MAGIC クラウドプロバイダーは、データを簡単にクラウド上に保存する方法を提供しています。これらのサービスでは、データを信頼性の高い方法で保存することに特化したコンピューターとソフトウェアが使用され、拡張性も高いものとなってます。
# MAGIC
# MAGIC クラウドプロバイダーが提供するストレージの一種は、**オブジェクトストレージ**で、テキスト、画像、動画、その他のバイナリデータなど、あらゆる種類のデータを保存することができます。クラウドオブジェクトストレージの例としては、以下のようなものがあります。
# MAGIC
# MAGIC * [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/)
# MAGIC * Microsoftの[Azure Blob storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)
# MAGIC * [Google Cloud Storage](https://cloud.google.com/storage)
# MAGIC
# MAGIC クラウドプロバイダーは、MySQL、PostgreSQL、Microsoft SQL Serverなどのリレーショナルデータベースや、Amazon DynamoDB、Azure Cosmos DB、Google Cloud Bigtableなどのキーバリューストアやその他の「NoSQL」データベースを保存・管理するサービスも提供しています。

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="cc376440-5b2e-4d04-ae07-77c5a08b66d9"/>
# MAGIC
# MAGIC #### Databricks
# MAGIC
# MAGIC <img src="https://s3.us-west-2.amazonaws.com/files.training.databricks.com/images/databricks_cloud_overview.png" style="width:800px;height:500px;">
# MAGIC
# MAGIC Databricksは、さまざまなデータ分析、ビジネスインテリジェンス、データサイエンス、機械学習のタスクを実行および管理するための、統一されたクラウドベースのプラットフォームを提供します。Databricksは複数のクラウドプロバイダー上で動作し、そのクラウドプロバイダーの仮想マシンを使用してクラウドオブジェクトストレージに保存したデータを処理することができます。

# COMMAND ----------

# MAGIC %md <i18n value="e631525b-075f-485e-979a-dfc8ab90973e"/>
# MAGIC
# MAGIC #### Apache Spark
# MAGIC
# MAGIC 通常、1 台のコンピューターには、数ギガバイト以下のサイズのデータセットに対して計算を実行するためのメモリと計算能力があります。それ以上のサイズのデータセットは、1台のコンピューターのメモリーに収まらないか、1台のコンピューターで処理するのに許容できないほど長い時間がかかる。このような「ビッグデータ」の利用には、大きなデータセットをより小さなサブセットに分割し、その処理を複数のコンピュータに分散できるシステムが必要になります（分割されたデータセットのことを、**partitions**といい、複数のコンピューターにサブセットを分散することになります）
# MAGIC
# MAGIC [Apache Spark」（https://spark.apache.org/） は、大規模なデータセットを分散処理するためのオープンソースのデータ処理エンジンです。
# MAGIC
# MAGIC 例えば、大規模なデータセットがあり、その数値列のいくつかについて様々な統計量を計算したいとします。Apache Sparkを使えば、プログラムは読み込むデータセットと計算したい統計値を指定するだけでよい。そして、そのプログラムをApache Sparkの**クラスタ**として構成されたコンピュータのセットで実行することができます。実行すると、Sparkは自動的に
# MAGIC
# MAGIC * データセットをパーティションに分割する方法を決定
# MAGIC * パーティションごとの統計情報を計算するための命令とともに、それらのパーティションをクラスターのさまざまなコンピューターに割り当て
# MAGIC * 最終的にパーティションごとの統計情報を収集し、我々が要求した最終結果を算出
# MAGIC
# MAGIC Sparkは、もともとカリフォルニア大学バークレー校の研究プロジェクトとして誕生しました。2013年に、このプロジェクトはApache Software Foundationに寄贈されました。同年、Sparkの生みの親たちはDatabricksを設立しました。
# MAGIC
# MAGIC Databricksは、一般的に、プラットフォームの計算エンジンとしてApache Sparkを使用しています。Databricksは、クラウド提供の仮想マシンで構成されたSparkクラスターを稼働させ、クラウドオブジェクトストレージなどにあるデータを処理するためのシンプルな管理ツールを提供します。

# COMMAND ----------

# MAGIC %md-sandbox <i18n value="5b907bd3-bc39-41d1-8294-1be99f57ca26"/>
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/sparkcluster.png" style="width:600px;height:250px;">

# COMMAND ----------

# MAGIC %md <i18n value="4e483909-d12e-4a76-94e4-b5e04e726ce2"/>
# MAGIC
# MAGIC #### Databricks File System &mdash; DBFS
# MAGIC
# MAGIC Databricks File System (DBFS) は、Databricks ワークスペースにマウントされ、Databricks クラスターで利用できる分散ファイルシステムです。DBFSはスケーラブルなオブジェクトストレージの上に抽象化されたもので、以下のような利点があります。
# MAGIC
# MAGIC * ストレージオブジェクトを[mount](https://docs.databricks.com/data/databricks-file-system.html#mount-storage)できるため、認証情報を必要としないシームレスなデータアクセスが可能です。
# MAGIC * ストレージの URL ではなく、ディレクトリやファイルのセマンティクスを使用してオブジェクトストレージと対話することができます。
# MAGIC * オブジェクトストレージにファイルを永続化させるので、クラスタを終了してもデータを失うことがありません。
# MAGIC
# MAGIC オブジェクトストレージを DBFS にマウントすることで、オブジェクトストレージ内のオブジェクトをローカルファイルシステム上にあるかのようにアクセスできるようになります。それでは、`%fs mounts`、あるいは `dbutils.fs.mounts()` を呼び出して、現在マウントされているデータを見てみましょう。

# COMMAND ----------

# MAGIC %fs mounts

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

# MAGIC %md <i18n value="a499fb6b-eb36-4732-9af9-c84329cdce8a"/>
# MAGIC
# MAGIC #### Git によるコードのバージョン管理・共同作業(Code Versioning and Collaboration with Git)
# MAGIC
# MAGIC [Git](https://git-scm.com/)は、フリーでオープンソースのバージョン管理システムです。これは、コードの変更を追跡し、プロジェクトの異なるバージョンを保存することができることを意味します。必要に応じて以前のバージョンを復元することができます。また、異なる機能の開発に焦点を当てたプロジェクトの異なるバージョンを作成し、それらを結合して戻すことができるプロジェクトのブランチとマージが可能です。
# MAGIC
# MAGIC Gitは、ローカルマシンやDatabricks上で実行してバージョン管理を支援するツールですが、[GitHub](https://github.com/)と組み合わせることでコラボレーションツールとして輝きを放ちます。GitHubは、Gitコードリポジトリを管理できるクラウドベースのホスティングサービスで、複数のユーザーがプロジェクトのバージョンをダウンロードし、そのプロジェクトのために開発し、その変更をプッシュバックすることが可能です。複数のユーザーがプロジェクトのバージョンをダウンロードし、プロジェクトのために開発し、変更点をプッシュバックすることができます。これらの変更点はマージすることができるので、コードプロジェクトのバックボーンを形成するコラボレーションを容易に行うシステムを構築することができます。
# MAGIC
# MAGIC オープンソースの技術は、通常Githubリポジトリで公開され、誰でもコードをダウンロードして開発に参加することができます。例えば、Apache Sparkはオープンソースであり、GitHubのページ[こちら](https://github.com/apache/spark)から全てのコードの閲覧、ダウンロード、新機能の作成を支援することが可能です。

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
