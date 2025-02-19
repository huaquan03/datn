from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TweetBatchProcessing").getOrCreate()

# Giả sử dữ liệu đã được ghi ra từ Kafka topic "tweets_batch" và lưu vào file hệ thống (hoặc bạn có thể đọc trực tiếp từ Kafka)
# Ví dụ: đọc dữ liệu đã lưu trữ ở định dạng JSON trên HDFS hoặc volume local đã được mount
df = spark.read.json("/data/tweets_batch/")

# Thực hiện tiền xử lý, ví dụ loại bỏ tweet trùng lặp, làm sạch văn bản, v.v.
processed_df = df.filter("text is not null")

# Lưu kết quả dưới dạng Parquet (Batch View)
processed_df.write.mode("overwrite").parquet("/data/processed_tweets/")

spark.stop()
