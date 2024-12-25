# Base image olarak Python kullan
FROM python:3.9-slim

# Çalışma dizinini oluştur ve ayarla
WORKDIR /app

# Gereksinim dosyasını ekle ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Django projesini konteynere kopyala
COPY . .

# Django komutları çalıştırmak için environment variable ayarları
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Django için gerekli komutları çalıştır
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Sunucuyu başlat
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]