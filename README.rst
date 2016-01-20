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
Do

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


Credits
-------

This package was developed by `Affinitic team <https://github.com/affinitic>`_.

.. image:: http://www.affinitic.be/affinitic_logo.png
   :alt: Affinitic website
   :target: http://www.affinitic.be

``affinitic.smsutils`` is licensed under GNU General Public License, version 2.

