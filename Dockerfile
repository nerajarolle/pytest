FROM python:3-slim-bullseye

COPY src src
COPY requirements.txt .


RUN pip install -r requirements.txt

WORKDIR /src
