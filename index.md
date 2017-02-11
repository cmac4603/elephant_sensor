![Elephant Sensor](icon.png)

## Air pollution sensor that can run on a Pi-Zero recording 2.5/10PPM (SDS011) with GPS, displayed on a LCD 16x2 matrix and writing to TinyDb

### How to use

### Plug 'n' Play

  - As soon as the battery is plugged in to the Pi-Zero, the main program will run.
  - Only when the GPS sensor begins returning latitude and longitude readings, is any data actually saved. It will still show readings on the LCD screen, as these flash across the screen every couple of seconds, but until GPS is active, none of the other data is saved.
  - So all you need to do is take it outside, and it will start recording 2.5 & 10 PPM readings, your location, and the time
 
### Map the Data

  - There is a script in this repository, `map_plotter.py`. This will grab all the data saved and plot it onto a Google Maps.
  - Connect the Raspberry Pi to your local wifi, find out it's local IP (via your router, or if you SSH onto the Pi you can use `ifconfig` and look for wlan0 usually. Over ethernet will usually be eth0).
  - Change the IP var in the python script using any text editor
  - You will also need an API key from [here](https://developers.google.com/maps/documentation/javascript/get-api-key) to gain access to the Google Maps API. You will also then need to change the API_KEY object, currently set to 'XXXXX' in this repo. 
  - Then in the terminal of the Pi run:
```python map_plotter.py```
  - This will create 'maps.html' in the current directory, and you will have a lovely map with colour-coded location markers showing how filthy the air was you were breathing!


### Prequisite commands
As well as the code in this repository, you will also need to run the following commands on the Pi

_Python-related commands and modules for Ubuntu/Debian/Raspbian_

```
sudo apt-get install build-essential python-dev python-smbus python-pip
sudo pip install -r requirements
```

_To get the GPS linux module working_

```
sudo apt-get install gpsd gpsd-clients
sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket
sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock
```
