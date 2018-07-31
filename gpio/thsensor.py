import sys
import Adafruit_DHT as ada
import time

while True:
	h, t = ada.read_retry(11,4)
	print 'hallo'
	#print 'Temp: {0:0.1f} C Humidity: {1:0.af} %'.format(t,h)
	time.sleep(1)
 
