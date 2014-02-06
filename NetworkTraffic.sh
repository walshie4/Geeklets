#!/usr/bin/env bash
#Ritten by: walshie4
#Maintained at https://github.com/walshie4/Geeklets
#Created on 2/3/2014
#Network Interface Config
INTERFACE='en0' #run ifconfig and look for the interface with a status marked 'active'
#End Config

response=`netstat -i -b | grep $INTERFACE`
in=$((`echo $response | cut -f7 -d ' '` / 1024)) #divided by number of bytes per megabyte
out=$((`echo $response | cut -f10 -d ' '` / 1024))
in2=$((`echo $response | cut -f7 -d ' '` / 1024)) #divided by number of bytes per megabyte
out2=$((`echo $response | cut -f10 -d ' '` / 1024))
inMB=$(($in / 1024))
outMB=$(($out / 1024))
echo "TX:$outMB MBs  RX:$inMB MBs"
sleep 1
diffIn=$(($in2 - $in))
diffOut=$(($out2 - $out))
echo "TX:$diffOut KB/s  RX:$diffIn KB/s"
