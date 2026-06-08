# DASH-ESTRUTURA-CONSULTA

Estrutura oficial das consultas SQL utilizadas na construção dos dashboards do NetObservatory DNS.

---

# 1. Top Domínios Consultados

Exibe os domínios mais consultados durante o período selecionado no Grafana.

```sql
SELECT
    domain,
    COUNT(*) AS total
FROM dns_queries
WHERE
    $__timeFilter(timestamp)
    AND domain IS NOT NULL
    AND domain <> ''
GROUP BY domain
ORDER BY total DESC
LIMIT 20;
```

### Uso

* Top Sites Acessados
* DNS Ranking
* Popularidade de Domínios

---

# 2. Clientes DNS Ativos

Quantidade de clientes únicos realizando consultas DNS ao longo do tempo.

```sql
SELECT
    date_trunc('minute', timestamp) AS time,
    COUNT(DISTINCT client_ip) AS clientes
FROM dns_queries
WHERE
    $__timeFilter(timestamp)
    AND client_ip IS NOT NULL
GROUP BY 1
ORDER BY 1;
```

### Uso

* Clientes ativos
* Tendência de utilização
* Crescimento de usuários

---

# 3. Volume Total de Consultas DNS

Quantidade total de consultas DNS ao longo do tempo.

```sql
SELECT
    $__timeGroupAlias(timestamp,$__interval),
    COUNT(*) AS total
FROM dns_queries
WHERE $__timeFilter(timestamp)
GROUP BY 1
ORDER BY 1;
```

### Uso

* DNS Queries per Second
* Capacidade DNS
* Tendência de utilização

---

# 4. Distribuição por Tipo de Consulta

Distribuição de registros DNS do tipo A e AAAA.

```sql
SELECT
    $__timeGroupAlias(timestamp, $__interval),
    query_type,
    COUNT(*) AS total
FROM dns_queries
WHERE
    $__timeFilter(timestamp)
    AND query_type IN ('A','AAAA')
GROUP BY 1,2
ORDER BY 1;
```

### Uso

* IPv4 x IPv6
* Evolução da adoção IPv6

---

# 5. Top Clientes DNS

Clientes que mais geraram consultas DNS.

```sql
SELECT
    client_ip AS "Cliente",
    COUNT(*) AS "Consultas"
FROM dns_queries
WHERE
    client_ip IS NOT NULL
    AND timestamp >= NOW() - INTERVAL '30 days'
GROUP BY client_ip
ORDER BY "Consultas" DESC
LIMIT 20;
```

### Uso

* Heavy Users
* Clientes corporativos
* Identificação de abusos

---

# 6. ASN com Maior Diversidade de Domínios

Ranking de ASN por quantidade de domínios distintos.

```sql
SELECT
    as_org,
    COUNT(DISTINCT domain) AS dominios
FROM dns_queries
WHERE
    as_org IS NOT NULL
    AND $__timeFilter(timestamp)
GROUP BY as_org
ORDER BY dominios DESC
LIMIT 20;
```

### Uso

* Distribuição de conteúdo
* Principais provedores de serviços

---

# 7. Distribuição Geográfica

Países mais acessados através das resoluções DNS.

```sql
SELECT
    country,
    COUNT(*) AS total
FROM dns_queries
WHERE country IS NOT NULL
AND $__timeFilter(timestamp)
GROUP BY country
ORDER BY total DESC
LIMIT 10;
```

### Uso

* GeoMap
* HeatMap
* Distribuição global de conteúdo

---

# 8. Distribuição por Tipo DNS

Percentual de cada tipo de consulta.

```sql
SELECT
    query_type,
    COUNT(*) AS total,
    ROUND(
        COUNT(*) * 100.0 /
        SUM(COUNT(*)) OVER (),
        2
    ) AS percent
FROM dns_queries
WHERE $__timeFilter(timestamp)
GROUP BY query_type
ORDER BY total DESC;
```

### Uso

* Pizza DNS
* Distribuição de registros

---

# 9. Top IPs Resolvidos

Endereços IP mais retornados pelo DNS.

```sql
SELECT
    resolved_ip,
    as_org,
    COUNT(*) AS total
FROM dns_queries
WHERE
    $__timeFilter(timestamp)
    AND resolved_ip IS NOT NULL
GROUP BY resolved_ip, as_org
ORDER BY total DESC
LIMIT 20;
```

### Uso

* CDN Analysis
* Cache Analysis
* Destinos mais populares

---

# Dashboards Recomendados

## Visão Executiva

* Total Queries
* Clientes Ativos
* Top Domínios
* Distribuição por País

## Engenharia ISP

* Top Clientes
* ASN Dominantes
* IPv4 x IPv6
* Top IPs Resolvidos

## Segurança

* Domínios Anômalos
* ASN Suspeitos
* Países Incomuns
* Picos de Consultas

## Capacity Planning

* Queries por Segundo
* Crescimento de Clientes
* Evolução DNS
* Tendência de Consumo

---

# Banco Utilizado

Tabela principal:

```sql
dns_queries
```

Campos principais:

```text
timestamp
client_ip
dns_server_ip
domain
query_type
resolved_ip
country
city
asn
as_org
```

---

Documento mantido para padronização dos dashboards oficiais do NetObservatory DNS.

