from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

USERS_URL = os.getenv("USERS_URL", "http://service_users:5001/users")
ORDERS_URL = os.getenv("ORDERS_URL", "http://service_orders:5002/orders")

@app.route("/users")
def proxy_users():
    try:
        r = requests.get(USERS_URL)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"erro": "Falha ao consultar usuários", "detalhe": str(e)}), 500

@app.route("/orders")
def proxy_orders():
    try:
        r = requests.get(ORDERS_URL)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"erro": "Falha ao consultar pedidos", "detalhe": str(e)}), 500

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)