FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get install -y \ 
    mysql-client
RUN apt-get update -y && apt-get install -y \
    apache2 \
    curl \
    git \
    python3.9 \
    python3-pip \
    python3-mysqldb \
    python3-tk \
    tk-dev \
    python3-venv \
    python3-dev \
    libpython3.9-stdlib \
    php7.4-cli

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt 

RUN pip3 install mysql-connector-python

RUN useradd -rm -d /home/omar -s /bin/bash -g root -G sudo -u 1001 omar

WORKDIR /home/omar

COPY . /home/omar

EXPOSE 3000

RUN mkdir /var/run/mysqld

RUN echo "#!/bin/bash" > script.sh && echo "python3 work.py" >> script.sh && chmod +x script.sh
ENTRYPOINT ["/home/omar/script.sh"]
