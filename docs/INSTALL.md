# 🔭 NetObservatory

Plataforma de Observabilidade DNS para ISPs, Datacenters e Redes Corporativas.

O NetObservatory coleta consultas DNS em tempo real diretamente da rede, enriquece os dados com informações de GeoIP e ASN e disponibiliza dashboards avançados para análise de comportamento, desempenho e segurança DNS.

---

## ✨ Recursos

### DNS Analytics

* Captura DNS em tempo real
* Suporte IPv4 e IPv6
* Registros A e AAAA
* Top Domínios
* Top Clientes
* Clientes Ativos
* Consultas por minuto
* Tipos de consulta DNS

### GeoIP Analytics

* Países acessados
* Cidades acessadas
* ASN de destino
* Organização responsável pelo ASN

### Dashboards Grafana

* DNS Overview
* Top Domains
* Top Clients
* Active Clients
* ASN Analytics
* GeoIP Analytics
* Resolved IP Analytics

### Enriquecimento

* GeoLite2 City
* GeoLite2 ASN
* ASN Organization Lookup

---

# 🏗 Arquitetura

```text
Clientes
    │
    ▼
Servidor DNS (Unbound)
    │
    ▼
NetObservatory Collector
    │
    ▼
PostgreSQL
    │
    ▼
Grafana Dashboards
```

---

# 🛠 Tecnologias

| Componente     | Tecnologia       |
| -------------- | ---------------- |
| Backend        | Python           |
| Packet Capture | Scapy            |
| Banco          | PostgreSQL       |
| Dashboards     | Grafana          |
| GeoIP          | MaxMind GeoLite2 |
| Versionamento  | Git              |
| Hospedagem     | Linux            |

---

# 📋 Requisitos

### Sistemas Operacionais

* Debian 12+
* Ubuntu 22.04+
* Ubuntu 24.04+

### Dependências

* Python 3.11+
* PostgreSQL 15+
* Git
* Pip
* Virtual Environment (venv)

---

# 🚀 Instalação

## 1. Instalar dependências

Debian / Ubuntu:

```bash
apt update

apt install -y \
git \
python3 \
python3-pip \
python3-venv \
postgresql \
postgresql-contrib \
tcpdump \
libpcap-dev
```

---

## 2. Clonar o projeto

```bash
mkdir -p /root/projects

cd /root/projects

git clone https://github.com/OliveiED/netobservatory.git

cd netobservatory
```

---

## 3. Executar instalação automática

```bash
chmod +x install/install.sh

./install/install.sh
```

O script cria:

* Ambiente virtual Python
* Instala dependências
* Estrutura inicial do projeto

---

## 4. Criar banco PostgreSQL

```bash
sudo -u postgres createdb netobservatory
```

---

## 5. Criar estrutura do banco

```bash
psql -U postgres netobservatory < schema.sql
```

---

## 6. Configurar conexão PostgreSQL

Editar:

```text
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

## 7. Instalar GeoLite2

Baixar:

* GeoLite2-ASN.mmdb
* GeoLite2-City.mmdb

e copiar para:

```text
database/geoip/
```

---

# ▶️ Executando

Ativar ambiente virtual:

```bash
source venv/bin/activate
```

Executar coletor:

```bash
python -m collectors.dns_collector
```

Saída esperada:

```text
[*] NetObservatory DNS Collector Started
[*] Listening on interface: ens33
```

---

# 🔄 Execução Automática

Exemplo utilizando cron:

```bash
@reboot cd /root/projects/netobservatory && \
/root/projects/netobservatory/venv/bin/python \
-m collectors.dns_collector
```

---

# 📂 Estrutura do Projeto

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
├── workers/
│
├── database/
│   └── geoip/
│
├── install/
│   └── install.sh
│
├── grafana/
│
├── schema.sql
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Métricas Disponíveis

## DNS

* Total de consultas
* Top domínios
* Top clientes
* Clientes ativos
* Domínios únicos
* Tipos de consultas

## ASN

* Top ASN
* ASN por consultas
* ASN por domínios
* Organizações mais acessadas

## GeoIP

* Países
* Cidades
* ASN de destino

## Resolução

* IPs mais resolvidos
* IPv4 x IPv6

---

# 📈 Grafana

O projeto utiliza Grafana para visualização dos dados.

Dashboards disponíveis:

* DNS Overview
* Top Domains
* Top Clients
* Active Clients
* ASN Analytics
* GeoIP Analytics
* Top Resolved IPs

---

# 🔒 Segurança

Recomendações:

* Utilizar usuário dedicado
* Restringir acesso ao PostgreSQL
* Utilizar autenticação SSH por chave
* Atualizar regularmente os bancos GeoLite2

---

# 👨‍💻 Autor

Evandro Duarte

Projeto desenvolvido para observabilidade DNS, análise de tráfego e inteligência de rede em ambientes ISP e corporativos.

