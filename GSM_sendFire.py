import serial
import RPi.GPIO as GPIO      
import os, time
 
GPIO.setmode(GPIO.BOARD)    

def send_msg(): 
 # Enable Serial Communication
 port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
 
 # Transmitting AT Commands to the Modem
 # '\r\n' indicates the Enter key
 
 port.write('AT'+'\r\n')
 rcv = port.read(10)
 print rcv
 time.sleep(1)
 
 port.write('ATE0'+'\r\n')      # Disable the Echo
 rcv = port.read(10)
 print rcv
 time.sleep(1)
 
 port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
 rcv = port.read(10)
 print rcv
 time.sleep(1)
 
 port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
 rcv = port.read(10)
 print rcv
 time.sleep(1)
 
# Sending a message to a particular Number
 
 port.write('AT+CMGS="+917760049480"'+'\r\n')
 rcv = port.read(10)
 print rcv
 time.sleep(1)
 
 port.write('Smoke Detected!!! Take appropriate action'+'\r\n')  # Message
 rcv = port.read(10)
 print rcv
 
 port.write("\x1A") # Enable to send SMS
 for i in range(10):
    rcv = port.read(10)
    print rcv
 exit(0);

GPIO.setup(7,GPIO.IN)
while True:
        try:
                if (GPIO.input(7)==0):
                        print("Smoke Detected! Move to safety")
			send_msg()
                else:
                        print("No Smoke! you are in SAFE zoone")
                time.sleep(1)
        except KeyboardInterrupt:
                exit()
GPIO.cleanup()

