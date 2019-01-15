# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)

for k in range(10):
    GPIO.output(11, GPIO.HIGH)
    sleep(1)
    GPIO.output(11, GPIO.LOW)
    sleep(1)
    print '%d times'%k

GPIO.cleanup()
