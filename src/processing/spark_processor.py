from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, FloatType

class SparkProcessor:
    def __init__(self, master_url="local[*]"):
        self.spark = SparkSession.builder \
            .master(master_url) \
            .appName("BigDataPipeline") \
            .getOrCreate()

    def process_data(self, input_data):
        # Define o schema dos dados
        schema = StructType([
            StructField("key", StringType(), True),
            StructField("value", FloatType(), True)
        ])
        # Cria o DataFrame Spark
        df = self.spark.read.json(self.spark.sparkContext.parallelize(input_data), schema)
        # Adiciona uma nova coluna transformada
        processed_df = df.withColumn("transformed_value", col("value") * 2)
        return processed_df

    def write_to_hdfs(self, df, hdfs_path):
        df.write.mode("overwrite").parquet(hdfs_path)
        print(f"Data written to HDFS at {hdfs_path}")

if __name__ == "__main__":
    processor = SparkProcessor()
    sample_data = [{"key": "1", "value": 1.2}, {"key": "2", "value": 3.4}]
    processed = processor.process_data(sample_data)
    processed.show()
    processor.write_to_hdfs(processed, "hdfs://hadoop:9000/data/processed")
