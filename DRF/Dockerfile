FROM python:3.8.10

RUN apt-get update && apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

# set work directory
WORKDIR /home/django/DRFproject/DRFGeekBrains/DRF

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./ ./
RUN pip3 install gunicorn