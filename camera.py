#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python
# shoot.py
import threading
import os
import time
import datetime

capture_lock = threading.RLock() # lock object

class Camera(object):

  def __init__(self):
   self.todaydetail = datetime.datetime.today() 
   global capture_lock

  def shutter(self, sender, earg):
#    try:
    with capture_lock:
      print("-- Capture Lock by " + threading.currentThread().getName() + " --")
      print(earg+".jpg")
      os.system('raspistill -o ' + earg + '.jpg -vf -hf -w 1024 -h 768 -t 1000 -ex antishake')
      time.sleep(1)
      print("--Capture UnLock--")
#    except:
#      print("cancel capture")
