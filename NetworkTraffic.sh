#!/usr/bin/env bash
#Ritten by: walshie4
#Maintained at https://github.com/walshie4/Geeklets
#Created on 2/3/2014
#Network Interface Config
INTERFACE='en0' #run ifconfig and look for the interface with a status marked 'active'
#End Config

response=`netstat -i -b | grep $INTERFACE`
in=$((`echo $response | cut -f7 -d ' '` / 1048576)) #divided by number of bytes per megabyte
out=$((`echo $response | cut -f10 -d ' '` / 1048576))
echo "TX:$out MBs  RX:$in MBs"
