#-*- coding:utf-8 -*-
try:
    import gammu
except:
    raise(ImportError("""gammu library not found, is it installed in your python environnement? Did you export dist-packages ?
        export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages"""))

import ConfigParser
import argparse

class phone_numbers():
    def __init__(self, section, message):
        self.section = section
        self.message = message

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--section', required=True)
    parser.add_argument('-m', '--message', required=True)

    return parser.parse_args()

def main():
    args = get_args()

    config = ConfigParser.RawConfigParser()
    config.read('sms.cfg')

    # Initialisation
    sm = gammu.StateMachine()
    sm.ReadConfig(Filename='/home/jenny/.gammurc')
    sm.Init()

    section = config.items(args.section)
    
    for nom, number in section:
        print(number)
        # Entrer le code PIN si demandé
        if sm.GetSecurityStatus() == 'PIN':
            sm.EnterSecurityCode('PIN', 'XXXX')

        # Données du message
        message = {
            'Text': 'Hello {0}.\n{1}'.format(nom, args.message),
            'SMSC': {'Location': 1},
            'Number': number
        }

        # Envoi du message
        sm.SendSMS(message)
