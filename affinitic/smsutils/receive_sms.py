#!/usr/bin/python
#-*- coding:utf-8 -*-
import os

from affinitic.smsutils.send_sms import send_sms
#import sys


#numparts = int(os.environ['DECODED_PARTS'])


# Are there any decoded parts?


def main():
    #donnée recup du os.environ
    sms_receive = (os.environ['SMS_1_TEXT'])
    number_send_sms = (os.environ['SMS_1_NUMBER'])

    sms_message = number_send_sms + ' a envoyer un sms: ' + sms_receive

    send_sms("all_num", sms_message)
