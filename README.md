# elephant_sensor
![Elephant Sensor](icon.png)

## Air pollution sensor on the Pi zero recording 2.5/10PPM (SDS011) with GPS, displayed on a LCD 16x2 matrix and writing to TinyDb

### Prequisite commands

_Standard python-related commands and modules for Ubuntu/Debian/Raspbian_

`sudo apt-get install build-essential python-dev python-smbus python-pip`

`sudo pip install -r requirements`

_To get the GPS linux module working_

`sudo apt-get install gpsd gpsd-clients`

`sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock`

`sudo systemctl stop gpsd.socket`

`sudo systemctl disable gpsd.socket`

`sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock`
