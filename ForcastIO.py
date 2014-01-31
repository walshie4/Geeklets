#!/usr/bin/python
#Created on 1/30/2014
#Maintained @ 'https://github.com/walshie4/Geeklets'

#This script requires the requests library
#For install instructions go to 'http://docs.python-requests.org/en/latest/user/install/#install'
#It is awesome and you should have it

from __future__ import print_function
from __future__ import division
import requests
import time
import math

#TO DO: (in order of priority)
# Add support for changing units

__author__ = 'walshie4'

APIKEY = '7f19527c0c30f3b733c91beb3a393937' #ENTER YOUR OWN API KEY IN THE ''. Get one from https://developer.forecast.io/
LAT = '43.0848' #ENTER LATITUDE YOU WOULD LIKE WEATHER INFO ON
LONG = '-77.6744' #ENTER LONGITUDE YOU WOULD LIKE WEATHER INFO ON
LOCATIONLABEL = 'Rochester, NY' #ENTER THE NAME FOR THIS LOCATION
HOURLYINFOTOREPORT = {1, 2, 3} #ENTER INDEX FOR HOURLY DATA TO REPORT For example: 1 will have the first hourly weather info printed
                                                                                    #         2 will have the second...etc.
#CONFIG SECTION If you don't want one of these to show set it to false
TEMP = True
STATUS = True
DEWPOINT = True
HUMIDITY = True
WINDSPEED = True
WINDBEARING = True
OZONE = True
CLOUDCOVER = True
MILTIME = False
#END CONFIG

def getWeatherInfo(): #This can be used up to 1000 times a day before costing money (see forcast.io API info)
    return requests.get(getAPIURL(APIKEY, LAT, LONG)).json()#This means the max refresh rate you should have is once every ~86.5 seconds

def getAPIURL(key, latitude, longitude):
    base = 'https://api.forecast.io/forecast/'
    return base + APIKEY + '/' + latitude + ',' + longitude + '/'

def printWeatherInfo(json):
    if TEMP:
        print('\tTemp:\t\t' + str(json['temperature']) + '*F')
    if STATUS:
        print('\tStatus:\t\t' + str(json['summary']))
    if DEWPOINT:
        print('\tDew Point:\t\t' + str(json['dewPoint']) + '*F')
    if HUMIDITY:
        print('\tHumidity:\t\t' + str(json['humidity']) + '%')
    if WINDSPEED:
        print('\tWind Speed:\t' + str(json['windSpeed']) + 'MPH')
    if WINDBEARING:
        print('\tWind Bearing:\t' + str(json['windBearing']) + '*')
    if OZONE:
        print('\tOzone:\t\t' + str(float(json['ozone'])) + ' Dobsons')#http://ozonewatch.gsfc.nasa.gov/facts/dobson.html
    if CLOUDCOVER:
        print('\t' + str(float(json['cloudCover']) * 100) + '% of the sky is covered with clouds')
    print()

def printHourlyInfo(data, time, hoursToPrint, timeZone):
    for hour in hoursToPrint:
        hourInfo = data[hour]
        hourTime = hourInfo['time']
        print('Weather for ' + LOCATIONLABEL + ' at ' + str(formatTime(time, hourTime, timeZone)))
        printWeatherInfo(hourInfo)

def formatTime(time, futureTime, timeZone):
    dif = futureTime - time
    currentHour = ((time % 86400) // 3600) + timeZone
    futureHour = ((futureTime % 86400) // 3600) + timeZone
    if futureHour < 0:
        futureHour += 24
    unit = 'AM'
    if futureHour > 12:
        unit = 'PM'
    if not MILTIME:
        futureHour %= 12 #cut day in two, leave remainder
        return str(futureHour) + ':00' + unit
    return str(futureHour) + ':00'

if __name__ == '__main__':
    print('Current Weather for ' + LOCATIONLABEL)
    json = getWeatherInfo() #IF YOU ARE GETTING AN ERROR HERE IT IS MOST LIKELY FROM AN INCORRECT API KEY OR API REQUEST OVERLOAD
    timeZone = json['offset']
    current = json['currently']
    printWeatherInfo(current)
    hourlyData = json['hourly']['data']
    time = time.time()
    printHourlyInfo(hourlyData, time, HOURLYINFOTOREPORT, timeZone)
