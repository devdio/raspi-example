# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN)

try:
    while True:
        key_in = GPIO.input(18)
        if key_in == 0:
            print "LOW"
        else:
            print "HIGH"
            pass
        sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()




