import os
from dotenv import load_dotenv

load_dotenv()  # Tự động load các biến từ file .env

kafka_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
spark_master_url = os.getenv('SPARK_MASTER_URL')
elastic_host = os.getenv('ELASTICSEARCH_HOST')
elastic_port = os.getenv('ELASTICSEARCH_PORT')
secret_key = os.getenv('SECRET_KEY')

# Sử dụng các biến môi trường này cho cấu hình ứng dụ0n0g của bạn
print("Kafka Servers:", kafka_servers)
print("Spark Master URL:", spark_master_url)
print("Elasticsearch:", elastic_host, elastic_port)

from flask import Flask, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(hosts=["elasticsearch:9200"])

@app.route('/')
def index():
    # Ví dụ: truy vấn Elasticsearch để lấy số liệu tweet trong 1 phút gần nhất
    query = {
        "query": {
            "match_all": {}
        },
        "size": 10
    }
    res = es.search(index="tweets_index", body=query)
    return jsonify(res['hits']['hits'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
