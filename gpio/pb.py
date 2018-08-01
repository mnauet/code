import sys 
import RPi.GPIO as GPIO

BtnPin = 12
LedPin = 23#16
Led_status = 0

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LedPin, GPIO.OUT)
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down= GPIO.PUD_UP)
	GPIO.output(LedPin, Led_status)
	print "LED: on" if Led_status else "LED: off"
	
def swLed(ev=None):
	global Led_status
	Led_status = not Led_status
	GPIO.output(LedPin, Led_status)
	if Led_status == 1:
		print 'led on......'
	else:
		print '........led off'

def loop():
	GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback =swLed, bouncetime=200)
	while True:
		pass

def destroy():
	GPIO.output(LedPin, GPIO.LOW) # led off
	GPIO.cleanup()

if __name__=='__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
