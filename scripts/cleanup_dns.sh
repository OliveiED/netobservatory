#!/bin/bash

psql -U netobservatory -d netobservatory <<EOF

DELETE FROM dns_queries
WHERE timestamp < NOW() - INTERVAL '3 days';

VACUUM ANALYZE dns_queries;

EOF
