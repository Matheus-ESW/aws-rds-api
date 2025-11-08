# Integração AWS, Docker, Python e CoinMarketCap API

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

## Como Executar o Projeto Localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/Matheus-ESW/aws-rds-api.git
```

### 2. Acessar o diretório e construir a imagem Docker

```bash
cd aws-rds-api
sudo docker build -t api-schedule-app .
```

### 3. Execute o contêiner com as variáveis de ambiente para integração com o RDS

```bash
sudo docker run -d \
--name api-schedule-app-container \
-e DB_HOST=<endereco-rds> \
-e DB_USER=<usuario> \
-e DB_PASS=<senha> \
-e DB_NAME=<nome-do-banco> \
api-schedule-app
```

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
Analista de Banco de Dados e entusiasta de Engenharia de Dados   
🔗 [LinkedIn](https://www.linkedin.com/in/matheussoaresramos/)
