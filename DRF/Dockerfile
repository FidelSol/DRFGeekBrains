FROM python:3.9

RUN apt-get update && apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip
RUN pip3 install pipenv

COPY ./ ./
RUN pipenv sync