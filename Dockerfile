FROM python:3
MAINTAINER Lucas M. Sing

RUN mkdir /src
WORKDIR /src
COPY ./ /src

RUN pip install -r requirements.txt

