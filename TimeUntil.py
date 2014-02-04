#!/usr/bin/python
#Created on 2/3/2014
#Maintained @ 'https://github.com/walshie4/Geeklets'

#Prints the time until an event

from __future__ import print_function
import time

__author__='walshie4'

YEAR = 2014
MONTH = 5
DAY = 19
HOUR = 0
MIN = 0
SEC = 0

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysInMonthLY = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getTimeUntil(event): #must be in secs
    current = time.time()
    return event - current

def computeUnixTime(day, month, year, hour, mins, sec):
    if year < 1970:
        print('Unix time started in 1970 D: Please choose a date before then')
        return -1
    time = (day-1) * 86400 #start with the completed days this month
    for y in range(1970, year): #for each year from 1970
        for m in range(12): #for each month
            if (y+1970) % 4 == 0: #if a leap year
                time += daysInMonthLY[m] * 86400
            else:                                   #add days according the number of days in month
                time += daysInMonth[m] * 86400
    for m in range(month - 1): #account for complete months so far this year
        if year % 4 == 0:
            time += daysInMonthLY[m] * 86400
        else:                       #add days for months this year
            time += daysInMonth[m] * 86400
    return time + (hour * 3600) + (mins * 60) + sec #return time with hours, mins, secs added

def convertToTimeUnits(secs):#returns a tuple in order (days, hours, mins, secs)
    if secs > 86400: #at least one day
        days = secs // 86400
        leftover = secs % 86400
        return tuple(map(sum, zip((days,0,0,0), convertToTimeUnits(leftover))))
    elif secs > 3600: #more than an hour
        hours = secs // 3600
        leftover = secs % 3600
        return tuple(map(sum, zip((0,hours,0,0), convertToTimeUnits(leftover))))
    elif secs > 60: #more than a min
        mins = secs // 60
        seconds = secs % 60
        return (0,0,mins,seconds)
    else: #less than a min
        return (0,0,0,secs)

if __name__=="__main__":
    event = computeUnixTime(DAY, MONTH, YEAR, HOUR, MIN, SEC)
    timeUntil = getTimeUntil(event)
    timeTo = convertToTimeUnits(timeUntil)
    print('There are ' + str(timeTo[0]) + ' days, ' + str(timeTo[1]) + ' hours, ' + str(timeTo[2]) + ' minutes, and ' + str(round(timeTo[3], 2))
            + ' seconds until ' + str(MONTH) + '/' + str(DAY) + '/' + str(YEAR) + ' @ ' + str(HOUR) + ':' + str(MIN) + ':' + str(SEC))
