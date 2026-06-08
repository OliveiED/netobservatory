# NetObservatory

Plataforma de observabilidade DNS desenvolvida para coletar, armazenar, analisar e visualizar consultas DNS em tempo real.

O projeto captura tráfego DNS diretamente da rede, enriquece os dados com informações de GeoIP e ASN e disponibiliza métricas avançadas através de dashboards Grafana.

---

## Funcionalidades

* Captura de consultas DNS em tempo real
* Suporte IPv4 e IPv6
* Identificação do cliente DNS
* Identificação do servidor DNS
* Resolução de registros A e AAAA
* GeoIP (País e Cidade)
* ASN e Organização
* Estatísticas de domínios
* Estatísticas por cliente
* Estatísticas por ASN
* Top domínios consultados
* Top IPs resolvidos
* Clientes ativos
* Dashboards avançados Grafana
* Banco PostgreSQL

---

## Tecnologias Utilizadas

### Backend

* Python 3.11+
* Scapy
* PostgreSQL
* Psycopg2

### Visualização

* Grafana
* Business Charts
* Geomap

### Banco de Dados

* PostgreSQL

### Enriquecimento

* GeoLite2 ASN
* GeoLite2 City

---

## Arquitetura

Cliente DNS
↓
Servidor DNS (Unbound)
↓
NetObservatory Collector
↓
PostgreSQL
↓
Grafana

---

## Requisitos

### Sistema Operacional

* Debian 12+
* Ubuntu 22.04+
* Ubuntu 24.04+

### Pacotes necessários

* Python 3
* Python venv
* PostgreSQL
* Git

---

# Instalação

## 1 - Clonar o Projeto

```bash
git clone https://github.com/OliveiED/netobservatory.git

cd netobservatory
```

---

## 2 - Executar instalação automática

```bash
chmod +x install/install.sh

./install/install.sh
```

O script realiza:

* Criação do ambiente virtual Python
* Instalação das dependências
* Configuração inicial do projeto

---

## 3 - Criar Banco PostgreSQL

```bash
sudo -u postgres createdb netobservatory
```

---

## 4 - Criar Estrutura do Banco

```bash
psql -U postgres netobservatory < schema.sql
```

---

## 5 - Configurar Banco

Editar:

```bash
app/services/database.py
```

Exemplo:

```python
DB_HOST = "localhost"
DB_NAME = "netobservatory"
DB_USER = "postgres"
DB_PASSWORD = "senha"
```

---

## 6 - Configurar GeoIP

Copiar os bancos MaxMind:

```text
GeoLite2-ASN.mmdb
GeoLite2-City.mmdb
```

para:

```text
database/geoip/
```

---

# Inicialização

Ativar ambiente virtual:

```bash
source venv/bin/activate
```

Iniciar coletor DNS:

```bash
python -m collectors.dns_collector
```

---

## Execução em segundo plano

Exemplo utilizando screen:

```bash
screen -S netobservatory

source venv/bin/activate

python -m collectors.dns_collector
```

Desanexar:

```bash
CTRL+A D
```

---

# Estrutura do Projeto

```text
netobservatory/

├── app/
│   ├── services/
│   ├── models/
│   └── utils/
│
├── collectors/
│   └── dns_collector.py
│
├── database/
│   ├── geoip/
│   └── schema.sql
│
├── install/
│   └── install.sh
│
├── workers/
│
├── grafana/
│
├── venv/
│
└── README.md
```

---

# Principais Métricas

## DNS

* Total de consultas
* Consultas por segundo
* Top domínios
* Top clientes
* Clientes ativos
* Tipos de registros DNS

## GeoIP

* Países mais acessados
* Cidades mais acessadas

## ASN

* ASN mais consultados
* Organizações mais consultadas

## Resolução

* Top IPs resolvidos
* Distribuição IPv4
* Distribuição IPv6

---

# Dashboards

O projeto possui dashboards Grafana para:

* DNS Overview
* Clientes DNS
* ASN Analytics
* GeoIP Analytics
* Top Domínios
* Top Resolved IPs
* Clientes Ativos
* Distribuição de Consultas

---

# Segurança

Recomendado:

* Executar o coletor com usuário dedicado
* Restringir acesso ao PostgreSQL
* Utilizar SSH com chaves ED25519
* Manter GeoLite2 atualizado

---

# Autor

Evandro Duarte

Projeto criado para monitoramento, observabilidade e análise avançada de tráfego DNS.

