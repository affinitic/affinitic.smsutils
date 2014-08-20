#-*- coding:utf-8 -*-
import ConfigParser
import argparse
import gammu.smsd
""" les numeros de telephonne et les groupes de numéros se trouve dans fichier
sms.cfg
récupération des informations fournie via terminal
(section = groupe def dans sms.cfg - message = "le message txt") """


class phone_numbers():
    def __init__(self, section, message):
        self.section = section
        self.message = message


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--section', required=True)
    parser.add_argument('-m', '--message', required=True)

    return parser.parse_args()


def send_sms(section, message, sender=None):

    config = ConfigParser.RawConfigParser()
    config.read('sms.cfg')
    section = config.items(section)
    nom, number = section[0]

    smsd = gammu.smsd.SMSD('/home/jenny/.gammurc')

    for nom, number in section:
        if sender != number:
            message_send = {'Text': 'Hello {0}.\n{1}'.format(nom, message), 'SMSC': {'Location': 1}, 'Number': number}
            smsd.InjectSMS([message_send])


def main():
    args = get_args()
    send_sms(args.section, args.message)
