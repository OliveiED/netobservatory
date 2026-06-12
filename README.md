# NetObservatory DNS

## DNS Observability Platform for ISPs, NOCs and Network Engineers

NetObservatory DNS is a passive DNS observability platform designed to collect, enrich, store and visualize DNS activity from recursive resolvers such as Unbound, BIND and PowerDNS.

The platform provides real-time visibility into client behavior, DNS traffic patterns, domain popularity, ASN distribution, geolocation intelligence and DNS infrastructure usage.

Built for Internet Service Providers (ISPs), Network Operations Centers (NOCs), Security Operations Centers (SOCs) and enterprise networks, NetObservatory DNS enables large-scale DNS analytics using PostgreSQL and Grafana.

---

## Features

### DNS Traffic Collection

* Passive DNS monitoring
* Recursive DNS observability
* IPv4 and IPv6 support
* A and AAAA record collection
* Client IP identification
* DNS Server IP identification
* Real-time packet capture
* Multi-answer DNS response processing

### DNS Intelligence

* Top Queried Domains
* Top Active Clients
* Top Resolved IPs
* ASN Distribution
* Autonomous System Analysis
* Geographic Intelligence
* Country Distribution
* City Distribution
* DNS Infrastructure Visibility

### GeoIP Enrichment

* ASN Lookup
* Organization Lookup
* Country Identification
* City Identification
* MaxMind GeoLite2 Integration
* In-memory GeoIP Cache

### Grafana Dashboards

* DNS Queries Over Time
* Active Clients
* Top Domains
* Top Resolved IPs
* ASN Rankings
* Geographic Distribution
* Query Type Analysis (A / AAAA)
* DNS Traffic Trends
* DNS Usage Analytics

### Database

* PostgreSQL Backend
* Historical DNS Storage
* Optimized Indexes
* Connection Pooling
* Aggregated Statistics
* Long-Term Retention Support

### Performance

* PostgreSQL Connection Pool
* GeoIP Memory Cache
* Optimized DNS Processing
* Low Resource Consumption
* High-Speed DNS Ingestion

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
│   ├── cleanup_dns.sh
│   └── backup.sh
│
├── docs/
│   ├── INSTALL.md
│   └── DASH-ESTRUTURA-CONSULTA.md
│
├── requirements/
│
└── venv/
```

---

## Main Components

### DNS Collector

Captures DNS traffic directly from a network interface and stores enriched DNS information into PostgreSQL.

Collected fields:

* Timestamp
* Client IP
* DNS Server IP
* Domain
* Query Type
* Resolved IP
* ASN
* Organization
* Country
* City

### GeoIP Service

Performs ASN and geolocation enrichment using MaxMind databases.

Information provided:

* ASN Number
* ASN Organization
* Country
* City

### Aggregation Worker

Processes historical DNS data and generates optimized statistics for dashboards and future reporting modules.

### Cleanup Jobs

Automatically removes old records according to the configured retention policy.

---

## Use Cases

### Internet Service Providers (ISP)

* Subscriber DNS visibility
* DNS traffic analysis
* Capacity planning
* Abuse investigation

### Network Operations Centers (NOC)

* DNS monitoring
* Service visibility
* Client behavior analysis
* DNS infrastructure monitoring

### Security Operations Centers (SOC)

* Threat hunting
* DNS anomaly detection
* IOC investigation
* Suspicious domain analysis

### Enterprise Networks

* DNS observability
* User behavior analytics
* Application dependency mapping
* Infrastructure visibility

---

## Installation

Detailed installation instructions are available in:

```text
docs/INSTALL.md
```

---

## Current Version

### v1.1.0

Implemented features:

* IPv4 Support
* IPv6 Support
* Client IP Tracking
* DNS Server IP Tracking
* ASN Enrichment
* Country and City Enrichment
* GeoIP Memory Cache
* PostgreSQL Connection Pool
* Automated Data Aggregation
* Automated Data Retention

---

## Roadmap

### v1.2.0

* Bulk Insert Processing
* Buffered DNS Ingestion
* Increased Query Throughput

### v1.3.0

* PostgreSQL Partitioning
* Large Dataset Optimization


---

## License

Internal Project / Private Repository
© NetObservatory
