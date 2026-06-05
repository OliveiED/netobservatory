from datetime import datetime

from app.services.database import get_connection


BEACON_THRESHOLD = 15


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

    print(f"[!] Beaconing Detected: {domain}")


def detect_beaconing():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            src_ip,
            domain,
            COUNT(*) AS total

        FROM dns_queries

        WHERE timestamp >= NOW() - INTERVAL '1 hour'

        GROUP BY src_ip, domain

        HAVING COUNT(*) >= %s
        """,
        (BEACON_THRESHOLD,)
    )

    results = cursor.fetchall()

    for row in results:

        src_ip = row[0]
        domain = row[1]
        total = row[2]

        save_threat(
            src_ip,
            domain,
            "DNS_BEACONING",
            "HIGH",
            f"Repeated DNS requests detected ({total} requests)"
        )

    cursor.close()
    connection.close()


if __name__ == "__main__":

    print("[*] Beacon Detection Engine Started")

    detect_beaconing()

    print("[+] Beacon analysis completed")
