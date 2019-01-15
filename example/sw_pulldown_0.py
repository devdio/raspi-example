# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        key_in = GPIO.input(18)
        if key_in == 0:
            print "LED ON"
            GPIO.output(37, GPIO.HIGH)
        else:
            print "LED OFF"
            GPIO.output(37, GPIO.LOW)
        sleep(0.5)

except KeyboardInterrupt:
    pass
finally
    GPIO.cleanup()




