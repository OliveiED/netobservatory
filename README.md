# NetObservatory DNS

DNS Observability Platform for ISPs, NOCs and Network Engineers.

NetObservatory DNS is a passive DNS analytics platform designed to collect, store and visualize DNS activity from recursive resolvers such as Unbound, BIND and PowerDNS.

The platform provides real-time visibility into client behavior, DNS traffic patterns, domain popularity, ASN distribution, geolocation intelligence and DNS infrastructure usage.

---

## Features

### DNS Traffic Collection

* Passive DNS monitoring
* IPv4 and IPv6 support
* A and AAAA record collection
* Client identification
* DNS server identification

### DNS Intelligence

* Top Queried Domains
* Top Clients
* Top Resolved IPs
* ASN Analysis
* GeoIP Enrichment
* Country Distribution
* City Distribution

### Grafana Dashboards

* DNS Queries per Second
* Active Clients
* Domain Ranking
* ASN Ranking
* Geographic Distribution
* DNS Traffic Trends

### Database

* PostgreSQL backend
* Historical DNS storage
* Aggregated statistics
* Long-term retention support

---

## Technology Stack

* Python 3
* PostgreSQL
* Grafana
* Scapy
* MaxMind GeoLite2
* Systemd
* Linux

---

## Project Structure

```text
netobservatory/

├── app/
│   ├── services/
│   └── config/
│
├── collectors/
│   └── dns_collector.py
│
├── workers/
│   └── hourly_aggregation.py
│
├── scripts/
│
├── requirements/
│
├── docs/
│   └── INSTALL.md
│
└── venv/
```

---

## Main Components

### DNS Collector

Captures DNS traffic directly from a network interface and stores enriched information in PostgreSQL.

Collected information:

* Client IP
* DNS Server IP
* Domain
* Query Type
* Resolved IP
* ASN
* Organization
* Country
* City
* Timestamp

### Aggregation Worker

Processes historical DNS data and generates optimized statistics for dashboards and reporting.

### Cleanup Jobs

Automatically removes old records according to the configured retention policy.

---

## Installation

Detailed installation instructions are available in:

```text
docs/INSTALL.md
```

---

## Use Cases

* Internet Service Providers (ISP)
* Network Operations Centers (NOC)
* Security Operations Centers (SOC)
* DNS Infrastructure Monitoring
* Capacity Planning
* Traffic Analysis
* Threat Hunting
* Network Visibility

---

## License

Internal Project / Private Repository

