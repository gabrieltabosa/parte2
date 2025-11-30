from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def get_users():
    return jsonify([
        {"id": 1, "nome": "Alice", "ativo": True},
        {"id": 2, "nome": "Bob", "ativo": False},
        {"id": 3, "nome": "Carlos", "ativo": True},
    ])

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)