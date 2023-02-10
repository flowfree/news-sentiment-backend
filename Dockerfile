FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ARG ENVIRONMENT_TO_BUILD=production
ENV DJANGO_SETTINGS_MODULE config.settings.${ENVIRONMENT_TO_BUILD}
ENV APP_HOME /app 
WORKDIR $APP_HOME 

COPY requirements.txt .
RUN apt update -y && \
    apt install -y libpq-dev gcc python3-dev python3-lxml && \
    pip install --no-cache-dir -r requirements.txt 

COPY . .

CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 config.wsgi:application
