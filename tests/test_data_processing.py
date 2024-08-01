import pytest
from pyspark.sql import SparkSession
from src.data_processing.spark_streaming import create_spark_session, process_stream

@pytest.fixture(scope="module")
def spark():
    return create_spark_session()

def test_spark_session(spark):
    assert isinstance(spark, SparkSession)

def test_process_stream(spark):
    df = spark.createDataFrame([
        ("2023-05-01 10:00:00", 1, 1001, "game1", 5, 100, 10, 300, 0, "mobile", "US")
    ], ["timestamp", "player_id", "session_id", "game_id", "level", "score", "items_collected", "time_played", "in_app_purchases", "device_type", "location"])
    
    result = process_stream(df)
    assert result.count() == 1