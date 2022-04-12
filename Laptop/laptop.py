from xml.sax.handler import property_declaration_handler
import paho.mqtt.client as mqtt
import time
from datetime import datetime
import wiotp.sdk.application
import json
import numpy as np

# Constants
# BROKER_IP_ADDRESS = '192.168.1.233'
# PORT = 1883
# KEEPALIVE = 60

TOPIC_DOORSENSOR = "DoorStatus"


# SUCCESS_CODE = 0

# # Callbacks
# # Called on MQTT connect
# def mqtt_connect(client, data, flags, rc):
#     if rc == SUCCESS_CODE:
#         print(f"Connected")
#     else:
#         print(f"Failed connection. Code {rc}")
#
# # Called on MQTT disconnect
# def mqtt_disconnect(client, data, rc):
#     if rc == SUCCESS_CODE:
#         print("Graceful disconnect successful")
#     else:
#         print(f"Forced disconnect. Code {rc}")

# Called on MQTT msg received
def mqtt_message_rcv(evt):
    payload = json.dumps(evt.data).strip("{\" }").replace('"', '').split(":")
    receivedLabel = payload[1].lstrip(' ')
    TIMESTAMP = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
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

    # mqttClient = mqtt.Client("DoorIMUlaptop")
    #
    # # Define callbacks
    # mqttClient.on_connect = mqtt_connect
    # mqttClient.on_message = mqtt_message_rcv
    # mqttClient.on_disconnect = mqtt_disconnect
    #
    # # Connect to broker
    # mqttClient.connect(host = BROKER_IP_ADDRESS, port = PORT, keepalive = KEEPALIVE)
    # mqttClient.loop_start()
    #
    # mqttClient.subscribe(TOPIC_DOORSENSOR)


if __name__ == '__main__':
    main()
