#!/usr/bin/python
# coding=utf-8

from __future__ import print_function
import serial, struct

ser = serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 9600

ser.open()
ser.flushInput()

byte, data = 0, ""

def process_frame(d):
    r = struct.unpack('<HHxxBBB', d[2:])
    pm25 = r[0]/10.0
    pm10 = r[1]/10.0
    checksum = sum(ord(v) for v in d[2:8])%256
    print("PM 2.5: {} μg/m^3  PM 10: {} μg/m^3 CRC={}".format(pm25, pm10, "OK" if (checksum==r[2] and r[3]==0xab) else "NOK"))

while True:
    while byte != "\xaa":
        byte = ser.read(size=1)
    d = ser.read(size=10)
    if d[0] == "\xc0":
        process_frame(byte + d)
