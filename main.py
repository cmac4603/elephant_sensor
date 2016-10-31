#!/usr/bin/python
# coding=utf-8
from SDS011 import SDS011
from GPS import GPSPoller
import os
import time
from tinydb import TinyDB, where
import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:
lcd_rs = 26
lcd_en = 19
lcd_d4 = 13
lcd_d5 = 6
lcd_d6 = 5
lcd_d7 = 11
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

# Check if TinyDB JSON file already exists
if not os.path.isfile('/home/pi/db.json'):
    file('/home/pi/db.json', 'w').close()

# Initialize TinyDB with DB in /home/pi
db = TinyDB('/home/pi/db.json')
table = db.table('pollution')

if __name__ == "__main__":
    dust = SDS011()
    gps = GPSPoller()
    try:
        gps.start()
        while True:
            pm25, pm10, crc = dust.run()
            lcd.message("PM2.5:{}ug/m^3\nPM10:{}ug/m^3".format(pm25, pm10))
            time.sleep(5)
            lcd.clear()
            lat, lon = gps.gpsd.fix.latitude, gps.gpsd.fix.longitude
            lcd.message("LAT:{}\nLON:{}".format(lat, lon))
            time.sleep(5)
            if lat != 'Nan':
                table.insert({'pm25': pm25, 'pm10': pm10, 'latitude': lat, 'longitude': lon})
            lcd.clear()
    except KeyboardInterrupt:
        lcd.clear()
        gps.running = False
        gps.join()
        exit()
