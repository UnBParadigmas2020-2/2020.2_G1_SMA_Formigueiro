FROM python:3.7-slim

EXPOSE 20000 8000 5000 8001

RUN mkdir /code

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt
