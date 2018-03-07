from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.setup(4,GPIO.IN)
GPIO.setup(4,GPIO.OUT)

state=1;
def changeState():
	global state;
	if state == 0:
		GPIO.output(4,GPIO.HIGH)
		state=1;
	elif state==1:
		GPIO.output(4,GPIO.LOW)
		state = 0;
	return
while True:
	changeState()
	sleep(2);
GPIO.cleanup()

