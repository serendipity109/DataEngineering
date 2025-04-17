import kafka
import time
import random
import json
import numpy as np
from time import sleep

#define producer and consumer variable
sensor_data = {'longitude': 0, 'lattitude': 0}
topic_name = "vehicle-coordinates"
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
        longitude = np.random.randint(-180, 81)
        latitude = np.random.randint(-90, 91)
        
        print(f"longitude: {longitude} latitude: {latitude}")
        sensor_data['longitude'] = longitude
        sensor_data['latitude'] = latitude
        producer.send(topic_name, value=sensor_data)
        sleep(3)

except KeyboardInterrupt:
    pass