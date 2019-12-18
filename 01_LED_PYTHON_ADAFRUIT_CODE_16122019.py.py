  GNU nano 3.2                                                                    led5.py                                                                               

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from Adafruit_IO import *

ADAFRUIT_IO_KEY = '4ccce0cab0024d4ea8aa651507e27510'
ADAFRUIT_IO_USERNAME = 'Rakaka'

aio = Client('Rakaka','4ccce0cab0024d4ea8aa651507e27510')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

while True:
  controlling = aio.receive('divya').value
  print (controlling)
  if controlling == 'ON':
   GPIO.setup(4,GPIO.OUT)
   print ('LED1 ON')
   GPIO.output(4,GPIO.HIGH)
   GPIO.setup(17,GPIO.OUT)
   #print ('LED ON')
   GPIO.output(17,GPIO.LOW)

  #time.sleep(1)
  else:
   GPIO.setup(4,GPIO.OUT)
   #print ('LED OFF')
   GPIO.output(4,GPIO.LOW)
   GPIO.setup(17,GPIO.OUT)
   print ('LED2 ON')
   GPIO.output(17,GPIO.HIGH)

  #time.sleep(1)


                         