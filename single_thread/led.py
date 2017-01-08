import RPi.GPIO as GPIO
import time

class Led(object):
  def __init__(self):
    self.PIN = 21
    print self.PIN

  def execute(self, sender, earg):
  #def execute(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN, GPIO.OUT)
    GPIO.output(self.PIN, GPIO.HIGH)
    time.sleep(5)
    GPIO.cleanu()

#l = Led()
#l.execute()
