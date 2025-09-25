import json
from kafka import KafkaConsumer


TOPIC_NAME = 'fake_topic'
SERVER_ADDRESS = '127.0.0.1:9092'
CONSUMER_GROUP_ID = 'fake_group'

#defining consumer 
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=SERVER_ADDRESS,
    group_id=CONSUMER_GROUP_ID
)

if __name__ == "__main__":
    """Consume Data from the consumer """

    try:
        for msg in consumer:
            print (json.loads(msg.value))
    except KeyboardInterrupt:
        print("-quit")


