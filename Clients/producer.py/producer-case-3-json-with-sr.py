from confluent_kafka import Producer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from utils import *

import socket
from datetime import datetime
import random

class Record(object):
    def __init__(self, field_int, field_str, timestamp):
        self.field_int = field_int
        self.field_str = field_str
        self.timestamp = timestamp

schema_string = """{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "SampleRecord",
    "description": "Sample.Record",
    "type": "object",
    "properties": {
      "field_int": {
        "description": "Integer field",
        "type": "integer"
      },
      "field_str": {
        "description": "String Field",
        "type": "string"
      },
      "timestamp": {
        "description": "Timestamp; String Field",
        "type": "string"
      }
    }
  }"""

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
    
    topic="test-case-3"
    
    producer = Producer(conf)
    sr_client = SchemaRegistryClient(sr_config)
    json_serializer = JSONSerializer(schema_string,
                                     sr_client,
                                     record_to_dict)
    
    for i in range(1,5):    

        key=str(datetime.now().strftime("%H:%M:%S")+"-"+str(i))
        value=Record(random.randint(1, 1000000), str(random.randint(1, 1000000)), datetime.now().strftime("%H:%M:%S"))
        producer.produce(topic, key=key, value=json_serializer(value, SerializationContext(topic, MessageField.VALUE)),on_delivery=delivery_report)

    producer.flush()