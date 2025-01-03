from src.ingestion.kafka_consumer import KafkaConsumerWrapper

def test_consume_messages():
    consumer = KafkaConsumerWrapper("test_topic", "localhost:9092")
    messages = consumer.consume_messages()
    assert messages is not None
