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

Add this line to your .bashrc / .zshrc this will allow virtuaenv to use dist-packages
    export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages

    git clone
    make install
You have to disconnect current user because we added it to some groups

Uninstall
---------

    make uninstall


Usage
-----

Launch daemon

    sudo gammu-smsd -c '/home/<user>/.gammurc'

Send sms:

    bin/send_sms
