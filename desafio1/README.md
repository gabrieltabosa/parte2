# 🐳 Desafio 1 — Containers em Rede (Docker)

## 🚀 Passo a passo

### 1️⃣ Criar rede Docker
Esse passo é essencial para as duas aplicações se conectrem 

```bash
docker network create minha_rede
```

### 2️⃣ Construir a imagem do servidor

```bash
cd server
docker build -t servidor .
```
### 3️⃣ Executar o servidor Flask

```bash
docker run -d --name servidor_web --network minha_rede -p 8080:8080 servidor
```
neste passo sua aplicação do servidor ja estara rodando, então basta rodar este comando para ver os Logs:
```bash
docker logs -f servidor_web
```

### 4️⃣ Construir a imagem do cliente
