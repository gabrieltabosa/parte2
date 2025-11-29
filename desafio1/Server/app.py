from flask import Flask, jsonify, request
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def status():
    hostname = socket.gethostname()
    server_ip = socket.gethostbyname(hostname)

    client_ip = request.remote_addr
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[SERVER] Requisição recebida de {client_ip} às {timestamp}")

    return jsonify({
        "status": "ok",
        "server_hostname": hostname,
        "server_ip": server_ip,
        "client_ip": client_ip,
        "timestamp": timestamp
    })
    
app.run(host="0.0.0.0", port=8080)