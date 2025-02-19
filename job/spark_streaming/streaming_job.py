from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

spark = SparkSession.builder.appName("TweetStreamingProcessing").getOrCreate()

# Định nghĩa schema của tweet
schema = StructType([
    StructField("id", StringType(), True),
    StructField("text", StringType(), True),
    StructField("created_at", TimestampType(), True)
    # Thêm các trường khác nếu cần
])

# Đọc dữ liệu từ Kafka topic "tweets_stream"
df_stream = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "tweets_stream") \
    .load()

df_parsed = df_stream.selectExpr("CAST(value AS STRING) as json_str") \
    .select(from_json(col("json_str"), schema).alias("data")).select("data.*")

# Ví dụ: Tính số lượng tweet theo cửa sổ 1 phút
agg_df = df_parsed.groupBy(window(col("created_at"), "1 minute")).count()

# Ghi kết quả ra console (hoặc có thể ghi ra Elasticsearch, Redis, v.v.)
query = agg_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
