import json
import boto3
from kafka import KafkaConsumer
from datetime import datetime
import os


TOPIC_NAME = "marketing"
SERVER_ADDRESS = "127.0.0.1:9092"

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "http://127.0.0.1:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ROOT_USER", "chapolin")
MINIO_SECRET_KEY = os.getenv("MINIO_ROOT_PASSWORD", "mudar@123")
BUCKET_NAME = "bronze" 

s3_client = boto3.client(
    's3',
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY
)


def consume_and_store():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=SERVER_ADDRESS,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="consumer-group-leads",
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        key_deserializer=lambda k: k.decode("utf-8") if k else None
    )

    print(f"Listening for messages on topic `{TOPIC_NAME}`...")

    for message in consumer:
        key = message.key or "nokey"
        value = message.value

        filename = f"{key}_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.json"

        data_json = json.dumps(value)

        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=data_json,
            ContentType='application/json'
        )

        print(f"Saved message to MinIO bucket `{BUCKET_NAME}` as {filename}")

if __name__ == "__main__":
    consume_and_store()
