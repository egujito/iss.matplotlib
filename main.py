"""
Where is the ISS At.
By: Saiko2043
LICENSE: MIT
"""
import requests
import matplotlib.pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation

y_velocity = []
y_altitude = []
y_longitude = []
y_latitude = []

x_delta_time = []

index = count()

fig = plt.figure(figsize=(15,15))

fig.suptitle("ISS TRACKER")

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222, sharex= ax1)
ax3 = fig.add_subplot(223, sharex= ax1)
ax4 = fig.add_subplot(224, sharex=ax1)

ax1.set_ylabel('Velocity')
ax2.set_ylabel('Altitude')
ax3.set_ylabel('Latitude')
ax4.set_ylabel('Longitude')

ax1.ticklabel_format(useOffset=False, style='plain')
ax2.ticklabel_format(useOffset=False, style='plain')
ax3.ticklabel_format(useOffset=False, style='plain')
ax4.ticklabel_format(useOffset=False, style='plain')

def updateData(i):
    
    url = "https://api.wheretheiss.at/v1/satellites/25544"
    data = requests.get(url).json()
 
    
    velocity = data['velocity']
    altitude = data['altitude']
    latitude = data['latitude']
    longitude = data['longitude']


    y_velocity.append(random.randrange(10))
    y_altitude.append(random.randrange(10))
    y_latitude.append(random.randrange(10))
    y_longitude.append(random.randrange(10))

    x_delta_time.append(next(index))

    ax1.plot(x_delta_time, y_velocity, color='red')
    ax2.plot(x_delta_time, y_altitude, color='blue')
    ax3.plot(x_delta_time, y_latitude, color='orange')
    ax4.plot(x_delta_time, y_longitude, color='green')

animate = FuncAnimation(fig, updateData, interval = 1)
plt.show()
