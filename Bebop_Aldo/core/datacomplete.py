import math
import time
import sys
import struct

import numpy as np
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise

from core.bebop import *
drone=Bebop()


my_filter = KalmanFilter(dim_x=2, dim_z=1)
lon = KalmanFilter (dim_x=2, dim_z=1)
lat = KalmanFilter (dim_x=2, dim_z=1)


variance=0.0005
uncertainty=0.005

lon.x = np.array([[2.],
                  [0.]])       # initial state (location and velocity) // State Transition Matrix
lon.F = np.array([[1.,1.],
                  [0.,1.]])    # state transition matrix
lon.H = np.array([[1.,0.]])    # Measurement function // Numpy array numpy.array(dim_x, dim_z)
lon.P *= 1000.                 # covariance matrix
lon.R = variance               # state uncertainty // numpy.array(dim_z, dim_z) ->measurement noise matrix
lon.Q = Q_discrete_white_noise(dim=2, dt=1, var=uncertainty) # process uncertainty

lat.x = np.array([[2.],
                  [0.]])       # initial state (location and velocity) // State Transition Matrix
lat.F = np.array([[1.,1.],
                  [0.,1.]])    # state transition matrix
lat.H = np.array([[1.,0.]])    # Measurement function // Numpy array numpy.array(dim_x, dim_z)
lat.P *= 1000.                 # covariance matrix
lat.R = variance               # state uncertainty // numpy.array(dim_z, dim_z) ->measurement noise matrix
lat.Q = Q_discrete_white_noise(dim=2, dt=1, var=uncertainty) # process uncertainty

#Finally, run the filter

def Data_Complete():
    lon.predict()
    lat.predict()
    drone.update()
    (roll, pitch, yaw) = drone.angle
    (lati, long, alt) = drone.positionGPS
    lon.update(lati)
    lat.update(long)
    x = lon.x
    y = lat.x
    [lat1,a]=x
    [lon1,b]=y
    return lat1, lon1, alt, roll, pitch, yaw


if __name__ == "__main__":
    Data_Complete()






