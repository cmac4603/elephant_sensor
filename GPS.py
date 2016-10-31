#! /usr/bin/python
from gps import *
import threading


class GPSPoller(threading.Thread):

  def __init__(self):
    threading.Thread.__init__(self)
    self.gpsd = gps(mode=WATCH_ENABLE)
    self.current_value = None
    self.running = True

  def run(self):
    while self.running:
      self.gpsd.next()