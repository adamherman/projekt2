#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import os


while True:
	iname=time.strftime("%Y%m%d-%H%M%S")
	def reading(sensor):
		
		
		# Disable any warning message such as GPIO pins in use
		GPIO.setwarnings(False)
		
		
		GPIO.setmode(GPIO.BCM)
		
	
		if sensor == 0:
		
			
			GPIO.setup(23,GPIO.OUT)
			GPIO.setup(24,GPIO.IN)
			GPIO.output(23, GPIO.LOW)
			
			
			time.sleep(0.3)
			
			GPIO.output(23, True)
						
			time.sleep(0.00001)
			
			GPIO.output(23, False)
	
			while GPIO.input(24) == 0:
			  signaloff = time.time()
			
			while GPIO.input(24) == 1:
			  signalon = time.time()
			
			timepassed = signalon - signaloff
			
			distance = timepassed * 17000

			return distance
			
			GPIO.cleanup()
	
		else:
			print "Incorrect usonic() function varible."

	print reading(0)

	if reading(0) < 50:
		myname=str(iname)+".jpg"
		os.system("raspistill -t 100 -n -w 640 -h 480 -o img/"+myname)		
		time.sleep(4)
#		iname+=1
		print("fotka")