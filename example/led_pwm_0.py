# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

led_pin = 37;

#ref : https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
try:
    pwm = GPIO.PWM(led_pin, 100)    #PWM(channel, frequency)
    pwm.start(0)    # where dc is the duty cycle (0.0 <= dc <= 100.0)

    for i in range(3):
        for j in range(10):
            pwm.ChangeDutyCycle(j*10)    # where 0.0 <= dc <= 100.0
            sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

