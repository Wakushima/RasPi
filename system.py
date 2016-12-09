#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python

import pysftp
import time
import RPi.GPIO as GPIO
import os
import datetime

INTAVAL = 3
SLLEPTIME = 2
SENSOR_PIN = 18
HOST = '172.21.42.152'
PORT = '22'
USER = 'iwataalb'
PRIVATE_KEY_FILE = '/home/pi/.ssh/id_rsa'
name = ''
uplploadPath = '/home/iwatalab/upload_image'

def upload(fName):
  fPath = '/home/iot_iwataken/motion_system/beagleboneblack/' + fName + '.jpg'
  sftp = pysftp.Connection(HOST, username=USER, port=PORT, privat_key=PRIVATE_KEY_FILE)
  sftp.listdir()
  sftp.chdir(uploadPath)
  sftp.getcwd()
  sftp.put(fPath)
  sftp.close()

GPIO.setmode(GPIO.BCM)
GPIT.setup(SENSOR_PIN, GPIO.IN)
st = time.time()-INTABAL

while True:
  if(GPIO.input(SENSOR_PIN)==GPIO.HIGH) and (st +INTAVAL < time.time()):
    st = time.time()
    print("待機中")
    todaydetail = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
    print todaydetail
    os.system('raspistill -o' + todaydetail + '.jpg -vf -hf -w 1024 -h 768 -t 1000 -ex antishake')
    time.sleep(2)
    upload(todatdetail)
  time.sleep(SLEEPTIME)
GPIO.cleanup()
    
