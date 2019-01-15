# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

led_pin = 37;

try:
    pwm = GPIO.PWM(led_pin, 100)
    pwm.start(0)

    for i in range(3):
        for j in range(10):
            pwm.ChangeDutyCycle(j*10)
            sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

