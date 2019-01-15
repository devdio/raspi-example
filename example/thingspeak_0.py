# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
# change pin 4
instance = dht11.DHT11(pin=4)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        time.sleep(1)

        url = "https://api.thingspeak.com/update?api_key=VW9WLRBTEKG18262"
        url = url + "&field1=" + str(result.temperature)
        url = url + "&field2=" + str(result.humidity)
        html = urllib2.urlopen(url)

    time.sleep(1)
