# Dockerfile

FROM python:3.11.0-alpine3.16

ADD requirements.txt /app/requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps build-base nginx \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

ADD policy /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PYTHONPATH /app:/app/server:/app/project:/app/policy
ENV SECRET_KEY overwrite_in_docker_config
ENV HOSTNAME fdqn

RUN source /env/bin/activate && python manage.py makemigrations && python manage.py migrate && python manage.py createcachetable

# start server
EXPOSE 8000

CMD ["/app/start-server.sh"]