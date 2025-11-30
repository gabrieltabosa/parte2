from flask import Flask, jsonify
import requests

app = Flask(__name__)

SERVICE_A_URL = "http://service_a:5001/users"

@app.route("/info")
def get_info():
    try:
        response = requests.get(SERVICE_A_URL)
        usuarios = response.json()

        info = [
            f"Usuário {u['nome']} ativo desde {u['ativo_desde']}"
            for u in usuarios
        ]

        return jsonify({"informacoes": info})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/health")
def health():
    return jsonify({"status": "ok"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

