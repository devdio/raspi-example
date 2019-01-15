# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

try:
	while True:
	    GPIO.output(11, GPIO.HIGH)
	    sleep(1)
	    GPIO.output(11, GPIO.LOW)
	    GPIO.output(13, GPIO.HIGH)
	    sleep(1)
	    GPIO.output(13, GPIO.LOW)
	    GPIO.output(15, GPIO.HIGH)
	    sleep(1)
	    GPIO.output(15, GPIO.LOW)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()    

