#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python

import pysftp
import time
import RPi.GPIO as GPIO
import os
import datetime
import event
import motion
import shoot
import uploader

class Manager:

  def __init__(self):
     self.evt    = event.Event()
     self.motion = motion.Motion() #actuator class
     self.shoot  = shoot.Shoot() #sencer class
     self.uploader = uploader.Uploader() #sencer class
     self.motion.evt += self.shoot.execute
     self.motion.evt += self.uploader.execute

  def execute(self):
    self.motion.execute(self, None)

if __name__ == '__main__':
  man  = Manager()
  man.execute()
