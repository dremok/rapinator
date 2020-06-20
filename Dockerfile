FROM python:3.7.3-slim-stretch

RUN apt-get -y update && apt-get -y install gcc

COPY requirements.txt /
RUN pip3 --no-cache-dir install -r requirements.txt

COPY . /app
WORKDIR /app

RUN chmod -x ./rapinator/app.py

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["gunicorn", "rapinator.app:api", "--timeout", "300", "-w", "2", "-b", "0.0.0.0:8003"]
