# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0

try:
    while True:
        key_in = GPIO.input(18)
        if key_in == 0:
            print "SW ON"
            count += 1
            print("Count = %d"%count)

        sleep(0.5)

except KeyboardInterrupt:
    print "Ctrl-C..."

GPIO.cleanup()


