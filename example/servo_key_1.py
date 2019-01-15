# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
 
pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
 
p = GPIO.PWM(pin, 50) # 50 Hz
p.start(0)
# this values validate only when 50Hz
left_angle = 12.5
center_angle = 7.5
right_angle = 2.5
 
def doAngle(angle):
    p.ChangeDutyCycle(angle)
    print "Angle: %d" % angle
    time.sleep(0.5)
 
try:
 
    while True:
        var = raw_input("Enter L/R/C : ")
        if var == 'R' or var == 'r' :
            print "Right"
            doAngle(right_angle)
        elif var == 'L' or var == 'l':
            print "Left"
            doAngle(left_angle)
        elif var == 'C' or var == 'c':
            print "Center"
            doAngle(center_angle)
except KeyboardInterrupt:
    p.stop()

GPIO.cleanup()
