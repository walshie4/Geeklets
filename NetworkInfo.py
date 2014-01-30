#!/usr/bin/python
#Created on: 1/29/2014
#Maintained @ 'https://github.com/walshie4/Geeklets'
#A geeklet to display LAN IP, WAN IP, and Estimated Geolocation

#This script requires the requests library
#For install instructions go to 'http://docs.python-requests.org/en/latest/user/install/#install'
#It is awesome and you should have it
from __future__ import print_function
import requests
import socket

__author__ = "walshie4"


url = 'http://wtfismyip.com/json'

def getWANIPInfo():
    return requests.get(url).json()

def getLANIPInfo(): #note on some machines this may return 127.0.0.1 on some systems (because of hosts file)
    return socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':
    print('LAN IP:\t',getLANIPInfo())
    wanInfo = getWANIPInfo()
    print('WAN IP:\t',wanInfo['YourFuckingIPAddress']) #pardon the language, not my names
    print('IP Location:',wanInfo['YourFuckingLocation'])
