import paho.mqtt.client as mqtt
broker_address ="127.0.0.1"  # "mqtt://localhost"
client = mqtt.Client("P1")
client.connect(broker_address)
client.publish("house/main-light", "OFF")
