# **Desafio 5 — Arquitetura de Microsserviços com API Gateway**

Este projeto implementa **três serviços Dockerizados**:

* **Service Users** → fornece dados de usuários
* **Service Orders** → fornece pedidos
* **API Gateway** → único ponto de entrada, repassa chamadas para os serviços internos

A arquitetura segue padrões modernos utilizados em sistemas distribuídos na nuvem.

---

# **Arquitetura**

```
        ┌────────────────┐
        │  Usuário       │
        └───────▲────────┘
                │ HTTP
                ▼
        ┌────────────────┐
        │  API Gateway   │  Porta 5000
        └───────┬────────┘
     /users     │        /orders
       ▼        │          ▼
┌────────────┐  │   ┌────────────┐
│ Service A  │  │   │ Service B  │
│ (Users)    │  │   │ (Orders)   │
│ Porta 5001 │  │   │ Porta 5002 │
└────────────┘  │   └────────────┘
                │
```

### 🔹 **Fluxo**

1. O cliente chama o Gateway
2. O Gateway decide para qual microsserviço enviar a requisição
3. Cada serviço responde e o Gateway retorna para o cliente

---

# **Como Executar**

```
docker compose -f 'desafio5/docker-compose.yml' up -d --build 
```

Aguarde os containers ficarem **healthy**:

```
docker ps
```

---

# 🧪 **Testes**

### Listar usuários

```
http://localhost:5000/users
```

Saída esperada:

```json
[
  {"id": 1, "nome": "Alice", "ativo": true},
  {"id": 2, "nome": "Bob", "ativo": false},
  {"id": 3, "nome": "Carlos", "ativo": true}
]
```

### Listar pedidos

```
http://localhost:5000/orders
```

---

# **Como Parar Tudo**

```
docker compose down
```

