# 📘 **Desafio 3 — Orquestração com Docker Compose**

Este projeto implementa uma arquitetura de microsserviços composta por três serviços principais:

* **Web (Flask/Python)**
* **Banco de Dados (PostgreSQL)**
* **Cache (Redis)**

Todos são orquestrados via **Docker Compose**, utilizando redes internas, variáveis de ambiente, dependências (`depends_on`) e inicialização automatizada do banco via script SQL.

---

# **📁 Estrutura do Projeto**

```
desafio3-docker/
│
├── web/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── db/
│   └── init.sql
│
│
├── docker-compose.yml
└── README.md
```

---

# **Objetivo do Projeto**

Demonstrar o uso do **Docker Compose** para orquestrar vários serviços dependentes, garantindo:

* Comunicação interna entre containers
* Organização modular de responsabilidades
* Automação da criação e povoamento do banco de dados
* Execução simples e reproduzível

---

# **Arquitetura da Solução**

A aplicação é composta por:

---

## **1. Serviço Web (Flask + Python)**

Localizado na pasta `web/`.

### Funções:

* Conectar ao PostgreSQL e listar informações de ações brasileiras.
* Testar comunicação com o Redis.
* Expor a aplicação na porta **5000**.

### Tecnologias:

* Python 3.11
* Flask
* Psycopg2
* Redis-Py

---

##  **2. Banco de Dados (PostgreSQL)**

Localizado em `db/`.

### Características:

* Utiliza a imagem oficial `postgres:15`.
* Executa automaticamente o script `init.sql` na primeira execução.
* Cria o banco **acoesdb**.
* Cria a tabela `acoes` e preenche com ações brasileiras:

| Ticker | Empresa              | Preço (R$) |
| ------ | -------------------- | ---------- |
| VALE3  | Vale S.A.            | 85.50      |
| KLBN11 | Klabin S.A.          | 32.10      |
| BBAS3  | Banco do Brasil S.A. | 42.75      |

---

## **3. Cache (Redis)**

* Usa imagem oficial `redis:7`
* Testa comunicação através de um simples `set`/`get`
* Disponível internamente via hostname `cache`

---

# **Rede Interna**

O Docker Compose cria automaticamente a rede `backend`, onde:

| Serviço | Hostname |
| ------- | -------- |
| web     | web      |
| db      | db       |
| cache   | cache    |

A comunicação entre containers usa esses nomes — por exemplo:

```
host="db"
port=5432
```

---

# **Decisões Técnicas**

### **1. Separação das tecnologias em pastas diferentes**

**O que é:** Cada serviço (web, banco de dados, cache) tem sua própria pasta com seus arquivos.

**Propósito:**
Isso deixa tudo organizado. Assim, quem abrir o projeto consegue entender rapidamente “onde fica o quê”, sem misturar código Python com arquivos do banco ou configurações do Redis.
É como separar gavetas diferentes para roupas, documentos e ferramentas — tudo fica mais fácil de achar e manter.

---

### **2. Banco criado e preenchido automaticamente por um script SQL**

**O que é:** O container do banco roda automaticamente um arquivo `init.sql` que cria tabelas e insere ações como Vale, Klabin e Banco do Brasil.

**Propósito:**
O projeto funciona do zero, sem você precisar criar nada manualmente.
Isso garante que:

* todos os ambientes (local, professor, colegas) começam com os mesmos dados
* evita erros e configurações manuais
* simplifica testes e demonstração

---

### **3. Variáveis de ambiente configuradas no docker-compose**

**O que é:** Usuário, senha e nomes do banco são passados por variáveis.

**Propósito:**
Assim, você pode mudar credenciais e configurações **sem editar código**, apenas alterando o compose.
Isso melhora:

* segurança (nada hardcoded no código)
* flexibilidade
* facilidade de manutenção

---

### **4. Uso do `depends_on` para iniciar os serviços na ordem correta**

**O que é:** Informa ao Docker que o serviço web só deve iniciar depois do banco e do Redis.

**Propósito:**
Evita que o web tente conectar no banco **antes dele existir**, o que causaria erros.
É como garantir que a tomada está ligada **antes** de ligar o notebook.

---

### **5. Rede interna do tipo *bridge* para comunicação entre containers**

**O que é:** Os containers conversam entre si por uma rede interna criada pelo Compose.

**Propósito:**
Mantém a comunicação dos serviços:

* **segura** (não expõe portas desnecessárias para fora)
* **simples** (os serviços se comunicam apenas pelo nome: `db`, `cache`, `web`)
* **isolada** (só os containers podem acessar)

É como ter uma “rede privada” onde só os serviços do projeto podem conversar.

---

### **6. Volumes persistentes para o banco**

**O que é:** Uma área do disco fica reservada para armazenar os dados do banco.

**Propósito:**
Sem volumes, toda vez que o container fosse reiniciado, o banco voltaria zerado.
Com o volume:

* os dados **não são perdidos**
* o banco continua igual mesmo após reiniciar os containers
* você pode atualizar imagens sem apagar as informações

É como usar um HD externo para garantir que seus arquivos não sumam quando o computador desliga.

---

# 🎯 Resultado final

Essas decisões criam uma arquitetura:

* organizada
* segura
* fácil de entender
* simples de rodar
* consistente em qualquer ambiente


---

# **Como Executar o Projeto**

## **1 Subir os containers**

Na raiz do projeto:

```bash
docker compose -f 'desafio3/docker-compose.yml' up -d --build 
```

Os serviços serão inicializados na ordem:

1. PostgreSQL
2. Redis
3. Web (Flask)

---

## **2 Acessar a aplicação**

Abra no navegador:

```
http://localhost:5000
```

Você verá:

```
Ações:
VALE3 - Vale S.A. - R$85.50
KLBN11 - Klabin S.A. - R$32.10
BBAS3 - Banco do Brasil S.A. - R$42.75

Redis: ok
```

---

# 🧪 **Testando Comunicação Entre os Serviços**

### **1. Web ↔ DB (PostgreSQL)**

A página principal lista as ações do banco.
Se os dados aparecem → comunicação OK.

### **2. Web ↔ Cache (Redis)**

A página principal mostra:

```
Redis: ok
```

Isso significa que `SET` e `GET` funcionaram.

---

# **Parar e Remover Containers**

Para parar:

```bash
docker-compose down
```

Para parar **e remover volume do banco**:

```bash
docker-compose down -v
```
