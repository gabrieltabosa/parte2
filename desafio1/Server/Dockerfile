FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 8080
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]