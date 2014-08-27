#-*- coding:utf-8 -*-
import os
import ConfigParser
import argparse
import gammu.smsd
""" les numeros de telephonne et les groupes de numéros se trouve dans fichier
sms.cfg
récupération des informations fournie via terminal
(section = groupe def dans sms.cfg - message = "le message txt") """


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--section', required=True)
    parser.add_argument('-m', '--message', required=True)

    return parser.parse_args()


def message_decomp(message_inject):
    liste = []
    step = 160

    for i in range(0, len(message_inject), 160):
        slice = message_inject[i:step]
        step += 160
        liste.append(slice)
    return liste


def send_sms(section, message_inject, sender=None):

    message_inject = message_inject.decode('utf-8')
    config = ConfigParser.RawConfigParser()
    sms_config_path = os.environ['SMS_CONFIG_PATH']
    config.read(sms_config_path)

    section = config.items(section)
    config_smsd = config.get('options', 'config_smsd')

    smsd = gammu.smsd.SMSD(config_smsd)
    liste_message = message_decomp(message_inject)

    for nom, number in section:

        if sender != number:
            for message in liste_message:
                message_send = {'Text': unicode(message), 'SMSC': {'Location': 1}, 'Number': number}
                smsd.InjectSMS([message_send])


def main():
    args = get_args()
    send_sms(args.section, args.message)
