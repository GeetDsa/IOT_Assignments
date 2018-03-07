import sys
import RPi.GPIO as GPIO
from time import sleep  
import Adafruit_DHT
import urllib2
baseURL = 'https://api.thingspeak.com/update?api_key=9AJQPWTRJB2O56IE'
while True:
 humidity, temperature = Adafruit_DHT.read_retry(11, 4)

 if humidity is not None and temperature is not None:
    print 'Temp='+str(temperature)+',Humidity='+str(humidity)
    f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (temperature, humidity))
    f.read()
    f.close()
 else:
    print 'Failed to get reading. Try again!'
