from mpu6050 import mpu6050
from xml.sax.handler import property_declaration_handler
import paho.mqtt.client as mqtt
import time
import datetime

mpu = mpu6050(0x68) #assign mpu to the right I2C address

#TODO: add MQTT interface

BROKER_IP_ADDRESS = 'localhost'
PORT = 1883
#BROKER_IP_ADDRESS = '107.13.179.1'
#PORT = 3276

KEEPALIVE = 60

TOPIC_MPU = "ncsu/iot/G11/MPU"

SUCCESS_CODE = 0

data = [0,0,0,0,0,0]


def mqtt_connect(client, data, flags, rc):
    if rc == SUCCESS_CODE:
        #client.publish(TOPIC_STATUS, STATUS_CONNECT_MSG, 2, True)
        print(f"Connected")
    else:
        print(f"Failed connection. Code {rc}")

def mqtt_connect(client, data, flags, rc):
    if rc == SUCCESS_CODE:
        client.publish(TOPIC_STATUS, STATUS_CONNECT_MSG, 2, True)
        print(f"Connected")
    else:
        print(f"Failed connection. Code {rc}")

def read_MPU(sensor):
	vals = [sensor.get_accel_data().get('x'),sensor.get_accel_data().get('y'),sensor.get_accel_data().get('z'),sensor.get_gyro_data().get('x'),sensor.get_gyro_data().get('y'),sensor.get_gyro_data().get('z')]
	return vals

# main
def main():

    # Create client
#	mqttClient = mqtt.Client("MPU6050")
    # Define callbacks
#	mqttClient.on_connect = mqtt_connect
	#mqttClient.on_message = mqtt_message_rcv
	#mqttClient.on_disconnect = mqtt_disconnect
#	mqttClient.connect(host = BROKER_IP_ADDRESS, port = PORT, keepalive = KEEPALIVE)
#	mqttClient.loop_start()
	f = open("train_data_new.txt", 'w')
	print("starting loop")
	label = ", STATIONARY"
	pastData = [0,0,0]
	avg = 0;
	while True:
		data = read_MPU(mpu)
		#mqttClient.publish(TOPIC_MPU, data, 2, True)
		#print(data)
		pastData[2] = pastData[1]
		pastData[1] = pastData[0]
		pastData[0] = data[3]
		avg = (pastData[0] + pastData[1] + pastData[2]) / 3
		if avg > 50:
			label = ", OPEN"
		elif avg < -50:
			label = ", CLOSED"
		else:
			label = ", STATIONARY"
		f.write(str(datetime.datetime.now()) + ": " + str(data) + label)
		f.write('\n')
		print(label)
		time.sleep(0.01)


if __name__ == '__main__':
	main()