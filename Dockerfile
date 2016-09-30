FROM python:2.7-wheezy
MAINTAINER Martin Peeters (@mpeeters)

USER root
RUN apt-get update
RUN apt-get install -y gammu gammu-smsd python-gammu
RUN useradd -ms /bin/bash -d /opt/sms sms
RUN usermod -aG dialout sms
RUN usermod -aG gammu sms
RUN usermod -aG tty sms

COPY Makefile /opt/sms
COPY README.rst /opt/sms
COPY bootstrap.py /opt/sms
COPY buildout.cfg /opt/sms
COPY setup.py /opt/sms
COPY affinitic /opt/sms/affinitic
COPY .gammurc /opt/sms
RUN mkdir /opt/sms/conf
RUN touch /opt/sms/gammu.log
RUN chown -R sms:sms /opt/sms

VOLUME /opt/sms/conf

## Clean up
RUN rm -rf /var/lib/apt/lists/*

USER sms
RUN cd /opt/sms && python bootstrap.py
RUN cd /opt/sms && bin/buildout

ENV LANG="fr_BE.UTF-8"
ENV LC_CTYPE="fr_BE.UTF-8"
ENV PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages
ENV SMS_CONFIG_PATH=/opt/sms/conf/sms.cfg

CMD ["gammu-smsd", "-c", "/opt/sms/.gammurc"]
