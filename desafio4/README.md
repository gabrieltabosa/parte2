# 🧩 **Desafio 4 — Microsserviços Independentes**

Este projeto implementa **dois microsserviços totalmente independentes**, que se comunicam entre si via **HTTP**, utilizando Docker e uma arquitetura simples, porém profissional.

---

# 📌 **Descrição Geral**

O objetivo do desafio é criar:

* **Microsserviço A** → fornece uma lista de usuários em formato JSON.
* **Microsserviço B** → consome o serviço A e exibe os dados combinados (por exemplo: cálculo de quanto tempo o usuário está ativo).
* Comunicação entre serviços feita via **HTTP interno** (sem API Gateway).
* Cada microsserviço possui **seu próprio Dockerfile**, garantindo isolamento total.

---

# 🏗️ **Arquitetura do Projeto**

A arquitetura segue o princípio de microsserviços independentes:

```
┌─────────────────────────────────────────────────────────┐
│                    Docker Network (backend)             │
│                                                         │
│    ┌───────────────────────┐        HTTP GET            │
│    │    Service A          │ <----------------------┐   │
│    │  (Fornece usuários)   │                        │   │
│    └───────────────────────┘                        │   │
│                                                     │   │
│    ┌───────────────────────┐        Resposta JSON   │   │
│    │    Service B          │ -----------------------┘   │
│    │ (Combina informações) │                            │
│    └───────────────────────┘                            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### ✔ O Service A expõe:

```
GET /users
GET /health
```

### ✔ O Service B expõe:

```
GET /info
GET /health
```

---

# 🔧 **Decisões Técnicas**

### 🔹 Microsserviços totalmente separados

Cada microsserviço (A e B) possui:

* sua própria pasta
* seu próprio código Flask
* seu próprio Dockerfile

➡ Isso garante independência total entre eles, como acontece em sistemas distribuídos reais.

---

### 🔹 Comunicação via HTTP

O **Service B** envia requisições HTTP diretamente para o **Service A**:

```
Service B → GET http://service_a:5001/users
```

➡ Essa forma de comunicação é exatamente a usada entre microsserviços em nuvem.

---

### 🔹 Healthchecks no Docker Compose

Ambos os serviços possuem healthchecks:

```
/health → retorna OK
```

O Compose verifica se cada serviço está saudável antes de considerá-lo “pronto”.

➡ Isso evita que o Service B tente chamar o A antes dele estar funcionando.

---

### 🔹 depends_on com condição de saúde

O Service B só inicia após o Service A responder “OK” no healthcheck:

```yaml
depends_on:
  service_a:
    condition: service_healthy
```

➡ Garante ordem de inicialização e evita erros de conexão na subida do ambiente.

---

### 🔹 Rede interna Docker (bridge)

Os dois serviços estão automaticamente na mesma rede interna criada pelo Docker.

➡ Isso permite comunicação via nome do container (`service_a`) sem expor portas extras.


---

# 📂 **Estrutura do Projeto**

```
desafio4/
│
├── service_a/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── service_b/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── docker-compose.yml
```

---

# ▶️ **Como Executar o Projeto**

### 1️⃣ Subir todos os serviços

```
docker compose -f 'desafio4/docker-compose.yml' up -d --build 
```

O Compose irá:

* Criar a rede interna
* Buildar os dois serviços
* Verificar se o Service A está saudável
* Iniciar o Service B apenas após o A estar pronto

---

# 🧪 **Como Testar**

### 📌 Verificar se os serviços estão rodando:

```
docker ps
```

---

## 🚀 **Testar Service A**

### Lista de usuários:

```
http://localhost:5001/users
```

### Healthcheck:

```
http://localhost:5001/health
```

---

## 🚀 **Testar Service B**

### JSON com descrição formatada:

```
http://localhost:5002/info
```
### Healthcheck:

```
http://localhost:5002/health
```
---

# 🧹 **Como Parar Tudo**

```
docker compose down
```




