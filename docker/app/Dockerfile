FROM python:latest

ENV TZ=Asia/Tokyo
ENV APP_ROOT=/app
ENV SELENIUM_HUB_URL=http://selenium:4444/wd/hub
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR $APP_ROOT

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
