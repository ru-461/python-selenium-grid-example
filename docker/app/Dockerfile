FROM python:slim-bullseye

ENV APP_ROOT=/app
ENV SELENIUM_HUB_URL=http://selenium:4444/wd/hub
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $APP_ROOT

COPY ./docker/app/requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
