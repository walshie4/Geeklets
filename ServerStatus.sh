#!/usr/bin/env bash
#Written by: walshie4
#Maintained at https://github.com/walshie4/Geeklets
#Created on 2/2/2014
#Server list config
SERVER='www.something.com' #put URL in ''s in this variable 
#End config

response=`ping -c 1 $SERVER`
ip=`echo $response | cut -f2 -d '(' | cut -f1 -d ')'`
time=`echo $response | cut -f4 -d '=' | cut -f1 -d ' '`
echo "The server at $ip ($SERVER) responded in $time ms."
