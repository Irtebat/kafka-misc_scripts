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

with open(f"{os.getcwd()}/Clients/record.avsc") as f:
        schema_string = f.read()


def record_to_dict(record, ctx):
    return {"field_int":record.field_int, 
            "field_str":record.field_str,
            "timestamp":record.timestamp}

conf = {'bootstrap.servers': '',
        'security.protocol': '',
        'sasl.mechanism': '',
        'sasl.username': '',
        'sasl.password': '',
        'client.id': socket.gethostname()}

sr_config = {
    'url': '',
    'basic.auth.user.info':''
}

if __name__ == '__main__':
    
    topic="test-case-4"
    
    producer = Producer(conf)
    sr_client = SchemaRegistryClient(sr_config)
    avro_serializer = AvroSerializer(sr_client, schema_string, record_to_dict)
    
    for i in range(1,5):    

        key=str(datetime.now().strftime("%H:%M:%S")+"-"+str(i))
        value=Record(random.randint(1, 1000000), str(random.randint(1, 1000000)), datetime.now().strftime("%H:%M:%S"))
        print(key,value)
        producer.produce(topic=topic,key=key,value=avro_serializer(value, SerializationContext(topic, MessageField.VALUE)),
                             on_delivery=delivery_report)
    producer.flush()