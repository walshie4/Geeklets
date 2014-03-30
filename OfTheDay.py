#!/usr/bin/env python
#A simple script that prints the letter or whatever of the day (randomly)
#Written by: Adam Walsh (adamwalsh14@gmail.com)
#Maintained @ https://github.com/walshie4/Geeklets

from __future__ import print_function
import random

#CONFIG
NUMBER = True
#END CONFIG

numbers = range(-200,201) #all integers [-200, 200]

if NUMBER:
    print("The number of the day is:", numbers[int(random.random()*len(numbers))])
else:
    print('No data sources enabled in config')
