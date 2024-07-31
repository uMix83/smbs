FROM python:3.12

ADD import.py /smbs/
ADD IMOEX_230101_240601.csv /smbs/

WORKDIR /smbs/

RUN pip install --upgrade pip
RUN pip install "psycopg[binary]"
