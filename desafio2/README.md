

# 🐳 Desafio 2 — Volumes e Persistência (Docker)

## 📘 Descrição Geral da Solução

Este projeto demonstra como garantir **persistência de dados em containers Docker** utilizando volumes.  
A ideia principal é criar um banco de dados dentro de um container Docker, armazenando os dados em um volume externo, de forma que **os dados sobrevivam mesmo se o container for removido ou recriado**.

A solução consiste em:

- 🗄️ **Banco de Dados (PostgreSQL)** — roda em um container isolado.  
- 📂 **Volume Docker (`desafio2_pgdata`)** — armazena os dados fora do container.  
- 🔄 **Script de inicialização (`init.sql`)** — cria a tabela `usuarios` e insere dados iniciais.  

---

## 🧱 Arquitetura e Decisões Técnicas

### 🔹 Arquitetura

- **Container PostgreSQL (`desafio2_db`)**: responsável por armazenar os dados e responder às consultas.  
- **Volume Docker (`desafio2_pgdata`)**: garante que os dados não sejam perdidos mesmo se o container for removido.  
- **Rede Docker**: garante que containers distintos (se houver cliente adicional) possam se comunicar com o banco via hostname.  

### 🔹 Decisões Técnicas

- **PostgreSQL oficial**: escolha confiável e amplamente usada, com suporte a volumes.  
- **Persistência via volume**: permite que os dados sobrevivam a remoções ou atualizações de container.  
- **Script de inicialização (`init.sql`)**: cria a tabela `usuarios` e popula dados iniciais na primeira execução.  
- **Variáveis de ambiente** no `docker-compose.yml`: definem usuário, senha e banco de forma segura e reproduzível.  
- **Logs e acesso via `docker exec`**: permitem inspeção e depuração do banco de dados.  
- **Isolamento e reprodutibilidade**: cada container é independente e configurado para reconstrução automática via `docker-compose --build`.  

---

## 🔄 Funcionamento Detalhado

1. O `docker-compose.yml` cria o volume `desafio2_pgdata` e inicia o container `desafio2_db`.  
2. Durante a primeira execução, o PostgreSQL executa o script `init.sql` presente na pasta `./desafio2/`, criando a tabela `usuarios` e inserindo registros iniciais.  
3. Todos os dados do banco são armazenados no volume externo (`desafio2_pgdata`).  
4. O container pode ser removido ou recriado sem perda de dados, pois o volume mantém o conteúdo persistente.  

---

## 🚀 Passo a Passo de Execução

### 1️⃣ Subir o container com Docker Compose

Na raiz do projeto (`fccp/parte2/`), execute:

```bash
docker compose -f 'desafio2/docker-compose.yml' up -d --build
````

* Cria o **volume `desafio2_pgdata`** se ainda não existir.
* Inicializa o **container `desafio2_db`**.
* Executa o **script `init.sql`** na primeira execução para criar tabelas e inserir dados iniciais.

### 2️⃣ Acessar o banco

```bash
docker exec -it desafio2_db psql -U admin -d desafio
```

Dentro do console `psql`:

* Listar tabelas:

```
\dt
```

* Consultar dados da tabela `usuarios`:

```sql
SELECT * FROM usuarios;
```

### 3️⃣ Testar persistência

1. Pare e remova o container:

```bash
docker compose down
```

2. Suba o container novamente:

```bash
docker compose up -d
```

3. Repita o comando do passo 2 e vera o banco com os dados salvos:

```bash
docker exec -it desafio2_db psql -U admin -d desafio
```

Dentro do console `psql`:

* Listar tabelas:

```
\dt
```

* Consultar dados da tabela `usuarios`:

```sql
SELECT * FROM usuarios;
```


