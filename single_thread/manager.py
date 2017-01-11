#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python

import pysftp
import time
import RPi.GPIO as GPIO
import os
import datetime
import event
import camera
import uploader
import threading
import motion_sensor
import sonic_sensor

rlock = threading.RLock() # lock object

class Manager:

  def __init__(self):
     self.evnet_handlers         = event.Event()
     self.motion      = motion_sensor.MotionSensor() #actuator class
     self.sonic       = sonic_sensor.SonicSensor()
     self.camera      = camera.Camera() #sensor class
     self.uploader    = uploader.Uploader() #process class
     self.motion.event_handlers += self.camera.shutter
     self.motion.event_handlers += self.uploader.upload
     self.sonic.event_handlers  += self.camera.shutter
     self.sonic.event_handlers  += self.uploader.upload 

  def execute(self):
    self.motion.detect(self, None)
    #self.sonic.measure(self, None)

if __name__ == '__main__':
  man  = Manager()
  man.execute()
