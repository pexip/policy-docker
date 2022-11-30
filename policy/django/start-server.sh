#!/usr/bin/env sh
# start-server.sh

source /env/bin/activate

gunicorn -c /app/config/gunicorn/dev.py --bind 0.0.0.0:8000 --workers 3
