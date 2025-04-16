#!/usr/bin/env python3
# First example of pinging from Python
# By 


import os

#Assign Ip to a variable
ip_address = "127.0.0.1"
#Build a ping command
ping_cmd= "ping -c 1 -w 1 {0}".format(ip_address) 
#Build Execute
exit_code = os.system(ping_cmd)
#Print out results
print(exit_code)
