from confluent_kafka.admin import AdminClient, NewTopic, KafkaException
from utils import getAdminConfig

# List of topics to delete
TOPICS = []

def delete_topics(topics=None):
    

    admin_client = AdminClient(getAdminConfig())

    if topics is None:
        # Fetch all topics
        topics = list(admin_client.list_topics().topics.keys())

    # Delete the topics
    fs = admin_client.delete_topics(topics, operation_timeout=30)

    # Wait for each operation to finish
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print(f"Topic {topic} deleted")
        except KafkaException as e:
            print(f"Failed to delete topic {topic}: {e}")
        except Exception as e:
            print(f"Unexpected error deleting topic {topic}: {e}")

if __name__ == "__main__":
    delete_topics()