FROM python:3.11-slim

WORKDIR /app

COPY app.py /app/

RUN pip install --no-cache-dir flask

# folder for SQLite DB
RUN mkdir -p /data

EXPOSE 5000

CMD ["python", "app.py"]
