import time
import serial
          
      
ser = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
print("connected to: " + ser.portstr)
counter=0
          
      
while 1:
# try:
  if (ser.inWaiting()>0):
   x=ser.readline()
   print x
