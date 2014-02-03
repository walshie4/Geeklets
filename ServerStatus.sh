#!/usr/bin/env bash
#Written by: walshie4
#Maintained at https://github.com/walshie4/Geeklets
#Created on 2/2/2014
#Server list config
SERVER='www.rit.edu' #put URL in ''s in this variable 
#End config

response=`ping -c 1 $SERVER`
if [[ -n "$response" ]]; then #if response is non-zero (got a response)
    ip=`echo $response | cut -f2 -d '(' | cut -f1 -d ')'` #get the ip
    time=`echo $response | cut -f4 -d '=' | cut -f1 -d ' '` #get the response time
    lost=`echo $response | cut -f1 -d '%' | tail -c 10 | cut -f2 -d ' '` #get the percent of packets lost
    echo "The server at $ip ($SERVER) responded in $time ms, and lost $lost% of the packets sent"  #print the info
else
    echo "Invalid hostname or not connected to the internet" #alert the user of error
fi
