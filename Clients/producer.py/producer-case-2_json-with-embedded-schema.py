from confluent_kafka import SerializingProducer
from utils import *

import socket
from datetime import datetime
import random



conf = {'bootstrap.servers': '',
        'security.protocol': '',
        'sasl.mechanism': '',
        'sasl.username': '',
        'sasl.password': '',
        'value.serializer': json_serializer,
        'client.id': socket.gethostname()}

conf = {'bootstrap.servers': '<bootstrap_server>',
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'PLAIN',
        'sasl.username': '<key>',
        'sasl.password': '<secret>',
        'value.serializer': json_serializer,
        'client.id': socket.gethostname()
        }


sample_input={
        "schema": {
            "type": "struct",
            "fields": [
            {
                "type": "int64",
                "optional": False,
                "field": "field_int"
            },
            {
                "type": "string",
                "optional": False,
                "field": "field_str"
            },
            {
                "type": "string",
                "optional": False,
                "field": "timestamp"
            },
            ],
            "optional": False,
            "name": "test.object"
        },
        "payload":{
            "field_int":random.randint(1, 10000), 
            "field_str":"string_"+str(random.randint(1, 10000)),
            "timestamp":datetime.now().strftime("%H:%M:%S")
        }
    }

if __name__ == '__main__':
    
    topic="test-topic"
    
    producer = SerializingProducer(conf)
    
    for i in range(1,5):    
        
        key=str(datetime.now().strftime("%H:%M:%S")+"-"+str(i))
        value=sample_input
        value["payload"]["field_int"]=random.randint(1, 1000000)
        value["payload"]["field_str"]=str(random.randint(1, 1000000))
        value["payload"]["timestamp"]=datetime.now().strftime("%H:%M:%S")
        
        producer.produce(topic, key=key, value=value,on_delivery=delivery_report)

    producer.flush()