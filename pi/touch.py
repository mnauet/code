import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

padPin = 22
GPIO.setup(padPin, GPIO.IN)
num =0
while True:
	padPressed = GPIO.input(padPin)
	if padPressed:
		print "pressed times :", num
		num +=1
	time.sleep(0.1)
