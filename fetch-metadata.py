from confluent_kafka.admin import AdminClient
from utils import getAdminConfig

def print_metadata():
    
    admin_client = AdminClient(getAdminConfig())
    try:
        # Request metadata from the broker
        metadata = admin_client.list_topics(timeout=10)
        
        # Print broker details
        print(f"\nCluster Metadata:")
        print(f"  Broker ID: {metadata.orig_broker_id}")
        print(f"  Broker Name: {metadata.orig_broker_name}\n")

        print("Broker Information:")
        for broker in metadata.brokers.values():
            print(f"  Broker ID: {broker.id}")
            print(f"  Host: {broker.host}")
            print(f"  Port: {broker.port}")
            print(f"  Is Controller: {broker.id == metadata.controller_id}\n")

        print("Available Topics:")
        for topic in metadata.topics.values():
            print(f"  Topic: {topic.topic}")
            print(f"    Error: {topic.error if topic.error else 'None'}")

            for partition in topic.partitions.values():
                print(f"    Partition: {partition.id}")
                print(f"      Leader: {partition.leader}")
                print(f"      Replicas: {partition.replicas}")
                print(f"      In-Sync Replicas (ISRs): {partition.isrs}")
                print(f"      Error: {partition.error if partition.error else 'None'}")


    except Exception as e:
        print(f"Failed to fetch metadata: {e}")

if __name__ == "__main__":
    print_metadata()