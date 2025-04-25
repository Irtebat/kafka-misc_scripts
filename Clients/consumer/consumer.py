from confluent_kafka import KafkaException, KafkaError,DeserializingConsumer, Consumer


from utils import json_deserializer, kafka_config
VERBOSITY=10000

if __name__ == '__main__':
        
    # Consumer instance
    consumer = DeserializingConsumer(kafka_config)

    consumer.subscribe(["business_data"])
    
    # Poll for new messages
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            else:
                print(msg.value())

    except KeyboardInterrupt:
        pass
    
    finally:
        consumer.close()