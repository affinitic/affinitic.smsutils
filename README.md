affinitic.smsutils
==================

Allow to send sms with 3G key


Warning
-------

This package use a python library (gammu) that will be installed in your dist-packages synaptic. You need your virtualenv python to know about that library. For this, edit your PYTHONPATH envar.

PYTHONPATH=/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages


The user that execute the script also need to be in the group 'dialout' to access the USB 3G key

sudo adduser $USER dialout

This need the user to reconnect his session.


Installation
------------

git clone
make install


Uninstall
---------

make uninstall


Usage
-----

bin/send_sms
