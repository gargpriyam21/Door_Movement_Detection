# IoT_ASN4_Group11

This repository is created for the sole purpose of uploading codes related to the Assignment 4 for the course CSC 591 - 022 Internet of Things: Architectures, Applications, and Implementation Spring 2022 of North Carolina State University.

## Environment
- Python 3.7.3

## Requirements
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

-Raspberry Pi model 3B<br />
-MPU6050 accelerometer & gyro

To setup the hardware, connect the following raspberry pi GPIO pins to the corresponding MPU pins.

GPIO 2 to SDA, <br />
GPIO 3 to SCL, <br />
5V to VCC, <br />
GND to GND <br />

## Classification Model

For the prediction of the door status we have used the SVM model and deployed it to the IBM cloud. To which the IBM Cloud provides us the RESP API request on which the result can be requested by calling the API by passing the required data and calling the API.

The Complete procedure for the model implementation and deployment can be found under the `Model Implemenation and Implementation` folder.

## Procedure
For the execution of each code file, the  a detailed README.md file explaining how to execute the code is available in the respective folder of that device.

IMU : [IMU](./IMU)

Laptop : [Laptop](./Laptop)

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
