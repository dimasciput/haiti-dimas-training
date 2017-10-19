#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

until psql -h "$host" -U "postgis" -c '\l'; do
  >&2 echo "Postgis is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgis is up - executing command"
exec $cmd