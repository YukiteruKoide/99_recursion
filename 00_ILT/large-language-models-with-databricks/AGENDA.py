# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC
# MAGIC
# MAGIC ## Large Language Models with Databricks
# MAGIC
# MAGIC This course is aimed at data scientists, machine learning engineers, and other data practitioners looking to build LLM-centric applications with the latest and most popular frameworks. In this course, you will build common LLM applications using Hugging Face, develop retrieval-augmented generation (RAG) applications, create multi-stage reasoning pipelines using LangChain, fine-tune LLMs for specific tasks, assess and address societal considerations of using LLMs, and learn how to deploy your models at scale leveraging LLMOps best practices.
# MAGIC
# MAGIC By the end of this course, you will have built an end-to-end LLM workflow that is ready for production!
# MAGIC
# MAGIC ## Course agenda
# MAGIC
# MAGIC | Time | Module &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Lessons &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 55m    | **[Introduction]($./LLM 00 - Introduction/LLM 00a - Install Datasets)**    | Generative AI and LLMs</br>Practical NLP Primer</br>Databricks and LLMs</br>[Demo: Install Datasets]($./LLM 00 - Introduction/LLM 00a - Install Datasets)|
# MAGIC | 85m    | **[Common Applications with LLMs]($./LLM 01 - Common Applications with LLMs/LLM 01 - Common Applications)** | Common Applications Overview </br> [Common Applications Demo]($./LLM 01 - Common Applications with LLMs/LLM 01 - Common Applications) </br> [Common Applications Lab]($./LLM 01 - Common Applications with LLMs/LLM 01L - Common Applications Lab) | 
# MAGIC | 10m  | **Break**                                            ||
# MAGIC | 90m  | **[Retrieval-Augmented Generation (RAG)]($./LLM 02 - Retrieval-Augmented Generation [RAG]/LLM 02 - RAG with FAISS and Chroma)** | Retrieval-augmented Generation Overview </br> [Retrieval-augmented Generation Demo]($./LLM 02 - Retrieval-Augmented Generation [RAG]/LLM 02 - RAG with FAISS and Chroma) </br> [Retrieval-augmented Generation Lab]($./LLM 02 - Retrieval-Augmented Generation [RAG]/LLM 02L - RAG Lab) </br> [RAG with Pinecone [OPTIONAL]]($./LLM 02 - Retrieval-Augmented Generation [RAG]/LLM 02a - RAG with Pinecone [OPTIONAL]) </br> [RAG with Weaviate [OPTIONAL]]($./LLM 02 - Retrieval-Augmented Generation [RAG]/LLM 02b - RAG with Weaviate [OPTIONAL])| 
# MAGIC | 10m  | **Break**                                               ||
# MAGIC | 35m    | **[Multi-stage Reasoning with LLM Chains]($./LLM 03 - Multi-stage Reasoning with LLM Chains/LLM 03 - Building LLM Chains)**    | Multi-stage Reasoning Overview </br> [Multi-stage Reasoning Demo]($./LLM 03 - Multi-stage Reasoning with LLM Chains/LLM 03 - Building LLM Chains) </br> [Multi-stage Reasoning Lab]($./LLM 03 - Multi-stage Reasoning with LLM Chains/LLM 03L - Building LLM Chains Lab) |
# MAGIC | 10m | **Break**                                               ||
# MAGIC | 90m  | **[Fine-tuning LLMs]($./LLM 04 - Fine-tuning LLMs/LLM 04 - Fine-tuning LLMs)**       | Fine-tuning LLMs Overview </br> [Fine-tuning LLMs Demo]($./LLM 04 - Fine-tuning LLMs/LLM 04 - Fine-tuning LLMs) </br> [Fine-tuning LLMs Lab]($./LLM 04 - Fine-tuning LLMs/LLM 04L - Fine-tuning LLMs Lab) |
# MAGIC | 75m  | **[Evaluating LLMs]($./LLM 05 - Evaluating LLMs/LLM 05 - Evaluating LLMs)**      | Evaluating LLMs Overview </br> [Evaluating LLMs Demo]($./LLM 05 - Evaluating LLMs/LLM 05 - Evaluating LLMs) </br> [Evaluating LLMs Lab]($./LLM 05 - Evaluating LLMs/LLM 05L - Evaluating LLMs Lab) |
# MAGIC | 10m  | **Break**                                               ||
# MAGIC | 75m |**[LLMs and Society]($./LLM 06 - LLMs and Society/LLM 06 - LLMs and Society)** |  Society and LLMs Overview </br> [Society and LLMs Demo]($./LLM 06 - LLMs and Society/LLM 06 - LLMs and Society) </br> [Society and LLMs Lab]($./LLM 06 - LLMs and Society/LLM 06L - LLMs and Society Lab) |
# MAGIC | 10m  | **Break**                                               ||
# MAGIC | 70m  | **[LLMOps]($./LLM 07 - LLMOps/LLM 07 - LLMOps)**  | LLMOps Overview </br>[LLMOps Demo]($./LLM 07 - LLMOps/LLM 07 - LLMOps) </br>[LLMOps Lab]($./LLM 07 - LLMOps/LLM 07L - LLMOps Lab) |
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC
# MAGIC * To run demo and lab notebooks, you need to use one of the following Databricks runtime(s): **13.3.x-cpu-ml-scala2.12, 13.3.x-gpu-ml-scala2.12**

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2024 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
