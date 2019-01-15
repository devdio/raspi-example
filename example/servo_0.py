# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin,50)
p.start(2.5)

try:
    while True:
        print('*** Start *** ')
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(3)

except  KeyboardInterrupt:
        p.stop()

GPIO.cleanup()
