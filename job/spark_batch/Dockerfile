# Sử dụng image Spark từ Bitnami
FROM bitnami/spark:latest

# Đặt thư mục làm việc
WORKDIR /app

# Copy file mã nguồn của Spark Batch job
COPY batch_job.py .

# Command để chạy Spark Batch job
CMD ["/opt/bitnami/spark/bin/spark-submit", "--master", "spark://spark-master:7077", "batch_job.py"]
