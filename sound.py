from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
while True:
	try:
		if (GPIO.input(4)==1):
			print("No sound")
		else:
			print("!Sound Detected")
		sleep(0.3);
	except KeyboardInterrupt:
		exit()
GPIO.cleanup()

