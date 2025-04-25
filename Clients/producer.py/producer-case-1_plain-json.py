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

sample_input={
        "field_int":random.randint(1, 1000000), 
        "field_str":"string_"+str(random.randint(1, 1000000)),
        "timestamp":datetime.now().strftime("%H:%M:%S")
        }

if __name__ == '__main__':
    
    topic="test-case-1"
    
    producer = SerializingProducer(conf)
    
    for i in range(1,5):    
        
        key=str(datetime.now().strftime("%H:%M:%S")+"-"+str(i))
        value=sample_input
        value["field_int"]=random.randint(1, 1000000)
        value["field_str"]=str(random.randint(1, 1000000))
        value["timestamp"]=datetime.now().strftime("%H:%M:%S")
        
        producer.produce(topic, key=key, value=value,on_delivery=delivery_report)

    producer.flush()