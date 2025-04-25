from confluent_kafka import DeserializingConsumer, Consumer, TopicPartition
from confluent_kafka.admin import AdminClient
import socket

kafka_config = {
        'bootstrap.servers': '',
        'security.protocol': '',
        'sasl.mechanism': '',
        'sasl.username': '',
        'sasl.password': '',
        'group.id': f'cg',
        'auto.offset.reset': 'earliest',
        'client.id': socket.gethostname()
    }

# Deserialize consumed kafka records
def json_deserializer(obj,ctx):
    return json.loads(obj.decode('utf-8'))
