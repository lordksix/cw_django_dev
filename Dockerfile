FROM python:3.11
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV COLUMNS 80
WORKDIR /code
COPY requirements.txt /code/
RUN addgroup --system user && adduser --system --group user
RUN apt-get update -y && \
    apt-get install -y netcat-traditional && \
    apt-get install -y gcc python3-dev musl-dev libmagic1 libffi-dev libzmq3-dev git && \
    pip install --upgrade pip && \
    pip install -r requirements.txt
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

COPY . .
USER user
ENTRYPOINT ["/code/entrypoint.sh"]
