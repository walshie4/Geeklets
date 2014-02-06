#!/usr/bin/env bash
#Ritten by: walshie4
#Maintained at https://github.com/walshie4/Geeklets
#Created on 2/3/2014

#UI COLORS
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
RESET=$(tput sgr0)
#END UI COLORS

#Network Interface Config
INTERFACE='en0' #run ifconfig and look for the interface with a status marked 'active'
#End Config

response=`netstat -ib | grep $INTERFACE`
in=$((`echo $response | cut -f7 -d ' '`)) #divided by number of bytes per megabyte
out=$((`echo $response | cut -f10 -d ' '`))
sleep 1
response=`netstat -ib | grep $INTERFACE` 
in2=$((`echo $response | cut -f7 -d ' '`)) #divided by number of bytes per megabyte
out2=$((`echo $response | cut -f10 -d ' '`))
inMB=$(($in / 1048576))
outMB=$(($out / 1048576))
echo "TX:$RED$outMB$RESET MBs  RX:$GREEN$inMB$RESET MBs"
diffIn=$((($in2 - $in) / 1024))
diffOut=$((($out2 - $out) / 1024))
echo "TX:$RED$diffOut$RESET MBs/s  RX:$GREEN$diffIn$RESET MBs/s"
