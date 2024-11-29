#!/bin/bash
set -e
alembic upgrade head

db_exists=$(sqlite3 /app/mydatabase.db "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='customers';")
data_exists=$(sqlite3 /app/mydatabase.db "SELECT count(*) FROM customers;")

if [ "$db_exists" -eq "1" ] && [ "$data_exists" -eq "0" ]; then
    echo "Инициализация базы данных..."
    sqlite3 /app/mydatabase.db < ./dump/init.sql
else
    echo "База данных уже заполнена."
fi

exec gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080
