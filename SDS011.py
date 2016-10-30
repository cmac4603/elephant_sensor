#!/usr/bin/python
from __future__ import print_function
import serial, struct

ser = serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 9600

ser.open()
ser.flushInput()

class SDS011():
    def process_frame(self, d):
        r = struct.unpack('<HHxxBBB', d[2:])
        pm25 = r[0] / 10.0
        pm10 = r[1] / 10.0
        checksum = sum(ord(v) for v in d[2:8]) % 256
        return (pm25, pm10, checksum)

    def run(self):
        byte, data = 0, ""
        while byte != "\xaa":
            byte = ser.read(size=1)
        d = ser.read(size=10)
        if d[0] == "\xc0":
            self.process_frame(byte + d)
