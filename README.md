# elephant_sensor

## Air pollution sensor with GPS, SDS011 &amp; NO2, and LCD readings

`sudo apt-get install build-essential python-dev python-smbus python-pip`

`sudo pip install RPi.GPIO`

`cd /tmp\nclone\ncd /tmp/Adafruit_Python_CharLCD\nsudo python setup.py install`

`sudo apt-get install gpsd gpsd-clients`

`sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock`

`sudo systemctl stop gpsd.socket\nsudo systemctl disable gpsd.socket\nsudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock`
