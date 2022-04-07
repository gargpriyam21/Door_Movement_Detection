from xml.sax.handler import property_declaration_handler
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import numpy as np

# Constants
BROKER_IP_ADDRESS = 'localhost'
PORT = 1883
KEEPALIVE = 60

TOPIC_DOORSENSOR = "ncsu/iot/G11/IMU"

SUCCESS_CODE = 0

# Callbacks
# Called on MQTT connect
def mqtt_connect(client, data, flags, rc):
    if rc == SUCCESS_CODE:
        print(f"Connected")
    else:
        print(f"Failed connection. Code {rc}")

# Called on MQTT disconnect
def mqtt_disconnect(client, data, rc):
    if rc == SUCCESS_CODE:
        print("Graceful disconnect successful")
    else:
        print(f"Forced disconnect. Code {rc}")

# Called on MQTT msg received
def mqtt_message_rcv(client, data, message):
    receivedLabel = float(message.payload.decode("utf-8"))
    print(f"Door is {receivedLabel}")

# Main
def main():

    # Create client
    mqttClient = mqtt.Client("DoorIMU")

    # Define callbacks
    mqttClient.on_connect = mqtt_connect
    mqttClient.on_message = mqtt_message_rcv
    mqttClient.on_disconnect = mqtt_disconnect

    # Connect to broker
    mqttClient.connect(host = BROKER_IP_ADDRESS, port = PORT, keepalive = KEEPALIVE)
    mqttClient.loop_start()

    mqttClient.subscribe(TOPIC_DOORSENSOR)

if __name__ == '__main__':
    main()
