# NetObservatory DNS

DNS Observability Platform for ISPs, NOCs and Enterprise Networks.

---

# Overview

NetObservatory DNS is a passive DNS observability platform designed to collect, enrich, store and visualize DNS traffic from recursive resolvers such as Unbound, BIND and PowerDNS.

The platform captures DNS responses in real time, enriches them with ASN and GeoIP information, stores the data in PostgreSQL and provides advanced analytics through Grafana dashboards.

---

# Requirements

## Operating System

Supported distributions:

* Debian 12+
* Ubuntu 22.04+
* Ubuntu 24.04+

## Software

Required:

* Python 3.11+
* PostgreSQL 15+
* Git
* tcpdump
* libpcap-dev

---

# Installation

## 1. Install Dependencies

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

## 2. Clone Repository

```bash
mkdir -p /opt

cd /opt

git clone git@github.com:OliveiED/netobservatory.git

cd netobservatory
```

---

## 3. Run Automatic Installation

```bash
chmod +x install/install.sh

./install/install.sh
```

This script will:

* Create Python Virtual Environment
* Install Python Dependencies
* Prepare Project Structure

---

## 4. Create PostgreSQL Database

```bash
sudo -u postgres createuser netobservatory

sudo -u postgres createdb netobservatory
```

Optional:

```bash
sudo -u postgres psql
```

```sql
ALTER USER netobservatory WITH PASSWORD 'StrongPassword';
```

---

## 5. Create Database Structure

```bash
psql -U postgres netobservatory < schema.sql
```

---

## 6. Configure Environment Variables

Create:

```bash
cp .env.example .env
```

Edit:

```bash
vim .env
```

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=netobservatory
DB_USER=netobservatory
DB_PASS=StrongPassword
```

---

## 7. Install GeoLite2 Databases

Download:

* GeoLite2-ASN.mmdb
* GeoLite2-City.mmdb

Create directory:

```bash
mkdir -p /root/geoip
```

Copy files:

```text
/root/geoip/GeoLite2-ASN.mmdb
/root/geoip/GeoLite2-City.mmdb
```

---

## 8. Configure Capture Interface

Edit:

```bash
collectors/dns_collector.py
```

Locate:

```python
INTERFACE = "ens33"
```

Adjust according to your environment.

Examples:

```python
INTERFACE = "eth0"
```

```python
INTERFACE = "ens33"
```

```python
INTERFACE = "bond0"
```

---

# Starting Collector

Activate virtual environment:

```bash
source venv/bin/activate
```

Start manually:

```bash
python -m collectors.dns_collector
```

Expected output:

```text
[*] NetObservatory DNS Collector Started
[*] Listening on interface: ens33
```

---

# Configure Systemd Service

Create:

```bash
vim /etc/systemd/system/netobservatory-dns.service
```

Content:

```ini
[Unit]
Description=NetObservatory DNS Collector
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/netobservatory
ExecStart=/opt/netobservatory/venv/bin/python -m collectors.dns_collector
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Reload services:

```bash
systemctl daemon-reload
```

Enable service:

```bash
systemctl enable netobservatory-dns
```

Start service:

```bash
systemctl start netobservatory-dns
```

Check status:

```bash
systemctl status netobservatory-dns
```

---

# Configure Aggregation Worker

Edit crontab:

```bash
crontab -e
```

Add:

```cron
0 * * * * cd /opt/netobservatory && /opt/netobservatory/venv/bin/python -m workers.hourly_aggregation
```

---

# Configure Data Retention

Create cleanup script:

```bash
vim /opt/netobservatory/scripts/cleanup_dns.sh
```

Content:

```bash
#!/bin/bash

psql -U netobservatory -d netobservatory -c "
DELETE
FROM dns_queries
WHERE timestamp < NOW() - INTERVAL '30 days';
"
```

Grant permission:

```bash
chmod +x /opt/netobservatory/scripts/cleanup_dns.sh
```

Add to crontab:

```cron
0 3 * * * /opt/netobservatory/scripts/cleanup_dns.sh
```

---

# Verify Installation

Verify service:

```bash
systemctl status netobservatory-dns
```

Verify collector logs:

```bash
journalctl -fu netobservatory-dns
```

Verify inserts:

```sql
SELECT COUNT(*)
FROM dns_queries;
```

Verify latest records:

```sql
SELECT
    timestamp,
    client_ip,
    domain,
    resolved_ip,
    asn
FROM dns_queries
ORDER BY id DESC
LIMIT 10;
```

---

# Performance Features

Current optimizations:

* PostgreSQL Connection Pool
* GeoIP Memory Cache
* ASN Cache
* Optimized PostgreSQL Indexes
* IPv4 Support
* IPv6 Support

---

# Grafana Dashboards

Available dashboards:

* DNS Overview
* Top Domains
* Top Clients
* Active Clients
* ASN Analytics
* GeoIP Analytics
* Top Resolved IPs
* Query Type Distribution

---

# Project Structure

```text
netobservatory/

├── app/
│   ├── services/
│   │   ├── database.py
│   │   └── geoip_service.py
│   │
│   └── config/
│
├── collectors/
│   └── dns_collector.py
│
├── workers/
│   └── hourly_aggregation.py
│
├── scripts/
│   └── cleanup_dns.sh
│
├── docs/
│   ├── INSTALL.md
│   └── DASH-ESTRUTURA-CONSULTA.md
│
├── install/
│   └── install.sh
│
├── schema.sql
│
├── requirements.txt
│
└── venv/
```

---

# Current Version

## v1.1.0

Implemented:

* DNS Collection
* IPv4 Analytics
* IPv6 Analytics
* ASN Analytics
* GeoIP Analytics
* Client IP Tracking
* DNS Server Tracking
* PostgreSQL Connection Pool
* GeoIP Memory Cache
* Automated Retention
* Hourly Aggregation

---

# Roadmap

## v1.2.0

* Bulk Insert Processing
* Buffered DNS Ingestion

## v1.3.0

* PostgreSQL Partitioning

## v2.0.0

* Interactive Geographic Maps
* Native Web Interface
* Multi-Tenant Support

---

# Author

Evandro Duarte

NetObservatory DNS - Advanced DNS Observability Platform

