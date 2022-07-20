FROM --platform=linux/amd64 python:3.10.2-slim
LABEL maintainer="mcx.ink"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=true

RUN python3 -m venv /opt/venvmz
RUN /opt/venvmz/bin/python3 -m pip install --upgrade pip

RUN if [ $DEV = "true" ]; then \
        echo "Installing DEV Requirements!" && \
        /opt/venvmz/bin/pip install -r /tmp/requirements.dev.txt ; \
    else \
        echo "Installing PRODUCTION Requirements!" && \
        apt-get update && \
        apt-get install -y libpq-dev gcc && \
        /opt/venvmz/bin/pip install -r /tmp/requirements.txt ; \
    fi && \
    rm -rf /tmp

RUN adduser \
        --disabled-password \
        --no-create-home \
        dockuser

ENV PATH="/opt/venvmz/bin:$PATH"

RUN mkdir -p /staticfiles/web/media
RUN mkdir -p /staticfiles/web/static
RUN chown -R dockuser:dockuser /staticfiles/
RUN chmod -R 755 /staticfiles/web

RUN chown -R dockuser:dockuser /app/

USER dockuser

RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]
