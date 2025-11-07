# ใช้ base image ของ Python
FROM python:3.10-slim

# [แก้ไข] เปลี่ยน Workdir เป็น /code เพื่อความชัดเจน
WORKDIR /code

# คัดลอก requirements.txt (ไฟล์นี้อยู่ในระดับเดียวกับ Dockerfile)
COPY requirements.txt .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# [!!! นี่คือจุดที่แก้ไขหลัก !!!]
# คัดลอกโฟลเดอร์ "app" ทั้งหมดในเครื่อง
# ไปไว้ใน container ในชื่อ "app"
# (จะกลายเป็น /code/app)
COPY ./app /code/app

# [!!! นี่คือจุดที่แก้ไขหลัก !!!]
# สั่ง Uvicorn ให้รัน "app.main:app" (โมดูล 'main' ในแพ็คเกจ 'app')
# ไม่ใช่แค่ "main:app"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]