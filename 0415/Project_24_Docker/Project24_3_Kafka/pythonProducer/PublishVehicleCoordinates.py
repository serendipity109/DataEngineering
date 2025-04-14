import kafka
import time
import random
import json
from time import sleep

#define producer and consumer variable
sensor_data = {'longitude': 0, 'latitude': 0}
topic_name = ????
client = kafka.KafkaClient(bootstrap_servers=['localhost:9092'])
producer = kafka.KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))
consumer = kafka.KafkaConsumer(bootstrap_servers=['localhost:9092'])

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))
try:
   
    if topic_name in consumer.topics():
         print(topic_name+" exist")
    else:
        client.ensure_topic_exists(topic_name)

    consumer.close()
    client.close()

    while True:
        longitude = ????
        latitude = ????
        
        print(f"longitude: {longitude} latitude: {latitude}")
        sensor_data['longitude'] = ????
        sensor_data['latitude'] = ????
        producer.send(topic_name, value=????)
        sleep(3)

except KeyboardInterrupt:
    pass
