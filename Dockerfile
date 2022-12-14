FROM python:3.9.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code
RUN python3.9 -m pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel

RUN addgroup --system dokku \
    && adduser --system --ingroup dokku dokku

COPY requirements.txt /code/

RUN pip install --no-cache-dir  -r requirements.txt && rm -rf /var/lib/apt/lists/*
COPY . /code/

# Collect static files
RUN chown -R dokku:dokku /code/
# RUN chown -R dokku:dokku /code/static/
USER dokku


EXPOSE 6000

CMD [ "gunicorn", "code:code" ]