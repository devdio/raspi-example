# -*- coding: utf-8 -*-
import smbus
from time import sleep

bus = smbus.SMBus(1)
#bus = SMBus(0) 

print("Read the A/D")

bus.write_byte(0x48, 0)
last_reading = -1

while True:
    reading = bus.read_byte(0x48)
    if(abs(last_reading - reading) > 2):
        print(reading)
        last_reading = reading

    sleep(0.5)
