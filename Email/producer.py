from kafka import KafkaProducer
import pandas as pd
import json

KAFKA_TOPIC = "email_topic"
KAFKA_SERVER = "localhost:9092"

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

# Function to write email to Excel
def save_email_to_excel(email):
    file_name = "emails.xlsx"

    try:
        df = pd.read_excel(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Email"])

    new_data = pd.DataFrame({"Email": [email]})
    df = pd.concat([df, new_data], ignore_index=True)

    df.to_excel(file_name, index=False)
    print(f"Email saved to {file_name}")

# Take email as input
email = input("Enter email: ")
save_email_to_excel(email)

# Send email to Kafka
producer.send(KAFKA_TOPIC, {"email": email})
producer.flush()
print(f"Sent {email} to Kafka topic {KAFKA_TOPIC}")
