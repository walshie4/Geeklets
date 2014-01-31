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
# Add config section

__author__ = 'walshie4'

APIKEY = '2593824e7869f8849843a77521464d82' #ENTER YOUR OWN API KEY IN THE ''. Get one from https://developer.forecast.io/
LAT = '43.0848' #ENTER LATITUDE YOU WOULD LIKE WEATHER INFO ON
LONG = '-77.6744' #ENTER LONGITUDE YOU WOULD LIKE WEATHER INFO ON
LOCATIONLABEL = 'Rochester, NY' #ENTER THE NAME FOR THIS LOCATION
HOURLYINFOTOREPORT = {1, 2, 3, 5, 10, 20} #ENTER INDEX FOR HOURLY DATA TO REPORT For example: 1 will have the first hourly weather info printed
                                                                                    #         2 will have the second...etc.

def getWeatherInfo(): #This can be used up to 1000 times a day before costing money (see forcast.io API info)
    return requests.get(getAPIURL(APIKEY, LAT, LONG)).json()#This means the max refresh rate you should have is once every ~86.5 seconds

def getAPIURL(key, latitude, longitude):
    base = 'https://api.forecast.io/forecast/'
    return base + APIKEY + '/' + latitude + ',' + longitude + '/'

def printWeatherInfo(json):
    print('\tTemp:\t\t' + str(json['temperature']) + '*F')
    print('\tStatus:\t\t' + str(json['summary']))
    print('\tDew Point:\t' + str(json['dewPoint']) + '*F')
    print('\tHumidity:\t' + str(json['humidity']) + '%')
    print('\tWind Speed:\t' + str(json['windSpeed']) + 'MPH')
    print('\tWind Bearing:\t' + str(json['windBearing']) + '*')
    print('\tOzone:\t\t' + str(float(json['ozone'])) + ' Dobsons')#http://ozonewatch.gsfc.nasa.gov/facts/dobson.html
    print('\t' + str(float(json['cloudCover']) * 100) + '% of the sky is covered with clouds')

def printHourlyInfo(data, time, hoursToPrint):
    for hour in hoursToPrint:
        hourInfo = data[hour]
        hourTime = hourInfo['time']
        print('Weather for ' + LOCATIONLABEL + ' in ' + str(formatTime(time, hourTime)))
        printWeatherInfo(hourInfo)

def formatTime(time, futureTime):
    dif = futureTime - time
    difMin = dif / 60
    if difMin > 60:
        hours = difMin // 60
        difMin %= 60
        return (str(hours) + ' hours and ' + str(round(difMin, 2)) + ' minutes.')
    return (str(round(difMin, 2)) + ' minutes.')

if __name__ == '__main__':
    print('Current Weather for ' + LOCATIONLABEL)
    json = getWeatherInfo()
    current = json['currently']
    printWeatherInfo(current)
    hourlyData = json['hourly']['data']
    time = time.time()
    printHourlyInfo(hourlyData, time, {1,2,4,6,12,24,48})
