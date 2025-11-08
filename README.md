# Integração AWS, Docker, Python e CoinMarketCap API

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)

Projeto desenvolvido na **Aula 08 do Bootcamp de Cloud e AWS**, com o objetivo de construir uma arquitetura completa na **AWS**, utilizando **EC2**, **RDS (PostgreSQL)**, **Docker** e **Python** para consumir a **API do CoinMarketCap** e armazenar automaticamente os dados coletados.

---

## Visão Geral do Projeto

A aplicação realiza requisições à **API do CoinMarketCap** para capturar informações sobre criptomoedas e persistir os dados em um banco **PostgreSQL** hospedado no **Amazon RDS**.

A infraestrutura foi construída dentro de uma **VPC (Virtual Private Cloud)** com:

- Uma sub-rede pública para a instância **EC2** (container Docker com aplicação Python).
- Uma sub-rede privada para o **RDS PostgreSQL**.
- Grupos de segurança independentes para cada recurso.

---

## Arquitetura

```
API CoinMarketCap (Request)
          ↓
Amazon EC2 → Docker → Aplicação Python
          ↓
Amazon RDS (PostgreSQL)
```

Fluxo resumido:
1. A aplicação Python, em execução na EC2, realiza chamadas à API do CoinMarketCap.  
2. Os dados retornados são processados e inseridos no PostgreSQL no Amazon RDS.  
3. Um scheduler em Python executa novas coletas a cada 5 segundos, mantendo o processo contínuo.

---

## Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|-------------|
| **Cloud** | AWS EC2, AWS RDS, AWS VPC |
| **Linguagem** | Python |
| **Containers** | Docker |
| **Banco de Dados** | PostgreSQL |
| **Gerenciamento de Variáveis** | python-dotenv |
| **Fonte de Dados** | CoinMarketCap API |

---

## Estrutura do Projeto

```
aws-rds-api/
├── src/
│   ├── main.py              # Script principal com integração e ETL
│   ├── db_connection.py     # Conexão e persistência no PostgreSQL
│   ├── scheduler.py         # Agendador de execuções periódicas
│   └── utils/
│       └── helpers.py       # Funções auxiliares
├── Dockerfile               # Configuração do container
├── requirements.txt         # Dependências do projeto
├── .env.example             # Modelo de variáveis de ambiente
└── README.md                # Documentação
```

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
CMC_API_KEY=your_coinmarketcap_api_key
DB_HOST=your_rds_endpoint
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_PORT=5432
```

> **Atenção:** o arquivo `.env` não deve ser versionado ou compartilhado publicamente.

---

## Como Executar o Projeto Localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/Matheus-ESW/aws-rds-api.git
```

### 2. Acessar o diretório

```bash
cd aws-rds-api
```

### 3. Criar o arquivo `.env`

```bash
cp .env.example .env
```

Preencha com suas credenciais da API CoinMarketCap e do banco RDS.

### 4. Criar ambiente virtual (opcional, se rodar sem Docker)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Executar o projeto

```bash
python src/main.py
```

---

## Executando com Docker

### 1. Build da imagem

```bash
docker build -t aws-rds-api .
```

### 2. Execução do container

```bash
docker run --env-file .env aws-rds-api
```

---

## Resultado Final

Arquitetura completa, segura e escalável, unindo:

> **AWS (EC2 + RDS) + Docker + Python + API CoinMarketCap**

Essa solução demonstra, na prática, como integrar **nuvem, contêineres e dados** para criar pipelines modernos de engenharia de dados.

---

## Repositório

🔗 [https://github.com/Matheus-ESW/aws-rds-api](https://github.com/Matheus-ESW/aws-rds-api)

---

## Autor

**Matheus Ramos**  
Analista e entusiasta de Engenharia de Dados  
📍 Jornada de Dados — Bootcamp Cloud & AWS  
🔗 [LinkedIn](https://www.linkedin.com/in/matheussoaresramos/)
