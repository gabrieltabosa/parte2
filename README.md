# 📘 **Resumo Geral do Projeto — FCCPD (Fundamentos da Computação Concorrente, Paralela e Distribuída)**

Este repositório reúne **cinco desafios práticos** desenvolvidos como parte da disciplina **FCCPD — Fundamentos da Computação Concorrente, Paralela e Distribuída**.
O propósito central desses desafios é permitir que o aluno **compreenda, implemente e experimente na prática conceitos fundamentais de sistemas concorrentes, paralelos e distribuídos**, utilizando **Docker, redes, microsserviços e comunicação entre processos**.

Cada desafio aborda um aspecto essencial da computação moderna — desde containers isolados e redes virtuais até orquestração de serviços e arquitetura distribuída com API Gateway.

---

# 🎯 **Objetivo Geral da Prática**

Os cinco desafios têm como propósito:

### ✔ **Desenvolver competências práticas em ambientes concorrentes e distribuídos.**

O aluno interage com processos isolados, comunicação entre serviços, dependências e fluxos de dados distribuídos.

### ✔ **Ensinar o uso de Docker como ferramenta de isolamento e empacotamento.**

Containers simulam ambientes independentes, permitindo reproduzir cenários reais de produção.

### ✔ **Introduzir redes virtuais, persistência, orquestração e comunicação entre serviços.**

Cada desafio aumenta o nível de complexidade, preparando o aluno para arquiteturas distribuídas reais.

### ✔ **Praticar arquitetura de microsserviços e API Gateway.**

O aluno implementa serviços independentes, comunicação por HTTP e roteamento por um gateway central.

### ✔ **Desenvolver autonomia, boas práticas e clareza na documentação.**

Cada entrega deve conter um README completo, explicando decisões, arquitetura e execução — garantindo domínio sobre o tema.

---

# 🗂️ **Resumo dos 5 Desafios**

### 🟦 **Desafio 1 — Containers em Rede**

Aprender a criar e conectar containers em uma **rede Docker personalizada**, permitindo que um container servidor e um cliente troquem mensagens via HTTP.

Foco:

* Criação de redes Docker
* Comunicação entre containers
* Logs e interação entre serviços

---

### 🟩 **Desafio 2 — Volumes e Persistência**

Demonstrar como **dados podem sobreviver à recriação de containers**, utilizando volumes Docker.

Foco:

* Persistência real de dados
* Montagem de volumes
* Banco de dados simples (SQLite, Postgres ou equivalente)

---

### 🟧 **Desafio 3 — Docker Compose e Orquestração**

Criar uma arquitetura com **múltiplos serviços** (web, banco de dados, cache) orquestrados via `docker-compose`.

Foco:

* Definição de dependências com `depends_on`
* Variáveis de ambiente
* Rede interna
* Comunicação entre serviços

---

### 🟥 **Desafio 4 — Microsserviços Independentes**

Criar dois microsserviços isolados:

* Serviço A: retorna usuários
* Serviço B: consome o serviço A via HTTP

Tudo rodando em containers separados, com comunicação direta.

Foco:

* Microsserviços independentes
* Comunicação HTTP
* Dockerfiles individuais
* Healthchecks e boas práticas

---

### 🟪 **Desafio 5 — Microsserviços com API Gateway**

Introduzir arquitetura distribuída avançada com **um ponto único de entrada**:

* Gateway → /users e /orders
* Dois microsserviços independentes fornecendo dados

Foco:

* API Gateway
* Orquestração múltipla com docker-compose
* Roteamento interno
* Integração de serviços

---

# 🎓 **Propósito Educacional dos Desafios**

Os cinco desafios juntos formam uma trilha progressiva que desenvolve as seguintes habilidades:

### 🔹 **Concorrência:**

Entender como processos independentes podem coexistir, se comunicar e sincronizar.

### 🔹 **Paralelismo:**

Rodar múltiplas unidades de execução (containers/serviços) ao mesmo tempo.

### 🔹 **Distribuição:**

Implementar aplicações divididas em partes que se comunicam via protocolos de rede.

### 🔹 **Arquitetura de microsserviços:**

Projetar sistemas modulares, escaláveis e com isolamento lógico.

### 🔹 **Infraestrutura moderna (Docker):**

Aplicar conceitos essenciais para desenvolvimento em nuvem e DevOps.

---

# 📑 **O que o professor avalia?**

A avaliação geral da disciplina considera:

| Critério                        | Peso | Descrição                                                         |
| ------------------------------- | ---- | ----------------------------------------------------------------- |
| **Funcionamento técnico**       | 40%  | Serviços rodando conforme requisitos, sem erros.                  |
| **Explicação no README**        | 30%  | Clareza, domínio do conteúdo, entendimento real do aluno.         |
| **Organização e Boas Práticas** | 20%  | Estrutura limpa, arquivos bem nomeados, Dockerfiles organizados.  |
| **Originalidade / Autoria**     | 10%  | Soluções próprias — nada de copiar ou repetir exemplos idênticos. |

---

# 🧾 **Entrega Obrigatória**

O repositório deve conter:

```
/desafio1
/desafio2
/desafio3
/desafio4
/desafio5
README.md  ← resumo geral (este arquivo)
```

Cada desafio deve ter:

* Dockerfile(s)
* docker-compose.yml (quando aplicável)
* README próprio explicando:

  * funcionamento
  * arquitetura
  * decisões técnicas
  * como executar e testar

---

# ✔️ **Mensagem Final**

Este conjunto de desafios representa uma jornada completa pelos pilares da computação concorrente, paralela e distribuída. Ao fim da prática, o aluno terá vivenciado desde conceitos básicos de comunicação entre processos até a construção de sistemas distribuídos completos com API Gateway — habilidades fundamentais na engenharia de software moderna.

