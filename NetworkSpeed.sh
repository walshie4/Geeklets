#!/bin/sh
# created by chris helming.
# chris dot helming at gmail

# 2014-02-02
# Rubén Varela
# Found this script at, http://hints.macworld.com/article.php?story=20090326125916351
# Tested the script and while it works, the adapter needs to be changed manually in the
# script. Some code will be added to accept an argument and use en0 if the
# argument isn't present.

#DEFAULT_ADAPTER="enX"

usage() {
  echo " Usage: ./NetworkSpeed.sh arg1 "
  echo " arg1 can be either a network interface or --help."
  echo " Passing another value will be interpreted as being the "
  echo " network interface to be used."
  echo ""
  echo " If --help is used, or no argument is present, "
  echo "you will be presented with this text."
  echo ""
  echo " A default value may be configured in the script."
  echo " You need to edit it and set the variable DEFAULT_ADAPTER "
  echo " to the desired value."
  echo ""
  echo " Example usage:"
  echo " ./NetworkSpeed.sh en0"
  echo " In this example, the network interface en0 will be measured."
}

if [ ! -z $1 ]; then
  if [ $1 = "--help" ]; then
    usage;
    exit 1;
  else
    ADAPTER="$1"
  fi
else
  if [ ! -z $DEFAULT_ADAPTER ]; then
    ADAPTER=$DEFAULT_ADAPTER
  else
    usage;
    exit 1;
  fi
fi

# get the current number of bytes in and bytes out
myvar1=`netstat -ib | grep -e $ADAPTER -m 1 | awk '{print $7}'` # bytes in
myvar3=`netstat -ib | grep -e $ADAPTER -m 1 | awk '{print $10}'` # bytes out

#wait one second
sleep 1

# get the number of bytes in and out one second later
myvar2=`netstat -ib | grep -e $ADAPTER -m 1 | awk '{print $7}'` # bytes in again
myvar4=`netstat -ib | grep -e $ADAPTER -m 1 | awk '{print $10}'` # bytes out again

# find the difference between bytes in and out during that one second
subin=$(($myvar2 - $myvar1))
subout=$(($myvar4 - $myvar3))

# convert bytes to kilobytes
kbin=`echo "scale=2; $subin/1024;" | bc`
kbout=`echo "scale=2; $subout/1024;" | bc`

# print the results
echo "in: $kbin Kb/sec"
echo "out: $kbout Kb/sec"