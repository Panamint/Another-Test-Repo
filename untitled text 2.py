#Interface to the Elecraft KX3
#Paul Gacek March 17, 2013
# KX3 cable USB device is /dev/tty.usbserial-AE016TD1

import serial
ser = serial.Serial('/dev/tty.usbserial-AE016TD1', 38400, timeout=1)

ser.write('FA00014069022;')
ser.write('FA;')
ser.write('MD $6;')
freq = ser.readline()
print freq