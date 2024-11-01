from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import from_json, col, split
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName("streaming").getOrCreate()

ds = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092,kafka:9093")
    .option("subscribe", "spark-training")
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
    checkpoint_path = "data/tmp_students_checkpoint"
    path = "data/tmp_students"
    return (
        ds.transform(lambda df: with_normalized_names(df, student_schema))
        .writeStream.trigger(availableNow=True)
        .format("parquet")
        .option("checkpointLocation", checkpoint_path).start(path)
    )

if __name__ == "__main__":
    perform_available_now_data()
