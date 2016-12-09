#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python
# upload.py

import pysftp

class Upload(object):

  def __init__(self):
    self.HOST = '172.21.42.152'
    self.PORT = 22
    self.USER = 'iwatalab'
    self.PRIVATE_KEY_FILE = '/home/pi/.ssh/id_rsa'
    self.uploadPath = '/home/iwatalab/upload_image'

  def execute(self, sender, earg):
    print("upload_self", self)
    print("upload_sender",sender)
    print("upload_earg",earg)
    self.todaydetail = earg
    self.uploadPath = '/home/iwatalab/upload_image'
    self.fPath = '/home/pi/iot_iwataken/motion_system/beagleboneblack/' + self.todaydetail + '.jpg'
    sftp = pysftp.Connection(self.HOST, username=self.USER, port=self.PORT, private_key=self.PRIVATE_KEY_FILE)
    sftp.listdir()
    sftp.chdir(self.uploadPath)
    sftp.getcwd()
    sftp.put(self.fPath)
    for item in sftp.execute('ls -l /home/iwatalab/upload_image'):
      print item,     #結果を表示

    sftp.close()

