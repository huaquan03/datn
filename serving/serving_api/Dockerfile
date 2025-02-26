# Sử dụng image Python nhẹ
FROM python:3.8-slim

# Đặt thư mục làm việc
WORKDIR /app

# Copy file requirements (nếu có)
# COPY requirements.txt .
# Ví dụ nội dung requirements.txt:
# flask==2.0.3
# elasticsearch==7.17.0
# RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn của API
COPY app.py .

# Expose port cho API (ví dụ 5000)
EXPOSE 5000

# Command chạy ứng dụng
CMD ["python", "app.py"]
