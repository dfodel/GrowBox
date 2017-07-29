from datetime import datetime
import RPi.GPIO as GPIO
import sys, web

lighting_start = int(sys.argv[1])
photoperiod = int(sys.argv[2])

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)

def lighting(on):
	if on:
		GPIO.output(18, GPIO.LOW)
		print 'Light on'
	else:
		GPIO.output(18, GPIO.HIGH)
		print 'Light off'
	return

while True:
	hour = int(datetime.now().hour)

	if hour >= lighting_start and hour < lighting_start + photoperiod:
		lighting(True)
	else:
		lighting(False)
	
