FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
RUN chmod -R 777 /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
