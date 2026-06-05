from app.services.database import get_connection


def aggregate_dns():

    connection = get_connection()

    cursor = connection.cursor()

    query = """

    INSERT INTO dns_stats_hourly (
        timestamp_hour,
        domain,
        query_type,
        total_queries,
        avg_latency,
        nxdomain_count
    )

    SELECT
        date_trunc('hour', timestamp) AS timestamp_hour,

        domain,

        query_type,

        COUNT(*) AS total_queries,

        AVG(latency_ms) AS avg_latency,

        COUNT(*) FILTER (
            WHERE response_code = 'NXDOMAIN'
        ) AS nxdomain_count

    FROM dns_queries

    WHERE timestamp >= NOW() - INTERVAL '1 hour'

    GROUP BY
        timestamp_hour,
        domain,
        query_type

    """

    cursor.execute(query)

    connection.commit()

    cursor.close()
    connection.close()

    print("[+] DNS hourly aggregation completed")


if __name__ == "__main__":

    aggregate_dns()
