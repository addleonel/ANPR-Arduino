import os
from GPSPhoto import gpsphoto

filename = 'test2.jpg'
path = os.getcwd() + f'\\{filename}'
data = gpsphoto.getGPSData(path)
print(path)
print(data.get('Latitude'), data.get('Longitude'))
