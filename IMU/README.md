# IoT_ASN4_Group11 - Laptop

This repository is created for the sole purpose of uploading codes related to the Assignment 3 for the course CSC 591 - 022 Internet of Things: Architectures, Applications, and Implementation Spring 2022 of North Carolina State University.

## Environment
- macOS Monterey Version 12.2.1
- Python 3.7.3

## Requirements

Presence of `feature_creation.py` in the same folder as of the main file.

### Software
- Python3 3.7.3
- paho-mqtt v1.6.1
- numpy v1.19.5
- mosquitto 
- wiotp-sdk
- requests
- RPi.GPIO
- python3-smbus
- mpu6050-raspberrypi

```
pip install paho-mqtt
pip install RPi.GPIO
pip3 install wiotp-sdk
brew install mosquitto
apt install python3-smbus
pip install mpu6050-raspberrypi

```

### Hardware

-Raspberry Pi model 3B
-MPU6050 accelerometer & gyro

To setup the hardware, connect the following raspberry pi GPIO pins to the corresponding MPU pins.

GPIO 2 to SDA, <br />
GPIO 3 to SCL, <br />
5V to VCC, <br />
GND to GND <br />

## Procedure

Before proceeding with the execution make sure to update the **auth_key** and the **auth_token** in the `RPi.yaml` file. Other than that if you have published some other ML model on the IBM cloud make sure to update the **API_KEY** and the **response_scoring** in the file to the one you get from the model deployment.

Run the ***IMU (Inertial Measurement Unit)*** code by executing the below command on a new terminal window
```
python3 MPU_read.py
```

## Steps
1. Attach the required hardware to the door
2. Execute the code as explained in the above points
3. Proceed with opening and closing of the door as required
4. The status of the door will be predicted by the classification model on the cloud the respective result will be published via MQTT

# Instructor
- Dr. Muhammad Shahzad (mshahza@ncsu.edu )

# Teaching Assistants
- Hassan Ali Khan (hakhan@ncsu.edu)

# Team
- Priyam Garg (pgarg6@ncsu.edu)
- Divyang Doshi	(ddoshi2@ncsu.edu)
- Brendan Driscoll (bhdrisco@ncsu.edu)
- Jordan Boerger (jwboerge@ncsu.edu)
- Vishal Veera Reddy (vveerar2@ncsu.edu)
