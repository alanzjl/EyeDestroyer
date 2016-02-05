#!/bin/python2.7

#####################################
#                                   #
#       Written By Alanzjl          #
#           www.alanzjl.com         #
#                                   #
#####################################

import string
import os
import time

max_b = 1808
min_b = 0

def light(t):
    if t<min_b:
        t=min_b
    if t>max_b:
        t=max_b
    command = "sudo echo " + "%i"%t + " > /sys/class/backlight/intel_backlight/brightness"
    os.popen(command)

# STORY BRGINS
time.sleep(2)
print "This is an ancient legend...."
time.sleep(2)
print "Long long ago, there was no light..."
time.sleep(0.5)
light(50);
time.sleep(1)
print "HEAR !! WHAT'S THAT ?!!!"
time.sleep(1)
light(300)
time.sleep(1)
print "CAN YOU HEAR ME??"
time.sleep(2)
print "OH CAN YOU SEE ME???"
light(500)
time.sleep(1.5)
print "AHAHAHAHA YOU CAN SEE ME NOW!!"
light(max_b)
time.sleep(1)
print "AND YOU CAN SEE ME CLEARLY!!!!"

for i in range(1,5):
    light(400)
    time.sleep(1)
    light(max_b-200)
    time.sleep(1)

print "WELL, Are you OK?"
time.sleep(1)
print "I'm alanzjl, welcome to www.alanzjl.com"
