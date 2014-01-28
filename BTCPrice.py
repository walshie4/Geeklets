#!/usr/bin/python
#Created on 1/28/2014
#Maintained @ 'https://github.com/walshie4/Geeklets'

#This script requires the requests library
#For install instructions go to 'http://docs.python-requests.org/en/latest/user/install/#install'
#It is awesome and you should have it

from __future__ import print_function
import requests

__author__='walshie4'

ticker='https://www.bitstamp.net/api/ticker/'

def getCurrentInfo():
    try:
        return requests.get(ticker).json()
    except Error:
        return {'Error' : 'Error'}


if __name__=='__main__':
    json = getCurrentInfo()
    if 'Error' in json:
        print('An Error occured. Check internet connection.')
    else:
        print('Current Price:$',json['last'])
        print('24H High:\t\t$',json['high'])
        print('24H Low:\t\t$',json['low'])
        print('24H Volume:',json['volume'])
