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

Install zmq

    sudo apt-get install libzmq3-dev

... or

    brew install zeromq

... or

    wget http://download.zeromq.org/zeromq-4.0.4.tar.gz
    tar -xvf zeromq-4.0.4.tar.gz
    cd zeromq-4.0.4/
    ./configure
    make
    sudo make install
    sudo ldconfig
    cd ..
    rm -rf zeromq-4.0.4.tar.gz zeromq-4.0.4/

Zmq python library will need python-dev

    sudo apt-get install python-dev

Add this line to your .bashrc / .zshrc this will allow virtuaenv to use dist-packages

    export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages
    
Add this line to your .bashrc / .zshrc this allow python script to access configuration file. See the sms.cfg_example for the syntax

    export SMS_CONFIG_PATH=/home/<user>/buildout/affinitic.smsutils/sms.cfg

Then do

    git clone
    make install
You have to disconnect current user because we added it to some groups


Uninstall
---------

    make uninstall


Other configuration
-------------------

Gammu smsd daemon use a gammurc file specified when launching the daemon. You can see the gammurc_example file for an example of configuration.

If you want to set smsd daemon to launch at startup, see the service_example file.


Usage
-----

Launch daemon

    gammu-smsd -c '/home/<user>/.gammurc'

Send sms:

    bin/send_sms
