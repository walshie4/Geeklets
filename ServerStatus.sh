#!/usr/bin/env bash
#Written by: walshie4
#Maintained at https://github.com/walshie4/Geeklets
#Created on 2/2/2014
#Server list config
SERVER='se.rit.edu' #put URL in ''s in this variable 
NUM_PINGS=5 #Set the number of pings to average for each reported time
#End Config

response=`ping -c $NUM_PINGS $SERVER`
if [[ -n "$response" ]]; then #if response is non-zero (got a response)
    ip=`echo $response | cut -f2 -d '(' | cut -f1 -d ')'` #get the ip
    lost=`echo $response | cut -f1 -d '%' | tail -c 10 | cut -f2 -d ' '` #get the percent of packets lost
    if [ "$lost" = "100.0" ]; then
        echo "All packets lost when sending to $SERVER"
        exit 0
    fi
    avgtime=`echo $response | cut -f5 -d '/'` #get the average response time
    echo "The server at $ip ($SERVER) responded in $avgtime ms, and lost $lost% of the packets sent"  #print the info
else
    echo "Invalid hostname or not connected to the internet" #alert the user of error
fi
