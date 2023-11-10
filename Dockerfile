FROM python:3.9-slim

RUN mkdir -p /data/input
RUN mkdir -p /data/output
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


WORKDIR /app
COPY app /app
