FROM python:3
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV COLUMNS 80
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update -y && \
    apt-get install -y netcat-openbsd && \
    apt-get install -y netcat-traditional && \
    apt-get install -y gcc python3-dev musl-dev libmagic1 libffi-dev libzmq3-dev git && \
    pip install --upgrade pip && \
    pip install -r requirements.txt
COPY ./entrypoint.sh .
RUN chmod +x /code/entrypoint.sh

COPY . .

ENTRYPOINT ["/code/entrypoint.sh"]

CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT
