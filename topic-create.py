from confluent_kafka.admin import AdminClient, NewTopic, KafkaException
from utils import getAdminConfig

# List of topics to delete
TOPICS = [
    {'name': 'poc-syslog', 'num_partitions': 1, 'retention_ms': -1}
]   

def create_topics(topics):

    admin_client = AdminClient(getAdminConfig())

    # Create a list of NewTopic objects
    new_topics = [NewTopic(topic['name'], topic['num_partitions'], config={'retention.ms': topic['retention_ms']}) for topic in topics]

    # Call create_topics to create topics on the broker
    fs = admin_client.create_topics(new_topics, operation_timeout=30)

    # Wait for each operation to finish
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print(f"Topic {topic} created")
        except KafkaException as e:
            print(f"Failed to create topic {topic}: {e}")
        except Exception as e:
            print(f"Unexpected error creating topic {topic}: {e}")

if __name__ == "__main__":
    create_topics(TOPICS)