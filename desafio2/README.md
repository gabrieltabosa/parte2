

# 🐳 Desafio 2 — Volumes e Persistência (Docker)

## Arquitetura e Decisões Técnicas

### 🔹 Arquitetura

- **Container PostgreSQL (`desafio2_db`)**: responsável por armazenar os dados e responder às consultas.  
- **Volume Docker (`desafio2_pgdata`)**: garante que os dados não sejam perdidos mesmo se o container for removido. 

### 🔹 Decisões Técnicas

- **PostgreSQL oficial**: escolha confiável e amplamente usada, com suporte a volumes.  
- **Persistência via volume**: permite que os dados sobrevivam a remoções ou atualizações de container.  
- **Script de inicialização (`init.sql`)**: cria a tabela `usuarios` e popula dados iniciais na primeira execução.  
- **Variáveis de ambiente** no `docker-compose.yml`: definem usuário, senha e banco de forma segura e reproduzível.  
- **Logs e acesso via `docker exec`**: permitem inspeção e depuração do banco de dados.  

---

## Funcionamento Detalhado

1. O `docker-compose.yml` cria o volume `desafio2_pgdata` e inicia o container `desafio2_db`.  
2. Durante a primeira execução, o PostgreSQL executa o script `init.sql` presente na pasta `./desafio2/`, criando a tabela `usuarios` e inserindo registros iniciais.  
3. Todos os dados do banco são armazenados no volume externo (`desafio2_pgdata`).  
4. O container pode ser removido ou recriado sem perda de dados, pois o volume mantém o conteúdo persistente.  

---

## Passo a Passo de Execução

### 1️ Subir o container com Docker Compose

Na raiz do projeto (`fccp/parte2/`), execute:

```bash
docker compose -f 'desafio2/docker-compose.yml' up -d --build
````

* Cria o **volume `desafio2_pgdata`** se ainda não existir.
* Inicializa o **container `desafio2_db`**.
* Executa o **script `init.sql`** na primeira execução para criar tabelas e inserir dados iniciais.

### 2️ Acessar o banco

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

### 3️ Testar persistência

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


