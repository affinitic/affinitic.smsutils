#-*- coding:utf-8 -*-
import os

from affinitic.smsutils.send_sms import send_sms
#import sys


#numparts = int(os.environ['DECODED_PARTS'])


# Are there any decoded parts?
def name_send_sms(number_sms):
    import ConfigParser
    config = ConfigParser.RawConfigParser()
    config.read('sms.cfg')
    section = config.items('all_num')
    for nom, number in section:
        if number == number_sms:
            print nom
            return nom
    return number_sms


def main():
    #donnée recup du os.environ
    sms_receive = (os.environ['SMS_1_TEXT'])
    number_sms = (os.environ['SMS_1_NUMBER'])
    sms_message = name_send_sms(number_sms) + ' a envoyé un sms: ' + sms_receive
    send_sms("all_num", sms_message, sender=number_sms)
