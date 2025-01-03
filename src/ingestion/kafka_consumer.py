from confluent_kafka import Consumer, KafkaException
import json

# Configurar o consumidor Kafka
consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Endereço do broker Kafka
    'group.id': 'bigdata_group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_config)

# Consumir mensagens
def consume_messages(topic):
    consumer.subscribe([topic])
    print(f"Consuming messages from topic: {topic}")
    try:
        while True:
            msg = consumer.poll(1.0)  # Tempo de espera de 1 segundo
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            message = json.loads(msg.value().decode('utf-8'))
            print(f"Consumed: {message}")
    except KeyboardInterrupt:
        print("Exiting consumer...")
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_messages(topic="bigdata_topic")
