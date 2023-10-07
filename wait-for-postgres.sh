#!/bin/bash

# Exit if any command fails
set -e

# Wait until PostgreSQL is ready
until PGPASSWORD=password psql -h "localhost" -p "5433" -U "user" -d "testdb" -c '\l' > /dev/null 2>&1; do
  sleep 1
done

exec $cmd
