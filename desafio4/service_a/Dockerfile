FROM python:3.10-slim

WORKDIR /app

# Necessário para o healthcheck funcionar
RUN apt-get update && apt-get install -y curl && apt-get clean

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]