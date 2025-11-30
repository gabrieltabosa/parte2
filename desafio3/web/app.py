from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)


DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "acoesdb")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "senha")


REDIS_HOST = os.getenv("REDIS_HOST", "cache")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))



def conectar_postgres():
    
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def buscar_acoes():
    
    try:
        conn = conectar_postgres()
        cur = conn.cursor()
        cur.execute("SELECT ticker, empresa, preco FROM acoes;")
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return resultado
    except Exception as e:
        return [(f"Erro ao conectar no DB: {e}", "", "")]


def testar_cache():
    
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.set("teste", "ok")
        return r.get("teste").decode("utf-8")
    except Exception as e:
        return f"Erro ao conectar no Redis: {e}"


def formatar_acoes_html(acoes):
    
    return "<br>".join([f"{t[0]} - {t[1]} - R${t[2]}" for t in acoes])



@app.route("/")
def index():
    acoes = buscar_acoes()
    cache_status = testar_cache()
    acoes_html = formatar_acoes_html(acoes)

    return f"""
        <h2>Ações:</h2>
        {acoes_html}
        <br><br>
        <b>Redis:</b> {cache_status}
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

