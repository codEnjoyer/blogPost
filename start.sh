#!/bin/bash
cd src || exit
alembic upgrade 4836c0df2d4a
gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 --timeout 600