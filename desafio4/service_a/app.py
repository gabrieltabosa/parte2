from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def get_users():
    usuarios = [
        {"id": 1, "nome": "Gabriel", "ativo_desde": "2022"},
        {"id": 2, "nome": "Maria", "ativo_desde": "2021"},
        {"id": 3, "nome": "João", "ativo_desde": "2023"}
    ]
    return jsonify(usuarios)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)