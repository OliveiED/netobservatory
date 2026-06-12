from scapy.all import sniff
from scapy.layers.dns import DNS, dnsqtypes
from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6

from datetime import datetime, timezone

from app.services.database import get_connection, release_connection
from app.services.geoip_service import get_geoip_data

INTERFACE = "ens33"


# ==========================================
# DATABASE INSERT
# ==========================================
def save_dns_query(
    src_ip,
    dst_ip,
    domain,
    query_type,
    resolved_ip=None,
    country=None,
    city=None,
    asn=None,
    as_org=None,
    client_ip=None,
    dns_server_ip=None
):

    conn = get_connection()

    try:

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO dns_queries (
                timestamp,
                src_ip,
                dst_ip,
                domain,
                query_type,
                resolved_ip,
                country,
                city,
                asn,
                as_org,
                client_ip,
                dns_server_ip
            )
            VALUES (
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
            )
            """,
            (
                datetime.now(timezone.utc),
                src_ip,
                dst_ip,
                domain,
                query_type,
                resolved_ip,
                country,
                city,
                asn,
                as_org,
                client_ip,
                dns_server_ip
            )
        )

        conn.commit()

        cur.close()

    finally:

        release_connection(conn)

# ==========================================
# DNS PROCESSING
# ==========================================

def process_packet(packet):

    try:

        if not packet.haslayer(DNS):
            return

        dns = packet[DNS]

        # SOMENTE RESPOSTAS DNS
        if dns.qr != 1:
            return

        # IPv4
        if packet.haslayer(IP):

            src_ip = packet[IP].src
            dst_ip = packet[IP].dst

        # IPv6
        elif packet.haslayer(IPv6):

            src_ip = packet[IPv6].src
            dst_ip = packet[IPv6].dst

        else:
            return

        if not dns.qd:
            return

        domain = (
            dns.qd.qname
            .decode(errors="ignore")
            .rstrip(".")
        )

        query_type = dnsqtypes.get(
            dns.qd.qtype,
            "UNKNOWN"
        )

        # Em respostas DNS:
        # src_ip = DNS Server
        # dst_ip = Cliente

        client_ip = dst_ip
        dns_server_ip = src_ip

        # Sem resposta
        if dns.ancount == 0:

            save_dns_query(
                src_ip=src_ip,
                dst_ip=dst_ip,
                domain=domain,
                query_type=query_type,
                client_ip=client_ip,
                dns_server_ip=dns_server_ip
            )

            return

        # Percorre respostas
        for i in range(dns.ancount):

            try:

                answer = dns.an[i]

                resolved_ip = None

                # Registro A
                if answer.type == 1:
                    resolved_ip = str(answer.rdata)

                # Registro AAAA
                elif answer.type == 28:
                    resolved_ip = str(answer.rdata)

                else:
                    continue

                geo = get_geoip_data(resolved_ip)

                country = geo.get("country")
                city = geo.get("city")
                asn = geo.get("asn")
                as_org = geo.get("as_org")

                print(
                    f"[DNS] CLIENT={client_ip} "
                    f"DOMAIN={domain} "
                    f"TYPE={query_type} "
                    f"RESOLVED={resolved_ip} "
                    f"ASN={asn}"
                )

                save_dns_query(
                    src_ip=src_ip,
                    dst_ip=dst_ip,
                    domain=domain,
                    query_type=query_type,
                    resolved_ip=resolved_ip,
                    country=country,
                    city=city,
                    asn=asn,
                    as_org=as_org,
                    client_ip=client_ip,
                    dns_server_ip=dns_server_ip
                )

            except Exception as e:

                print(
                    f"[ANSWER ERROR] {e}"
                )

    except Exception as e:

        print(
            f"[COLLECTOR ERROR] {e}"
        )


# ==========================================
# START
# ==========================================

print(
    "[*] NetObservatory DNS Collector Started"
)

print(
    f"[*] Listening on interface: {INTERFACE}"
)

sniff(
    iface=INTERFACE,
    filter="udp port 53",
    prn=process_packet,
    store=False
)
