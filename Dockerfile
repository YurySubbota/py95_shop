FROM python:3.10.2

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirement.txt ./

RUN pip3 install -r 'requirement.txt'

COPY . .
