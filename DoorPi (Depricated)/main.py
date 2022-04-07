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

IMU_SAMPLING_RATE = 1 # Unit: seconds

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


# Methods
# Read IMU sensor and return value
def readSensor():
    sensorValue = 0

    """
    @BRENDAN
    I was thinking read the sensor here so it is returned and published
    """

    return sensorValue

# Main
def main():

    # Create client
    mqttClient = mqtt.Client("DoorIMU")

    # Define callbacks
    mqttClient.on_connect = mqtt_connect
    mqttClient.on_disconnect = mqtt_disconnect

    # Connect to broker
    mqttClient.connect(host = BROKER_IP_ADDRESS, port = PORT, keepalive = KEEPALIVE)
    mqttClient.loop_start()

    while True:
        time.sleep(IMU_SAMPLING_RATE)
        value = readSensor()
        mqttClient.publish(TOPIC_DOORSENSOR, value, 2, True)

if __name__ == '__main__':
    main()
