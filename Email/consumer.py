from kafka import KafkaConsumer
import json

KAFKA_TOPIC = "email_topic"
KAFKA_SERVER = "localhost:9092"

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

print(f"Listening for messages on topic {KAFKA_TOPIC}...\n")

for message in consumer:
    email_data = message.value
    print(f"Received Email: {email_data['email']}")
