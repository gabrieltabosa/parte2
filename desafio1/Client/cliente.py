import time
import requests

while True:
    try:
        print("Realizando requisição para o servidor...")
        r = requests.get("http://servidor_web:8080")
        print("Resposta:", r.text)
    except Exception as e:
        print("Erro ao acessar o servidor:", e)
    time.sleep(2)