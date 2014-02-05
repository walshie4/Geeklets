#!/usr/bin/env bash

# 2014-02-02
# Rubén Varela
# Created this script in order to be able to draw completion bars more easily.
# A use I have for this is to display in a visual way the amount of drive 
#  space I have used and have free. 

LEFT_SIDE="\xe2\x9d\xb2"
RIGHT_SIDE="\xe2\x9d\xb3"
FILLED_SPACE="\xe2\x96\xac"

usage () {
  echo " Usage: ./used_percent_bar.sh num1 [num2]"
  echo " [num1] is the percent used. This value is required."
  echo " [num2] is the length in characters you'd like the bar to be. "
  echo " If not provided, the default value will be 10."
  echo ""
  echo " Example:"
  echo " In this example, a bar of length 10 (the default value) will be "
  echo " drawn with 10 percent of it marked as used."
  echo " ./used_percent_bar.sh 10"
  echo ""
  echo " In this example, a bar of length 20 will be drawn with 10 percent"
  echo " of it marked as used."
  echo " ./used_percent_bar.sh 10 20"
}

#Is the argument for the percent used provided?
#Exit if not.
if [ ! -z "$1" ]; then
  USED="$1"
else
  usage
  exit
fi

#Is the length of the bar provided?
# Use a default value if not.
if [ ! -z "$2" ]; then
  LENGTH=$2
else
  LENGTH=10
fi

#Calculate
used_space=$(printf %.0f $(echo "scale=4; $USED/100*$LENGTH" | bc))
#echo $used_space;

#Print
echo -n -e "$LEFT_SIDE"

for i in $(eval echo "{1..$LENGTH}"); do
if [ $i -le $used_space ]; then
echo -n -e "$FILLED_SPACE"
  else
echo -n ' '
  fi
done

echo -e ''$RIGHT_SIDE