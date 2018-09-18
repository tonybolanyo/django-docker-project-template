FROM python:3.7.0-stretch

RUN apt-get update
RUN apt-get install -y binutils libproj-dev gdal-bin

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN mkdir /app
WORKDIR /app

RUN mkdir requirements
COPY ./requirements/base.txt ./requirements/
COPY ./requirements/dev.txt ./requirements/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements/dev.txt

COPY . .

WORKDIR /app/src
