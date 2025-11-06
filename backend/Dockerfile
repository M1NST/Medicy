# ใช้ base image ของ Python
FROM python:3.10-slim

# กำหนดโฟลเดอร์ทำงานภายใน container
WORKDIR /app

# คัดลอก requirements.txt ก่อน
COPY app/requirements.txt .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดในโฟลเดอร์ app
COPY app/ .

# รัน FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
