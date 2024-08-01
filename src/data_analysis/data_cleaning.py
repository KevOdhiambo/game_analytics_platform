import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

def create_spark_session():
    return SparkSession.builder \
        .appName("GameAnalyticsDataCleaning") \
        .getOrCreate()

def clean_data(spark):
    # Read data from BigQuery
    df = spark.read.format("bigquery") \
        .option("table", "your-project.game_analytics.raw_game_data") \
        .load()

    # Remove rows with null values
    df_cleaned = df.dropna()

    # Convert negative scores to 0
    df_cleaned = df_cleaned.withColumn("score", when(col("score") < 0, 0).otherwise(col("score")))

    # Remove outliers (e.g., playtime > 24 hours)
    df_cleaned = df_cleaned.filter(col("time_played") <= 86400)

    # Write cleaned data back to BigQuery
    df_cleaned.write.format("bigquery") \
        .option("table", "your-project.game_analytics.cleaned_game_data") \
        .mode("overwrite") \
        .save()

if __name__ == "__main__":
    spark = create_spark_session()
    clean_data(spark)