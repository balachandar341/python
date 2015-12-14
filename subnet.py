#!/usr/bin/env python
import os
import sys
import subprocess
import csv

former, sys.stdout = sys.stdout, open('o.csv', 'w')

hostname = sys.argv[1]
#hostname=raw_input("Enter the Host ID or Host Name here : ")
#hostname = "10.0.2.15" #example
print (riesponse = os.system("fping -g "+hostname))
#print response

results,sys.stdout = sys.stdout, former
results.close()
#and then check the response...
#if a == 0:
#if hostname == 0:
 # print hostname, 'is up!'
#else:
 # print hostname, 'is down!'

#This is used to findout all ip's under subnet
