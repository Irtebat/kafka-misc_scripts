from confluent_kafka import Producer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from utils import *

import socket
from datetime import datetime
import random
import os 

class Record(object):
    def __init__(self, field_int, field_str, timestamp):
        self.field_int = field_int
        self.field_str = field_str
        self.timestamp = timestamp

with open(f"{os.getcwd()}/record.avsc") as f:
        schema_string = f.read()


def record_to_dict(record, ctx):
    return {"field_int":record.field_int, 
            "field_str":record.field_str,
            "timestamp":record.timestamp}

conf = {'bootstrap.servers': '<bootstrap_server>',
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'PLAIN',
        'sasl.username': '<key>',
        'sasl.password': '<secret>',
        'client.id': socket.gethostname()}

sr_config = {
    'url': '<sr_endpoint>',
    'basic.auth.user.info':'<key:secret>'
}

if __name__ == '__main__':
    
    topic="<topic_name>"
    
    # producer = Producer(conf)
    sr_client = SchemaRegistryClient(sr_config)
    avro_serializer = AvroSerializer(sr_client, schema_string, record_to_dict)
    value=Record(random.randint(1, 1000000), str(random.randint(1, 1000000)), datetime.now().strftime("%H:%M:%S"))
    
    serialized_value=avro_serializer(value,SerializationContext(topic, MessageField.VALUE))
    schema_id=int.from_bytes(serialized_value[1:5], byteorder='big')

    print(schema_id)
    