FROM python:2.7

RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
RUN  dpkg-divert --local --rename --add /sbin/initctl

RUN apt-get -y update
RUN apt-get -y install \
    python-gdal \
    python-geoip \
    npm \
    nodejs \
    rpl

ADD uwsgi.conf /uwsgi.conf

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 8080

WORKDIR /home/web/django_project

ADD wait-for-it.sh /wait-for-it.sh
RUN chmod 0755 /wait-for-it.sh

CMD ["uwsgi", "--ini", "/uwsgi.conf"]
