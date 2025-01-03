from src.ingestion.kafka_consumer import KafkaConsumerWrapper
from src.processing.spark_processor import SparkProcessor
from src.storage.hdfs_writer import HDFSWriter
from src.config import KAFKA_BROKER, KAFKA_TOPIC, SPARK_MASTER, HDFS_PATH

def main():
    # Ingest data
    consumer = KafkaConsumerWrapper(KAFKA_TOPIC, KAFKA_BROKER)
    data = [message for message in consumer.consume_messages()]
    
    # Process data
    processor = SparkProcessor(SPARK_MASTER)
    processed_data = processor.process_data(data)
    
    # Store data
    writer = HDFSWriter(HDFS_PATH)
    writer.write_to_hdfs(processed_data)

if __name__ == "__main__":
    main()
