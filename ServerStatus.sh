#!/usr/bin/env bash
#Written by: walshie4
#Maintained at https://github.com/walshie4/Geeklets
#Created on 2/2/2014

#UI COLORS
RED=$(tput setaf 1)
YELLOW=$(tput setaf 3)
GREEN=$(tput setaf 2)
RESET=$(tput sgr0)
#END UI COLORS

#Server list config
SERVER='se.rit.edu' #put URL in ''s in this variable 
NUM_PINGS=5 #Set the number of pings to average for each reported time
TIMEBARRIER=500 #time (in ms) you will allow before coloring the time yellow
LOSTBARRIER=10 #Set this to the percent of lost pings you will allow before coloring the percent yellow
#End Config

response=`ping -c $NUM_PINGS $SERVER`
if [[ -n "$response" ]]; then #if response is non-zero (got a response)
    ip=`echo $response | cut -f2 -d '(' | cut -f1 -d ')'` #get the ip
    lost=`echo $response | cut -f1 -d '%' | tail -c 10 | cut -f2 -d ' '` #get the percent of packets lost
    if [ "$lost" = "100.0" ]; then
        echo "$REDAll packets lost when sending to $SERVER$RESET"
        exit 0
    fi
    avgtime=`echo $response | cut -f5 -d '/'` #get the average response time
    if [ $(echo "$avgtime > $TIMEBARRIER" | bc) -ne 0 ]; then
        timeColor=$YELLOW
    else
        timeColor=$GREEN
    fi
    if [ $(echo "$lost > $LOSTBARRIER" | bc) -ne 0 ]; then
        lostColor=$YELLOW
    else
        lostColor=$GREEN
    fi
    echo "The server at $ip ($SERVER) responded in $timeColor$avgtime$RESET ms, and lost $lostColor$lost$RESET% of the packets sent"  #print the info
else
    echo "$REDInvalid hostname or not connected to the internet$RESET" #alert the user of error
fi
