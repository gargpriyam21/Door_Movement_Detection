from mpu6050 import mpu6050
from xml.sax.handler import property_declaration_handler
import paho.mqtt.client as mqtt
import time
import datetime

# Constants
BROKER_IP_ADDRESS = 'localhost'
PORT = 1883
KEEPALIVE = 60

TOPIC_IMU = "ncsu/iot/G11/IMU"

SUCCESS_CODE = 0

IMU_SAMPLING_RATE = 0.01 # Unit: seconds

# Variables
mpu = mpu6050(0x68) # assign mpu to the right I2C address

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

def read_MPU(sensor):
	vals = [sensor.get_accel_data().get('x'),sensor.get_accel_data().get('y'),sensor.get_accel_data().get('z'),sensor.get_gyro_data().get('x'),sensor.get_gyro_data().get('y'),sensor.get_gyro_data().get('z')]
	return vals

# main
def main():
	
	# Create client
	mqttClient = mqtt.Client("DoorIMU")

	# Define callbacks
	mqttClient.on_connect = mqtt_connect
	mqttClient.on_disconnect = mqtt_disconnect

	# Connect to broker
	mqttClient.connect(host = BROKER_IP_ADDRESS, port = PORT, keepalive = KEEPALIVE)
	mqttClient.loop_start()

	#f = open("door_open.txt", 'w')
	print("starting loop")

	#label = ", STATIONARY"
	#pastData = [0,0,0]
	#avg = 0

	while True:
		data = read_MPU(mpu)
		#print(data)

		'''
		@Divyang
		Make REST API call here and get response
		'''
		returnedLabel = "enter label response here"

		mqttClient.publish(TOPIC_IMU, returnedLabel, 2, True)

		# pastData[2] = pastData[1]
		# pastData[1] = pastData[0]
		# pastData[0] = mpu.get_gyro_data().get('x')

		# avg = (pastData[0] + pastData[1] + pastData[2]) / 3

		# if avg > 50:
		# 	label = ", OPEN"
		# elif avg < -50:
		# 	label = ", CLOSED"
		# else:
		# 	label = ", STATIONARY"

		# f.write(str(datetime.datetime.now()) + ": " + str(data) + label)
		# f.write('\n')

		# print(label)

		time.sleep(IMU_SAMPLING_RATE)


if __name__ == '__main__':
	main()
