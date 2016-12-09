#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python
# motion.py

import RPi.GPIO as GPIO
import time
import event
import datetime

class Motion(object):

  def __init__(self):
    self.INTAVAL = 3
    self.SLEEPTIME = 2
    self.SENSOR_PIN = 18
    self.evt = event.Event()


  def execute(self, sender, earg):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.SENSOR_PIN, GPIO.IN)
    self.st = time.time() - self.INTAVAL
    while True:
      print("待機中")
      print("motion_self", self)
      print("motion_sender",sender)
      print("motion_earg",earg)
      if(GPIO.input(self.SENSOR_PIN)==GPIO.HIGH) and (self.st + self.INTAVAL < time.time()):
        print ("人を感知しました")
        self.st = time.time()
        self.earg = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
        self.evt(self, self.earg)
      time.sleep(self.SLEEPTIME)

  GPIO.cleanup()
