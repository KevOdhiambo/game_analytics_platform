from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

def create_spark_session():
    return SparkSession.builder \
        .appName("GameAnalyticsStreaming") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2") \
        .getOrCreate()

def process_stream(spark):
    schema = StructType([
        StructField("timestamp", TimestampType()),
        StructField("player_id", IntegerType()),
        StructField("session_id", IntegerType()),
        StructField("game_id", StringType()),
        StructField("level", IntegerType()),
        StructField("score", IntegerType()),
        StructField("items_collected", IntegerType()),
        StructField("time_played", IntegerType()),
        StructField("in_app_purchases", IntegerType()),
        StructField("device_type", StringType()),
        StructField("location", StringType())
    ])

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "game_events") \
        .load()

    parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

    query = parsed_df \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    spark = create_spark_session()
    process_stream(spark)