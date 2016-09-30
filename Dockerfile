FROM python:2.7-wheezy
MAINTAINER Martin Peeters (@mpeeters)

RUN apt-get update
RUN	apt-get install -y gammu gammu-smsd python-gammu
RUN adduser root dialout
RUN adduser root gammu
RUN adduser root tty

RUN mkdir /opt/sms
COPY Makefile /opt/sms
COPY README.rst /opt/sms
COPY bootstrap.py /opt/sms
COPY buildout.cfg /opt/sms
COPY setup.py /opt/sms
COPY affinitic /opt/sms/affinitic

RUN cd /opt/sms && python bootstrap.py
RUN cd /opt/sms && bin/buildout

## Clean up
RUN rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH=/usr/lib/python2.7/dist-packages
