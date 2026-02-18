# Databricks notebook source
dir(spark)

# COMMAND ----------

from pyspark.sql.types import *

data = [(1,'Anuj'),(2,'Ravi'),(3,'Raj')]

schema = StructType([StructField(name="id",dataType = IntegerType()),StructField(name="name",dataType = StringType())])

df = spark.createDataFrame(data = data, schema= schema)
df.show()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

from pyspark.sql.types import *

data = [{"id":1,"name":"Anuj"}, {"id":2,"name":"Ravi"}, {"id":3,"name":"Raj"}]

df = spark.createDataFrame(data = data)
df.show()

# COMMAND ----------

# MAGIC %fs ls dbfs:/Workspace/Users/anujkhare60@gmail.com/Data/employees.csv

# COMMAND ----------

import pandas as pd

# Use this path format (no dbfs:, no /Workspace)
path = "/Workspace/Users/anujkhare60@gmail.com/Data/employees.csv"

df_pandas = pd.read_csv(path, header=0)

# Convert to Spark DF if you need Spark for larger operations
df = spark.createDataFrame(df_pandas)

display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

