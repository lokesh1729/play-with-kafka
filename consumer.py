from kafka import KafkaConsumer


consumer1 = KafkaConsumer('user-events', group_id="group1", bootstrap_servers='localhost:9092')

consumer2 = KafkaConsumer('user-events', group_id="group1", bootstrap_servers='localhost:9092')

consumer3 = KafkaConsumer('user-events', group_id="group2", bootstrap_servers='localhost:9092')

consumer4 = KafkaConsumer('user-events', group_id="group2", bootstrap_servers='localhost:9092')

while True:
    print("****** consumer1 ********")

    for msg in consumer1:
        print(msg)
    print("****** consumer2 ********")

    for msg in consumer2:
        print(msg)
    print("****** consumer3 ********")

    for msg in consumer3:
        print(msg)
    print("****** consumer4 ********")

    for msg in consumer4:
        print(msg)

