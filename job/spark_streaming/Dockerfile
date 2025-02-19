# Sử dụng image Spark từ Bitnami (đã được cài sẵn Spark)
FROM bitnami/spark:latest

# Đặt thư mục làm việc
WORKDIR /app

# Copy file mã nguồn của Spark Streaming job
COPY streaming_job.py .

# Command để chạy Spark Streaming job
CMD ["/opt/bitnami/spark/bin/spark-submit", "--master", "spark://spark-master:7077", "streaming_job.py"]
