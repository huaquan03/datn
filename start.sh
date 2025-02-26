# Chạy Kafka stack
cd kafka && docker compose up --build -d

# Chạy Spark cluster
cd ../spark && docker compose up --build -d

# Chạy Jobs (Producer, Spark Streaming & Batch)
cd ../job && docker compose up --build -d

# Chạy Serving layer
cd ../serving && docker compose up --build -d
