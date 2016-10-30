#!/usr/bin/python
from __future__ import print_function
import serial, struct


class SDS011():

    def __init__(self):
        self.ser = serial.Serial()
        self.ser.port = '/dev/ttyUSB0'
        self.ser.baudrate = 9600
        self.ser.open()
        self.ser.flushInput()

    def process_frame(self, d):
        r = struct.unpack('<HHxxBBB', d[2:])
        self.pm25 = r[0] / 10.0
        self.pm10 = r[1] / 10.0
        self.checksum = sum(ord(v) for v in d[2:8]) % 256
        return (self.pm25, self.pm10, self.checksum)

    def run(self):
        byte, data = 0, ""
        while byte != "\xaa":
            byte = self.ser.read(size=1)
        d = self.ser.read(size=10)
        if d[0] == "\xc0":
            self.process_frame(byte + d)
