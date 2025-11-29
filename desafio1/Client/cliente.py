import requests
import time
from datetime import datetime

SERVER_URL = "http://servidor_web:8080"

while True:
    try:
        response = requests.get(SERVER_URL)
        data = response.json()

        print("========== CLIENTE ==========")
        print(f"[CLIENT] Horário local: {datetime.now().strftime('%H:%M:%S')}")
        print(f"[CLIENT] Status......: {data['status']}")
        print(f"[CLIENT] IP Servidor.: {data['server_ip']}")
        print(f"[CLIENT] Host Server.: {data['server_hostname']}")
        print(f"[CLIENT] IP Cliente..: {data['client_ip']}")
        print("=================================\n")

    except Exception as e:
        print("[CLIENT] Erro ao contactar servidor:", e)

    time.sleep(2)