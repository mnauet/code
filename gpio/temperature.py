#Drive 16x2 LCD screen for Raspberry Pi

import dht11
import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping
#LCD_RS = 7
#LCD_E  = 8
#LCD_D4 = 25
#LCD_D5 = 24
#LCD_D6 = 23
#LCD_D7 = 18
Temp_sensor= 4 #14

# Define some device constants
#LCD_WIDTH = 16    # Maximum characters per line
#LCD_CHR = True
#LCD_CMD = False

#LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
#LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
#E_PULSE = 0.0005
#E_DELAY = 0.0005

def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  
  instance = dht11.DHT11(pin = Temp_sensor)
  
  #GPIO.setup(LCD_E, GPIO.OUT)  # Enable
  #GPIO.setup(LCD_RS, GPIO.OUT) # RS
  #GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  #GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  #GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  #GPIO.setup(LCD_D7, GPIO.OUT) # DB7


  # Initialise display
  #lcd_init()

  while True:
	#get DHT11 sensor value
	result = instance.read()
        # Send some test

	#if result.is_valid():
	print result
	time.sleep(3)
 
if __name__ == '__main__':

#	try:
  		main()
#   	except KeyboardInterrupt:
#    		pass
#    	finally:
    #lcd_byte(0x01, LCD_CMD)
    #lcd_string("Goodbye!",LCD_LINE_1)
    #GPIO.cleanup()
