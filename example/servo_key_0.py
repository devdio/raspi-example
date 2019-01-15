# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin,50)
p.start(5)

var = 1
try:
    while True:
        angle = raw_input("Enter Angle(0~180)")
        duty = float(angle)/10.0 + 2.5
        p.ChangeDutyCycle(duty)
        time.sleep(0.5)

except KeyboardInterrupt:
	pass

GPIO.cleanup()