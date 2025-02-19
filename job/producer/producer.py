import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Giả sử dữ liệu tweet được lưu trong file JSON có tên tweets.json (đã mount volume)
with open('/data/tweets.json', 'r') as f:
    tweets_list = json.load(f)

batch_size = 500
i = 0
while i < len(tweets_list):
    batch = tweets_list[i: i + batch_size]
    for tweet in batch:
        producer.send('tweets_stream', tweet)
        producer.send('tweets_batch', tweet)
    producer.flush()
    i += batch_size
    time.sleep(1)
