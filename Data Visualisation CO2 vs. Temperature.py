# Databricks notebook source
# MAGIC %md
# MAGIC # Data Visualisation - CO2 vs. Temperature
# MAGIC Now that we have data in a desired shape, let's visualise it using different visualisation libraries in Python!

# COMMAND ----------

# MAGIC %md
# MAGIC ## Install some dependencies

# COMMAND ----------

!pip install pandas==1.2 s3fs plotly scikit-learn==0.24.2 dash


# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Read Parquet Data from S3
# MAGIC Let's read our data from S3. Remember, that typically, there would be some access layer in between you and the data. Right now, we're reading non-sensitive data from an S3 bucket (see `storage_options`) and [other examples](https://docs.dask.org/en/stable/how-to/connect-to-remote-data.html). Don't forget to replace `"YOUR-BUCKET-NAME"` with the bucket that contains your data.

# COMMAND ----------

import pandas as pd

bucket_name="YOUR-BUCKET_NAME" # TODO: Change me!
country_df = pd.read_parquet("s3://" + bucket_name + "/data-transformation/CountryEmissionsVsTemperatures.parquet/", storage_options={'anon': True, 'use_ssl': False})
display(country_df)

# COMMAND ----------

## If you would like to experiment with Machine Learning
import sklearn

# COMMAND ----------

country_df['Country'].unique()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Plotly Examples
# MAGIC Plotly is a common tool for data visualisation. Let's have a look at how it works.
# MAGIC 
# MAGIC Examples from [Plotly](https://plotly.com/python/getting-started/)

# COMMAND ----------

import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.write_html('first_figure.html', auto_open=True)
fig

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercise: Visualise CO2 vs. Temperature Data
# MAGIC Use Plotly to play around with the project data to see if you can come up with meaningful visualisations that answer our original questions:
# MAGIC * Which countries are worse-hit (higher temperature anomalies)?
# MAGIC * Which countries are the biggest emitters?
# MAGIC * What are some attempts of ranking “biggest polluters” in a sensible way?

# COMMAND ----------


