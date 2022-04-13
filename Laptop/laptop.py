from xml.sax.handler import property_declaration_handler
import paho.mqtt.client as mqtt
import time
from datetime import datetime
import wiotp.sdk.application
import json
import numpy as np

TOPIC_DOORSENSOR = "DoorStatus"

# Called on MQTT msg received
def mqtt_message_rcv(evt):
    received_data = evt.data
    TIMESTAMP = received_data['TimeStamp']
    receivedLabel = received_data['Status']

    print("{} : Door is {}".format(TIMESTAMP, receivedLabel))

# Main
def main():
    # Create client
    try:
        options = wiotp.sdk.application.parseConfigFile("laptop_config.yaml")
        mqttClient = wiotp.sdk.application.ApplicationClient(options)
        mqttClient.connect()
        mqttClient.subscribeToDeviceEvents(typeId="IOT_Assignment_4", deviceId='3', eventId=TOPIC_DOORSENSOR)
        mqttClient.deviceEventCallback = mqtt_message_rcv
        while True:
            pass
    except Exception as e:
        print("Exception: ", e)


if __name__ == '__main__':
    main()
