FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY ingest_data.py /app/ingest_data.py

RUN mkdir data \
    && apt-get update && apt-get install -y \
    wget \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "/app/ingest_data.py"]