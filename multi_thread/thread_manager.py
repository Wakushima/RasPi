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
import led
import threading
import sonic_sensor

global_variable = 0 
global_lock = threading.Lock() # Lock object

class Manager:

  def __init__(self):
    self.evt    = event.Event()
    self.motion = motion.Motion() #sencor class
    self.shoot  = shoot.Shoot() #actuator class
    self.uploader = uploader.Uploader() #actuator class
    self.led    = led.Led()
    self.sonic  = sonic_sensor.SonicSensor()
    GPIO.cleanup()

  def motion_method(self, earg=None):
    print "=== start main_thread(method) ===="
    print "[%s] thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today())
    self.evt(self, earg)

  def led_method(self, earg=None):
    print "=== start led_thead(method) ===="
    print "[%s] thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today())
    self.led.execute(self, earg)
    print "=== end [%s] led_thread (method) ===" % threading.currentThread().getName()

  def sonic_method(self, earg=None):
    print "=== start sonic_thead(method) ===="
    print "[%s] thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today())
    for i in range(earg):
      self.sonic.measure(self, earg)
      time.sleep(1)
    time.sleep(2)
    print "=== end [%s] sonic_thread (method) ===" % threading.currentThread().getName()

  def test(self, earg=None):
    print "=== start test_thread(method) ===="
    print "[%s] thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today())
    for i in range(earg):
      print "hello, %d" % i
      time.sleep(1)
    print "=== end [%s] test_thread (method) ===" % threading.currentThread().getName()

  def main(self):
    thread_motion = threading.Thread(target=self.motion_method, name="motion_sensor_class",)
    #thread_led = threading.Thread(target=self.led, name="temp_sensor_class", )
    thread_sonic= threading.Thread(target=self.sonic_method, name="sonic_sensor_class", args=(5, ))
    #thread_test= threading.Thread(target=self.test, name="test_sensor_class", args=(5, ))

#    thread_motion.start()
    thread_motion.start()
    time.sleep(1)
    thread_sonic.start()

if __name__ == '__main__':
  man  = Manager()
  man.evt += man.motion.execute
  man.motion.evt += man.shoot.execute
  man.motion.evt += man.uploader.execute
  man.main()
