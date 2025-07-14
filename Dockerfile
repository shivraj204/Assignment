# Use official Python image
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/wait-for-it.sh", "db:5432", "--", "sh", "-c", "python manage.py migrate && python manage.py createsuperuser --noinput || true && python manage.py runserver 0.0.0.0:8000"]
