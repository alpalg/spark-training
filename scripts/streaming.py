from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import from_json, col, split
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName("streaming").getOrCreate()

# Expected data
"""
{"student_name":"someXXperson", "graduation_year":"2023", "major":"math"}
{"student_name":"liXXyao", "graduation_year":"2025", "major":"physics"}
"""

ds = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9095,kafka:9096")
    .option("subscribe", "spark-training")
    .option("startingOffsets", "earliest")
    .load()
)

student_schema = StructType([
    StructField("student_name", StringType()),
    StructField("graduation_year", StringType()),
    StructField("major", StringType()),
])

def with_normalized_names(df: DataFrame, schema: StructType) -> DataFrame:
    parsed_df = (
        df.withColumn("json_data", from_json(col("value").cast("string"), schema))
        .withColumn("student_name", col("json_data.student_name"))
        .withColumn("graduation_year", col("json_data.graduation_year"))
        .withColumn("major", col("json_data.major"))
        .drop(col("json_data"))
        .drop(col("value"))
    )

    split_col = split(parsed_df["student_name"], "XX")
    return (
        parsed_df.withColumn("first_name", split_col.getItem(0))
        .withColumn("last_name", split_col.getItem(1))
        .drop(col("student_name"))
    )

def perform_available_now_data():
    checkpoint_path = "/opt/spark/work-dir/spark-warehouse/tmp_students_checkpoint"
    path = "/opt/spark/work-dir/spark-warehouse/tmp_students"
    return (
        ds.transform(lambda df: with_normalized_names(df, student_schema))
        .writeStream.trigger(availableNow=True)
        .format("csv")
        .option("checkpointLocation", checkpoint_path).start(path)
    )

if __name__ == "__main__":
    query = perform_available_now_data()
    query.awaitTermination()
