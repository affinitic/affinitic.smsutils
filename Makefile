install:
	sudo apt-get install gammu gammu-smsd python-gammu
	virtualenv -p python2.7 .
	bin/python bootstrap.py
	bin/buildout
	sudo adduser $(USER) dialout
	sudo adduser $(USER) gammu
	sudo adduser $(USER) tty

uninstall:
	sudo apt-get remove gammu gammu-smsd python-gammu
	rm -rf affinitic.smsutils.egg-info bin develop-eggs eggs include lib local parts .installed.cfg
	sudo deluser $(USER) dialout
	sudo deluser $(USER) gammu
	sudo deluser $(USER) tty
