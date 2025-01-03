from pyspark.sql import SparkSession
from src.processing.spark_processor import SparkProcessor

def test_process_data():
    spark = SparkSession.builder.master("local[*]").appName("Test").getOrCreate()
    processor = SparkProcessor("local[*]")

    data = [{"original_column": 1}, {"original_column": 2}]
    df = spark.createDataFrame(data)

    processed_df = processor.process_data(df.collect())
    assert "processed_column" in processed_df.columns
