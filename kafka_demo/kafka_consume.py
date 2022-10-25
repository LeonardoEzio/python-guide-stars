from kafka import KafkaConsumer


if __name__ == "__main__":
    consumer = KafkaConsumer(
        " ",
        #消息主题
        group_id="python_test_01",
        bootstrap_servers=[''],
        auto_offset_reset='earliest' # 默认为latest
    )
    while True:
        for msg in consumer:
            print(msg)

