import math
from collections import Counter
from datetime import datetime

from app.services.database import get_connection


ENTROPY_THRESHOLD = 3.8


def calculate_entropy(data):

    counter = Counter(data)

    length = len(data)

    entropy = 0

    for count in counter.values():

        probability = count / length

        entropy -= probability * math.log2(probability)

    return entropy


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

    print(f"[!] DGA Detected: {domain}")


def detect_dga_domains():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            src_ip,
            domain

        FROM dns_queries

        WHERE timestamp >= NOW() - INTERVAL '1 hour'

        ORDER BY id DESC

        LIMIT 500
        """
    )

    results = cursor.fetchall()

    for row in results:

        src_ip = row[0]
        domain = row[1]

        clean_domain = domain.replace(".", "")

        entropy = calculate_entropy(clean_domain)

        if entropy >= ENTROPY_THRESHOLD:

            save_threat(
                src_ip,
                domain,
                "DGA_DOMAIN",
                "HIGH",
                f"High entropy domain detected ({entropy:.2f})"
            )

    cursor.close()
    connection.close()


if __name__ == "__main__":

    print("[*] DGA Detection Engine Started")

    detect_dga_domains()

    print("[+] DGA analysis completed")
