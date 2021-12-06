from kafka import KafkaConsumer


consumer1 = KafkaConsumer('user-events', group_id="group1", bootstrap_servers='localhost:9092')

for msg in consumer1:
    print(msg)

