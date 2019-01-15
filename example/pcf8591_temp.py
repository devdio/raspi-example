# -*- coding: utf-8 -*-
import smbus
import time

address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)

try:
	while True:
	    bus.write_byte(address,A0)
	    value = bus.read_byte(address)
	    aout = value*3.3/255
	    print("AOUT:%1.3f  TEMP:%d" %(aout, aout*100))
	    time.sleep(0.5)

except KeyboardInterrupt:
    pass




