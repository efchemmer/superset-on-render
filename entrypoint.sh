#!/bin/bash
set -e

# Step 1: Wait for DB to be ready (optional but recommended for new deploys)
echo "Waiting for database..."
until superset db upgrade; do
  echo "Database not ready, retrying in 5s..."
  sleep 5
done

# Step 2: Create admin user if it doesn't exist
echo "Checking if admin user exists..."
if ! superset fab list-users | grep -q admin; then
  echo "Creating Superset admin user..."
  superset fab create-admin \
    --username admin \
    --firstname Superset \
    --lastname Admin \
    --email efchemmer@yahoo.com.br \
    --password "${SUPERSET_ADMIN_PASSWORD:-admin}"
else
  echo "Admin user already exists, skipping creation."
fi

# Step 3: Initialize Superset
echo "Running superset init..."
superset init

# Step 4: Start Superset server
echo "Starting Superset web server..."
exec gunicorn \
    --bind 0.0.0.0:8088 \
    --workers 3 \
    --worker-class gthread \
    --threads 8 \
    --timeout 60 \
    "superset.app:create_app()"