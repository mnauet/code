
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM  )    # set gpio pin mode
GPIO.setup(23, GPIO.OUT)    # set pin 23 as output
#GPIO.output(23, GPIO.HIGH)
#GPIO.output(23, GPIO.LOW)

print("Please enter 0 to exit")
num = input("please enter a digit to flash LED")
while num >0:
    num -= 1   
    if num >0:
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.5)
    else:
        print("Please enter 0 to exit")
        num = input("please enter a digit to flash LED again................")