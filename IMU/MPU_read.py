from mpu6050 import mpu6050
from xml.sax.handler import property_declaration_handler
import paho.mqtt.client as mqtt
import time
import datetime
from copy import deepcopy
from datetime import datetime
from feature_creation import create_data
import numpy as np
import requests
import wiotp.sdk.device
import json

TOPIC_IMU = "DoorStatus"
BEST_WINDOW_SIZE = 3

IMU_SAMPLING_RATE = 0.01  # Unit: seconds

# Variables
mpu = mpu6050(0x68)  # assign mpu to the right I2C address

def read_MPU(sensor):

    vals = [sensor.get_accel_data().get('x'), sensor.get_accel_data().get('y'), sensor.get_accel_data().get('z'),
            sensor.get_gyro_data().get('x'), sensor.get_gyro_data().get('y'), sensor.get_gyro_data().get('z')]
    
    return vals


current_label = 'STATIONARY'
past_gyro_data = [0, 0, 0]
avg = 0
past_labels = ['STATIONARY', 'STATIONARY', 'STATIONARY']
api_payload = []
cycle_start = False

def update_label(gyro_x):
    global current_label, past_gyro_data, avg

    past_gyro_data[2] = past_gyro_data[1]
    past_gyro_data[1] = past_gyro_data[0]
    past_gyro_data[0] = gyro_x

    avg = (past_gyro_data[0] + past_gyro_data[1] + past_gyro_data[2]) / 3

    if avg > 50:
        current_label = "OPEN"
    elif avg < -50:
        current_label = "CLOSED"
    else:
        current_label = "STATIONARY"


def detect_cycle(data):
    global current_label, past_labels, api_payload, cycle_start

    last_removed = past_labels[2]
    past_labels[2] = past_labels[1]
    past_labels[1] = past_labels[0]
    past_labels[0] = current_label

    ret_flag = False
    
    if cycle_start and past_labels[0] == past_labels[1] == past_labels[2] == 'STATIONARY':
        cycle_start = False
        ret_flag = True
    
    elif not cycle_start and current_label != 'STATIONARY':
        cycle_start = True
        api_payload = []
        api_payload.append(data)
    
    elif cycle_start and current_label != 'STATIONARY':
        api_payload.append(data)

    return ret_flag, last_removed


def get_prediction():
    global api_payload
    
    model_data = create_data([deepcopy(api_payload)], BEST_WINDOW_SIZE)
    model_data = model_data.tolist()

    API_KEY = "ysQ6mF886s6PwVPZt-2KqdmX4CnQZ78P3zjuEQwm4Y5v"
    
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token',
                                   data={"apikey": API_KEY,
                                         "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    # header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    payload_scoring = {"input_data": [{"fields": ["f0", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"],
                                       "values": model_data}]}
    
    response_scoring = requests.post(
        'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/19192d86-bf90-4ada-8898-a757aa57d433/predictions?version=2022-04-10',
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
    
    result = response_scoring.json()

    prediction_value = "CLOSED" if result['predictions'][0]['values'][0][0] == 0 else "OPEN"
    
    return prediction_value


def publishEventCallback():
    	print("Published.")

# main
def main():
    
    try:
        # Create client
        options = wiotp.sdk.application.parseConfigFile("RPi.yaml")
        mqttClient = wiotp.sdk.application.ApplicationClient(config=options)
        mqttClient.connect()
        
        print("starting loop")

        while True:
            # Read IMU
            data = read_MPU(mpu)

            update_label(data[3])
            cycle_detected, cycle_label = detect_cycle(data)

            # Get Prediction from cloud Model and Publish to MQTT
            if cycle_detected:
                # Get Prediction from cloud Model
                returned_label = get_prediction()

                if returned_label != cycle_label:
                    returned_label = cycle_label

                TIMESTAMP = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
                DoorStatus = {'TimeStamp' : TIMESTAMP , 'Status' : returned_label}

                mqttClient.publishEvent(typeId="IOT_Assignment_4", deviceId="3", eventId=TOPIC_IMU, qos = 2, msgFormat="json", data=DoorStatus, onPublish=publishEventCallback)
                
                # print(returned_label, " -------------- ", cycle_label)
                
            time.sleep(IMU_SAMPLING_RATE)
    
    except Exception as e:
        print("Exception: ", e)

if __name__ == '__main__':
    main()
