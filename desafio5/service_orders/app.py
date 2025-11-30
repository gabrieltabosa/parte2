from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def get_orders():
    return jsonify([
        {"id": 101, "user_id": 1, "item": "Notebook"},
        {"id": 102, "user_id": 3, "item": "Mouse"},
    ])

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)