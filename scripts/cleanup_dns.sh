#!/bin/bash

DB_NAME="netobservatory"
DB_USER="netobservatory"

echo "[$(date)] Iniciando retenção..."

psql -U "$DB_USER" -d "$DB_NAME" << EOF

DELETE FROM dns_queries
WHERE timestamp < NOW() - INTERVAL '30 days';

DELETE FROM dns_hourly_stats
WHERE hour < NOW() - INTERVAL '365 days';

VACUUM ANALYZE dns_queries;
VACUUM ANALYZE dns_hourly_stats;

EOF

echo "[$(date)] Retenção finalizada."
