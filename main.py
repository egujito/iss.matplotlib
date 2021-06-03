"""
Where is the ISS At.
By: Saiko2043
"""
import requests
import matplotlib.pyplot as plt
# import random # WAS ONLY NECESSARY DURING DEBUGING
from itertools import count
from matplotlib.animation import FuncAnimation

url = "https://api.wheretheiss.at/v1/satellites/25544"

y_velocity = []
y_altitude = []
y_longitude = []
y_latitude = []

x_delta_time = []

index = count()

fig = plt.figure(figsize=(15,15))

fig.suptitle("ISS TRACKER")


ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2, sharex= ax1)
ax3 = fig.add_subplot(2, 2, 3, sharex= ax1)
ax4 = fig.add_subplot(2, 2, 4, sharex=ax1)


ax1.set_xlabel('time (s)')
ax2.set_xlabel('time (s)')
ax3.set_xlabel('time (s)')
ax4.set_xlabel('time (s)')

ax1.set_ylabel('Velocity')
ax2.set_ylabel('Altitude')
ax3.set_ylabel('Latitude')
ax4.set_ylabel('Longitude')


# uncomment this line if you don't want the figure to display scientific notation
# ax1.ticklabel_format(useOffset=False, style='plain')
ax2.ticklabel_format(useOffset=False, style='plain')
ax3.ticklabel_format(useOffset=False, style='plain')
ax4.ticklabel_format(useOffset=False, style='plain')

def updateData(i):
    
    data = requests.get(url).json()
 
    
    velocity = data['velocity']
    altitude = data['altitude']
    latitude = data['latitude']
    longitude = data['longitude']

    
    y_velocity.append(velocity)
    y_altitude.append(altitude)
    y_latitude.append(latitude)
    y_longitude.append(longitude)

    x_delta_time.append(next(index))


    ax1.plot(x_delta_time, y_velocity, color='red')
    ax2.plot(x_delta_time, y_altitude, color='blue')
    ax3.plot(x_delta_time, y_latitude, color='orange')
    ax4.plot(x_delta_time, y_longitude, color='green')

animate = FuncAnimation(fig, updateData, interval = 1000)
plt.show()
