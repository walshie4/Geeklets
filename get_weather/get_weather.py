#!/usr/bin/env python

# Rubén Varela
# 2013-08-10
# Get the weather from Yahoo.

import feedparser
import pprint
import urllib2

result = feedparser.parse('http://weather.yahooapis.com/forecastrss?w=160991&u=f')
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(result)

# Temperature
degree_sign= u'\N{DEGREE SIGN}'
temp = result['feed']['yweather_wind']['chill'] #+ degree_sign + " F"

# Wind 
wspeed = result['feed']['yweather_wind']['speed'] + " MPH" 

# Wind Direction
direction = float(result['feed']['yweather_wind']['direction'])

if direction > 348.75 or direction <= 11.25:
  wdir = "N"
elif direction > 11.25 and direction <= 33.75:
  wdir = "NNE"
elif direction > 33.75 and direction <= 56.25:
  wdir = "NE"
elif direction > 56.25 and direction <= 78.75:
  wdir = "ENE"
elif direction > 78.75 and direction <= 101.25:
  wdir = "E"
elif direction > 101.25 and direction <= 123.75:
  wdir = "ESE"
elif direction > 123.75 and direction <= 146.25:
  wdir = "SE"
elif direction > 146.25 and direction <= 168.75:
  wdir = "SSE"
elif direction > 168.75 and direction <= 191.25:
  wdir = "S"
elif direction > 191.25 and direction <= 213.75:
  wdir = "SSW"
elif direction > 213.75 and direction <= 236.25:
  wdir = "SW"
elif direction > 236.25 and direction <= 258.75:
  wdir = "WSW"
elif direction > 258.75 and direction <= 281.25:
  wdir = "W"
elif direction > 281.25 and direction <= 303.75:
  wdir = "WNW"
elif direction > 303.75 and direction <= 326.25:
  wdir = "NW"
elif direction > 326.25 and direction <= 348.75:
  wdir = "NNW"

#Visibility
visibility = result['feed']['yweather_atmosphere']['visibility']
visibility = visibility + " Mi"

#Conditions
conditions = result['entries'][0]['yweather_condition']['text']
image = 'http://l.yimg.com/a/i/us/we/52/' + result['entries'][0]['yweather_condition']['code'] + '.gif'
# print conditions
# print image

temp.encode('utf-8')

# temp
# wspeed
# wdir
# visibility
# conditions
# image



f = open('temp', 'r+')
f.truncate()
f.write(temp)
f.close()

f = open('wspeed', 'r+')
f.truncate()
f.write(wspeed)
f.close()

f = open('wdir', 'r+')
f.truncate()
f.write(wdir)
f.close()

f = open('visibility', 'r+')
f.truncate()
f.write(visibility)
f.close()

f = open('conditions', 'r+')
f.truncate()
f.write(conditions)
f.close()

image_content = urllib2.urlopen(image)
f = open('image', 'r+')
f.truncate()
f.write(image_content.read())
f.close()