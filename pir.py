from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
while True:
	try:
		if (GPIO.input(4)):
			print("Intruder Detected")
		else:
			print("No Intruder")
		sleep(3)
	except KeyboardInterrupt:
		exit()
GPIO.cleanup()

