import json
import random

from kafka import KafkaProducer
from faker import Faker

obj = Faker()

producer = KafkaProducer(bootstrap_servers='localhost:9092', key_serializer=str.encode, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

usernames= [obj.user_name() for _ in range(10)]

data = [{"username": usernames[random.randint(0, 9)], "address": obj.address()} for _ in range(100)]

for each_data in data:
    print("sending message %s" % each_data)
    producer.send('user-events', key=each_data["username"], value=each_data)

