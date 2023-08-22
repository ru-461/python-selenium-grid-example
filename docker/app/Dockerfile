FROM python:3.11-slim-bullseye

WORKDIR /app

COPY ./docker/app/requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
