from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg

def create_spark_session():
    return SparkSession.builder \
        .appName("GameAnalyticsBatch") \
        .config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.22.2") \
        .getOrCreate()

def process_batch_data(spark):
    # Read data from BigQuery
    df = spark.read.format("bigquery") \
        .option("table", "your-project.game_analytics.historical_data") \
        .load()

    # Perform aggregations
    result = df.groupBy("game_id") \
        .agg(
            sum("total_playtime").alias("total_playtime"),
            avg("total_score").alias("avg_score"),
            sum("total_in_app_purchases").alias("total_revenue")
        )

    # Write results back to BigQuery
    result.write.format("bigquery") \
        .option("table", "your-project.game_analytics.game_performance_summary") \
        .mode("overwrite") \
        .save()

if __name__ == "__main__":
    spark = create_spark_session()
    process_batch_data(spark)