#!/usr/bin/python

import Adafruit_DHT
import time
sensor = Adafruit_DHT.DHT22

pin =17 
while(1):
 
 humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

 if humidity is not None and temperature is not None:
	print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
 else:
	print 'Failed to get reading. Try again!'
 time.sleep(1)

