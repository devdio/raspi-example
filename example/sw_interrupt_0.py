# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

def my_callback(channel):
    print "***callback***"
    GPIO.output(37, GPIO.HIGH)
    sleep(1)
    GPIO.output(37, GPIO.LOW)

GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback, 
	                                    bouncetime=300)
try:
    while True:
        print "***wating***"
        sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()


