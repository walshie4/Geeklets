#!/usr/bin/env bash

# Rubén Varela
# 2013-01-27
# Really simple script to print the SSID you're connected to.

ssid_without_leading_space=`/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -I | sed '/ SSID: /!d; s/^.* SSID: //'`
echo "SSID: $ssid_without_leading_space"
