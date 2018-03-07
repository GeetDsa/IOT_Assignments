from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(18,GPIO.OUT)

state=0;
def changeState():
	global state;
	if state == 0:
		GPIO.output(18,GPIO.HIGH)
		state=1;
	elif state==1:
		GPIO.output(18,GPIO.LOW)
		state = 0;
	return
while True:
	try:
		if (GPIO.input(4)==1):
			print("No sound")
		else:
			print("!Sound Detected")
			changeState()
			sleep(1);

	except KeyboardInterrupt:
		exit()
GPIO.cleanup()

