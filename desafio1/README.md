# 🐳 Desafio 1 — Containers em Rede (Docker)

## 📘 Descrição Geral da Solução

Este projeto implementa uma arquitetura simples com **dois microsserviços** executando em containers Docker distintos e comunicando-se por meio de uma **rede Docker customizada**. O objetivo é demonstrar como aplicações isoladas podem interagir entre si, através da requisição HTTP.

A solução é composta por:

* 🖥️ **Servidor Web (Flask)** — expõe uma rota HTTP retornando mensagens para o cliente.
* 💻 **Cliente (Python)** — conecta-se ao servidor via rede Docker e exibe a resposta.
* 🌐 **Rede Docker** — garante a comunicação direta entre os containers.

## 🧱 Arquitetura e Decisões Técnicas

### 🔹 Componentes

* **Microsserviço Servidor:** roda Flask e responde na porta `8080`.
* **Microsserviço Cliente:** envia requisições HTTP para `servidor_web:8080`.
* **Rede Docker personalizada (`minha_rede`)** para garantir que os containers se enxerguem pelo nome, atraves de um servidor DNS.

### 🔹 Decisões Técnicas

* Uso de `docker build` para gerar imagens isoladas e reproduzíveis.
* Nome dos containers fixo (`servidor_web` e `cliente`) para comunicação simples.
* O cliente só funciona quando a rede Docker existe e o servidor está ativo.
* Logs são acessados pelo Docker, permitindo depuração fácil.

### 🔹 Fluxo de Funcionamento

1. O servidor Flask inicia e fica ouvindo na porta 8080.
2. O container do cliente sobe e tenta acessar a URL `http://servidor_web:8080`.
3. A rede Docker resolve o hostname para o container do servidor.
4. O cliente recebe a resposta que esta no formato JSON e exibe no console.
5. Os logs podem ser acompanhados usando `docker logs`.

---

## 🚀 Passo a passo

### 1️⃣ Iniciando o Ambiente de Desenvolvimento (Desafio 1)
O comando abaixo é utilizado para construir as imagens Docker necessárias e iniciar os contêineres do servidor, cliente e da rede Docker do Desafio 1. A execução ocorre em segundo plano (modo detached), permitindo que você continue usando o terminal enquanto os serviços rodam.

```bash
docker compose -f 'desafio1/docker-compose.yml' up -d --build 
```
#### Detalhamento do Comando

🧩 **docker compose**  
Invoca o mecanismo de orquestração do Docker para subir múltiplos serviços ao mesmo tempo — como servidor web, cliente e redes internas — a partir de um arquivo YAML.

📂 **-f 'desafio1/docker-compose.yml'**  
Especifica qual arquivo `docker-compose.yml` deve ser usado.

Isso é útil quando você está na raiz do projeto, mas o compose do Desafio 1 está em um subdiretório:

/fccp/parte2/desafio1/docker-compose.yml

Assim, você pode rodar tudo a partir de:


Sem precisar entrar na pasta `desafio1/`.

🚀 **up**  
Cria e inicia todos os serviços descritos no compose, incluindo:

- containers (servidor e cliente)  
- rede declarada  
- dependências (`depends_on`)  
- regras de build  
- volumes (se houver)

Se um container já existir, ele é iniciado novamente.

🌙 **-d (detached mode)**  
Executa os containers em segundo plano.

Isso evita que o terminal seja ocupado mostrando logs contínuos.  
Você continua livre para rodar comandos como:


🔨 **--build**  
Força a reconstrução das imagens antes de subir os containers.

Isso garante que:

- alterações no código Python,  
- mudanças no Dockerfile,  
- modificações em dependências,

sejam aplicadas imediatamente.

Sem esse flag, o Docker pode usar imagens antigas do cache.

---

📌 **Resumo Geral**

Esse comando:

- Reconstrói as imagens do servidor e do cliente,  
- Recria a rede do Desafio 1,  
- Inicia os containers em modo background,  
- Garante que tudo esteja atualizado e isolado corretamente.  

É o comando principal que você usará para subir o ambiente completo do **Desafio 1**.




### 2️⃣ Construir a imagem do servidor

```bash
docker compose -f 'desafio1/docker-compose.yml' up -d --build 
```

---

### 3️⃣ Executar o servidor Flask

```bash
docker run -d --name servidor_web --network minha_rede -p 8080:8080 servidor
```

📌 Para ver os logs do servidor:

```bash
docker logs -f servidor_web
```

---

### 4️⃣ Construir a imagem do cliente

```bash
cd ../cliente
docker build -t cliente .
```

---

### 5️⃣ Executar o cliente

```bash
docker run -d --name cliente --network minha_rede cliente
```

📌 Para ver os logs do cliente:

```bash
docker logs -f cliente
```

📌 Caso queira ver detalhes completos:

```bash
docker logs --details -f cliente
```

---

## 🧪 Testando a Comunicação

1. Confirme se ambos containers estão rodando:

```bash
docker ps
```

2. Veja se o cliente está recebendo a resposta do servidor através dos logs.
3. Acesse no navegador (opcional):

```
http://localhost:8080
```

---

## 📡 Fluxo Final

```
CLIENTE  --->  REDE DOCKER  --->  SERVIDOR FLASK
   ↑                                  |
   └────────────── Logs via Docker ◄──┘
```

---

## ✅ Conclusão

Esta solução demonstra como criar microsserviços independentes que se comunicam em uma rede Docker isolada. É um exemplo ideal para aprender conceitos fundamentais de **containers, redes Docker e comunicação entre serviços**.
