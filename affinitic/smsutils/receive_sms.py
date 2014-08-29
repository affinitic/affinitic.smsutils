#-*- coding:utf-8 -*-
import os

from affinitic.smsutils.send_sms import send_sms


def name_send_sms(number_sms):
    # recovery name person to send sms
    import ConfigParser
    config = ConfigParser.RawConfigParser()
    sms_config_path = os.environ['SMS_CONFIG_PATH']
    config.read(sms_config_path)
    section = config.items('all_num')
    for nom, number in section:
        if number == number_sms:
            return nom
    return number_sms


def main():
    #telephon number to send sms
    number_sms = (os.environ['SMS_1_NUMBER'])
    #number messages receive
    numparts = int(os.environ['SMS_MESSAGES'])
    # Get all text parts
    text = ''
    for i in range(1, numparts + 1):
        varname = 'SMS_%d_TEXT' % i
        if varname in os.environ:
            text = text + os.environ[varname]
    sms_message = name_send_sms(number_sms) + ' dit: ' + text
    send_sms("all_num", sms_message, sender=number_sms)
