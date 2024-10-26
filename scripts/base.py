# This examples basically taken from https://spark.apache.org/examples.html

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg

spark = SparkSession.builder.appName("ETL").getOrCreate()

df = spark.createDataFrame(
    [
        ("sue", 32),
        ("li", 3),
        ("bob", 75),
        ("heo", 13)
    ],
    ["first_name", "age"]
)

# Add new column that based on data in DataFrame
df1 = df.withColumn(
    "life_stage",
    when(col("age") < 13, "child")
    .when(col("age").between(13,19), "teenager")
    .otherwise("adult")
)

# Filtering of data
df1.where(col("life_stage").isin("teenager", "adult")).show()

# Aggregation
df1.select(avg("age")).show()

# Query the DataFrame with SQL
spark.sql("SELECT AVG(age) AS avg_age FROM {df1}", df1=df1).show()

# Query with grouping with SQL
spark.sql("SELECT life_stage, AVG(age) FROM {df1} GROUP BY life_stage", df1=df1).show()

# Save table as Parquet
df1.write.saveAsTable("some_people")

spark.sql("select * from some_people").show()