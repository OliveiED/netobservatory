#!/bin/bash

psql -U netobservatory \
     -d netobservatory \
     -c "
DELETE FROM dns_queries
WHERE timestamp < NOW() - INTERVAL '30 days';
"
