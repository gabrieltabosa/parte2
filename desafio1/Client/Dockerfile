FROM python:3.10-slim

WORKDIR /app
COPY cliente.py .
ENV PYTHONUNBUFFERED=1
RUN pip install requests

CMD ["python", "cliente.py"]