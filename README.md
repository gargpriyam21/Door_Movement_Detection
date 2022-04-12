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

```
pip install paho-mqtt
pip install RPi.GPIO
pip3 install wiotp-sdk
brew install mosquitto
```
### Hardware

@Brendan can add the hardware requirements
<!-- - Raspberry PI A,B (We have used Raspberry Pi 3B model)
- 3 LEDS
- 5 Resistors
  - 2 1kOhm Resistors
  - 3 230 Ohm Resistors
- 1 Photoresistor (LDR)
- 1 500 kOhm Potentiometer
- Jumper Wires
- BreadBoard
- 1 220 nF capacitor
- 1 1 uF capacitor
- Keyboard, mouse & display (not mandatory) -->

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