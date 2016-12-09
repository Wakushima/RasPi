#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python

import pysftp
import time
import RPi.GPIO as GPIO
import os
import datetime
import event
import motion_sensor
import camera
import uploader
import threading
import sonic_sensor

rlock = threading.RLock() # lock object

class Manager:

  def __init__(self):
     self.evt         = event.Event()
     self.motion      = motion_sensor.MotionSensor() #actuator class
     self.sonic       = sonic_sensor.SonicSensor()
     self.camera       = camera.Camera() #sensor class
     self.uploader    = uploader.Uploader() #process class
     self.motion.evt += self.camera.execute
     self.motion.evt += self.uploader.execute
     self.sonic.evt  += self.camera.execute
     self.sonic.evt  += self.uploader.execute 

  def execute(self):
    self.motion.execute(self, None)
    #self.sonic.measure(self, None)

if __name__ == '__main__':
  man  = Manager()
  man.execute()
