FROM python:3.10-slim

WORKDIR /app
COPY cliente.py .

RUN pip install requests

CMD ["python", "cliente.py"]