from confluent_kafka import Producer
import json
import time
import random

# Configurar o produtor Kafka
producer_config = {
    'bootstrap.servers': 'localhost:9092'  # Endereço do broker Kafka
}
producer = Producer(producer_config)

# Função de callback para entrega
def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record successfully produced to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

# Produzir mensagens
def produce_messages(topic):
    print(f"Producing messages to topic: {topic}")
    while True:
        message = {"key": random.randint(1, 100), "value": random.random()}
        producer.produce(
            topic=topic,
            key=str(message["key"]),
            value=json.dumps(message),
            callback=delivery_report
        )
        producer.flush()  # Garante que as mensagens sejam enviadas
        time.sleep(1)  # Intervalo de 1 segundo entre mensagens

if __name__ == "__main__":
    produce_messages(topic="bigdata_topic")
