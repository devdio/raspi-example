# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

pin_trigger = 7
pin_echo = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_trigger, GPIO.OUT)
GPIO.setup(pin_echo, GPIO.IN)
GPIO.output(pin_trigger, GPIO.LOW)

try:
    print "Waiting for sensor to settle"
    time.sleep(2)

    print "Calculating distance"
    GPIO.output(pin_trigger, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(pin_trigger, GPIO.LOW)

    while GPIO.input(pin_echo)==0:
        pulse_start_time = time.time()

    while GPIO.input(pin_echo)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print "Distance:",distance,"cm"

finally:
      GPIO.cleanup()

