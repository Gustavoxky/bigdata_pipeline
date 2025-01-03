from pyspark.sql import SparkSession
from src.storage.hdfs_writer import HDFSWriter
import os

def test_write_to_hdfs(tmp_path):
    spark = SparkSession.builder.master("local[*]").appName("Test").getOrCreate()
    writer = HDFSWriter(f"{tmp_path}/output")

    data = [{"col1": 1}, {"col1": 2}]
    df = spark.createDataFrame(data)

    writer.write_to_hdfs(df)

    output_files = os.listdir(f"{tmp_path}/output")
    assert len(output_files) > 0
