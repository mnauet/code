import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
########################################
def on_message(client, userdata, message):
    print("message.payload decode - received " ,str(message.payload.decode("utf-8")))
    print("message.topic=",message.topic)
    print("message.qos=",message.qos)
    print("message.retain flag=",message.retain)
########################################
broker_address ="127.0.0.1"  # "mqtt://localhost"
GPIO.setmode(GPIO.BCM  )    # set gpio pin mode
GPIO.setup(23, GPIO.OUT)    # led output
padPin = 22
GPIO.setup(22, GPIO.IN)		#touch sensor output

print("creating new instance")
client = mqtt.Client("P1")
client.on_message=on_message #attach function to callback
print("connecting to broker")   
client.connect(broker_address)  #connect to broker

client.loop_start() #start the loop
client.subscribe("p1/cmd/ledon")
client.subscribe("p1/cmd/ledoff")

client.publish("p1/sensor/encoder","publish")
client.publish("p1/sensor/encoder","encoder")
ledState = False

while True:
	#client.publish("p1/cmd/ledon","off")
	#client.publish("p1/cmd/ledon","on")
	padPressed = GPIO.input(padPin)
        if padPressed:
		#client.publish("p1/sensor/touch","touched")
		print("touched")
		if ledState:
			GPIO.output(23,GPIO.HIGH)
			ledState = False
			print ("true")
		else:
			GPIO.output(23,GPIO.LOW)
			ledState = True
			print ("false")
	        time.sleep(1)



# read temp here
#client.loop_forever() #stop the loop
