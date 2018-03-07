import sys
import RPi.GPIO as GPIO
from time import sleep  
import Adafruit_DHT
import urllib2
while True:
 humidity, temperature = Adafruit_DHT.read_retry(11, 4)

 if humidity is not None and temperature is not None:
    print 'Temp='+str(temperature)+',Humidity='+str(humidity)
 else:
    print 'Failed to get reading. Try again!'
