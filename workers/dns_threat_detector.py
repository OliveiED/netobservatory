from datetime import datetime

from app.services.database import get_connection


LONG_DOMAIN_THRESHOLD = 45


def save_threat(
    src_ip,
    domain,
    threat_type,
    risk_level,
    description
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO dns_threats (
            timestamp,
            src_ip,
            domain,
            threat_type,
            risk_level,
            description
        )
        VALUES (%s,%s,%s,%s,%s,%s)
        """,
        (
            datetime.now(),
            src_ip,
            domain,
            threat_type,
            risk_level,
            description
        )
    )

    connection.commit()

    cursor.close()
    connection.close()

    print(f"[!] Threat Detected: {threat_type} -> {domain}")


def detect_long_domains():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            src_ip,
            domain

        FROM dns_queries

        WHERE LENGTH(domain) > %s

        ORDER BY id DESC

        LIMIT 100
        """,
        (LONG_DOMAIN_THRESHOLD,)
    )

    results = cursor.fetchall()

    for row in results:

        src_ip = row[0]
        domain = row[1]

        save_threat(
            src_ip,
            domain,
            "LONG_DOMAIN",
            "MEDIUM",
            "Very long domain detected. Possible DNS tunneling."
        )

    cursor.close()
    connection.close()


def detect_nxdomain_spikes():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            src_ip,
            COUNT(*)

        FROM dns_queries

        WHERE response_code = 'NXDOMAIN'
        AND timestamp >= NOW() - INTERVAL '1 hour'

        GROUP BY src_ip

        HAVING COUNT(*) > 20
        """
    )

    results = cursor.fetchall()

    for row in results:

        src_ip = row[0]
        total = row[1]

        save_threat(
            src_ip,
            "MULTIPLE_DOMAINS",
            "NXDOMAIN_SPIKE",
            "HIGH",
            f"High NXDOMAIN rate detected: {total}"
        )

    cursor.close()
    connection.close()


if __name__ == "__main__":

    print("[*] NetObservatory Threat Engine Started")

    detect_long_domains()

    detect_nxdomain_spikes()

    print("[+] Threat analysis completed")
