# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md <i18n value="be8397b6-c087-4d7b-8302-5652eec27caf"/>
# MAGIC
# MAGIC # Hyperopt Lab
# MAGIC
# MAGIC <a href="https://github.com/hyperopt/hyperopt" target="_blank">Hyperopt library</a> により、ランダムサーチまたはTree of Parzen Estimators (TPE) を用いたハイパーパラメータチューニングを並列に行うことができます。MLflowでハイパーパラメータの組み合わせごとに、ハイパーパラメータとそれに対応するメトリックスを記録することができます。詳しくは<a href="https://github.com/hyperopt/hyperopt/blob/master/docs/templates/scaleout/spark.md" target="_blank">SparkTrials / Hyperopt</a>でご参照ください。
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) このレッスンでは以下を行います。<br>
# MAGIC - シングルノードの機械学習モデルを学習する際に、デフォルトの **`Trials`** クラスではなく、 **`SparkTrials`** クラスを使用して分散チューニングの方法を学びます。
# MAGIC
# MAGIC > SparkTrialsは、1つのSpark Executorで一つのモデルを適合・評価するため、チューニングのための大規模なスケールアウトが可能になります。HyperoptでSparkTrialsを使うには、Hyperoptのfmin()関数にSparkTrialsオブジェクトを渡します。

# COMMAND ----------

# MAGIC %run "../Includes/Classroom-Setup"

# COMMAND ----------

# MAGIC %md <i18n value="13b0389c-cbd8-4b31-9f15-a6a9f18e8f60"/>
# MAGIC
# MAGIC Airbnbデータセットの数値型特徴量のみを抽出して読み込みます。

# COMMAND ----------

from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv(f"{DA.paths.datasets}/airbnb/sf-listings/airbnb-cleaned-mlflow.csv".replace("dbfs:/", "/dbfs/")).drop(["zipcode"], axis=1)

# split 80/20 train-test
X_train, X_test, y_train, y_test = train_test_split(df.drop(["price"], axis=1),
                                                    df[["price"]].values.ravel(),
                                                    test_size = 0.2,
                                                    random_state = 42)

# COMMAND ----------

# MAGIC %md <i18n value="b84062c7-9fb2-4d34-a196-98e5074c7ad4"/>
# MAGIC
# MAGIC **`objective_function`** を定義する必要があります。その中では、<a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html" target="_blank">ランダムフォレスト</a>の予測値をR2を使って評価します。
# MAGIC
# MAGIC 以下のコードで、 **`r2`** を計算してを返します（R2を最大化しようとしているので、負の値として返す必要があります）。

# COMMAND ----------

# TODO
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer, r2_score
from numpy import mean
  
def objective_function(params):
    # set the hyperparameters that we want to tune:
    max_depth = <FILL_IN>
    max_features = <FILL_IN>

    regressor = RandomForestRegressor(max_depth=max_depth, max_features=max_features, random_state=42)

    # Evaluate predictions
    r2 = mean(cross_val_score(regressor, X_train, y_train, cv=3))

    # Note: since we aim to maximize r2, we need to return it as a negative value ("loss": -metric)
    return <FILL_IN>

# COMMAND ----------

# MAGIC %md <i18n value="7b10a96d-d868-4603-ab84-50388a8f50fc"/>
# MAGIC
# MAGIC HyperOptの探索空間を定義する必要があります。 **`max_depth`** は2-10、 **`max_features`** は "auto"、"sqrt"、"log2"のいずれかを指定します。

# COMMAND ----------

# TODO
from hyperopt import hp

max_features_choices =  ["auto", "sqrt", "log2"]
search_space = {
    "max_depth": <FILL_IN>
    "max_features": <FILL_IN>
}

# COMMAND ----------

# MAGIC %md <i18n value="6db6a36a-e1ca-400d-81fc-20ad5a794a01"/>
# MAGIC
# MAGIC デフォルトの **`Trials`** クラスを使用する代わりに、 **`SparkTrials`** クラスを利用してSparkのExecutor群にチューニングタスクを分散するトリガーとすることが可能です。Databricksでは、SparkTrialsの実行がMLflowで自動的に記録されます。
# MAGIC
# MAGIC **`SparkTrials`** には3つのオプション引数、すなわち、 **`parallelism`** , **`timeout`** , **`spark_session`** があります。詳しくは、こちらの<a href="http://hyperopt.github.io/hyperopt/scaleout/spark/" target="_blank">ページ</a>をご参照ください。
# MAGIC
# MAGIC 以下のコードで、 **`fmin`** 関数を埋めてください。

# COMMAND ----------

# TODO
from hyperopt import fmin, tpe, SparkTrials
import mlflow
import numpy as np

# Number of models to evaluate
num_evals = 8
# Number of models to train concurrently
spark_trials = SparkTrials(parallelism=2)
# Automatically logs to MLflow
best_hyperparam = fmin(<FILL_IN>)

# Re-train best model and log metrics on test dataset
with mlflow.start_run(run_name="best_model"):
    # get optimal hyperparameter values
    best_max_depth = <FILL_IN>
    best_max_features = <FILL_IN>

    # train model on entire training data
    regressor = RandomForestRegressor(max_depth=best_max_depth, max_features=best_max_features, random_state=42)
    regressor.fit(X_train, y_train)

    # evaluate on holdout/test data
    r2 = regressor.score(X_test, y_test)

    # Log param and metric for the final model
    mlflow.log_param("max_depth", best_max_depth)
    mlflow.log_param("max_features", best_max_features)
    mlflow.log_metric("loss", r2)

# COMMAND ----------

# MAGIC %md <i18n value="398681fb-0ab4-4886-bb08-58117da3b7af"/>
# MAGIC
# MAGIC これで、MLflowのUIを使ってすべてのモデルを比較することができます。
# MAGIC
# MAGIC ハイパーパラメータのチューニングの効果を理解するため：
# MAGIC
# MAGIC 0. Runを選択し、[比較]をクリックします。
# MAGIC 0. 散布図において、X軸にハイパーパラメータを、Y軸にLoss(損失)を選択します。

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
