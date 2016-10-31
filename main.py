#!/usr/bin/python
# coding=utf-8
from SDS011 import SDS011
import gps
import time

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

if __name__ == "__main__":
    dust = SDS011()
    gpsd = gps(mode=WATCH_ENABLE)
    gpsd.start()
    try:
        while True:
            pm25, pm10, crc = dust.run()
            lcd.message("PM2.5:{}ug/m^3\nPM10:{}ug/m^3".format(pm25, pm10))
            time.sleep(5)
            lcd.message("LAT:{}\nLON:{}".format(gpsd.fix.latitude, gpsd.fix.longitude))
            time.sleep(5)
    except KeyboardInterrupt:
        lcd.clear()
        exit()
