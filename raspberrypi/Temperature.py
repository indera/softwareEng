# Copyright (c) 2012 Matthew Kirk
# Licensed under MIT License, see 
# http://www.cl.cam.ac.uk/freshers/raspberrypi/tutorials/temperature/LICENSE

import RPi.GPIO as GPIO
import time
import json
import pickle

# LED1_GPIO_PIN = 18
# LED2_GPIO_PIN = 25
# BUTTON_GPIO_PIN = 17
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(BUTTON_GPIO_PIN, GPIO.IN)
# GPIO.setup(LED1_GPIO_PIN, GPIO.OUT)
# GPIO.setup(LED2_GPIO_PIN, GPIO.OUT)

# GPIO.output(LED1_GPIO_PIN, GPIO.HIGH)

# while True:
	# if GPIO.input(BUTTON_GPIO_PIN):
		# break

# while GPIO.input(BUTTON_GPIO_PIN):
	# pass

# GPIO.output(LED1_GPIO_PIN, GPIO.LOW)
# GPIO.output(LED2_GPIO_PIN, GPIO.HIGH)

# timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
# filename = "".join(["temperaturedata", timestamp, ".log"])
# datafile = open(filename, "w", 1)

while True:
	tfile = open("/sys/bus/w1/devices/10-000802824e58/w1_slave")
	text = tfile.read()
	tfile.close()
	temperature_data = text.split()[-1]
	temperature = float(temperature_data[2:])
	temperature = temperature / 1000
	datafile.write(str(temperature) + "\n")
	data = [ {  'cusEmail' : 'indera@gmail.com', 'raspsDescription' : 'Temperature Sensor', 'temperature' : temperature, 'time': timestamp }]
	json= json.dumps(data)
	
	if GPIO.input(BUTTON_GPIO_PIN):
		break

datafile.close()
GPIO.output(LED2_GPIO_PIN, GPIO.LOW)
