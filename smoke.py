from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
while True:
	try:
		if (GPIO.input(4)==0):
			print("Smoke Detected! Move to safety")
		else:
			print("No Smoke! you are in SAFE zoone")
		sleep(1)
	except KeyboardInterrupt:
		exit()
GPIO.cleanup()

