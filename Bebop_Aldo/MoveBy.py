#!/usr/bin/python
"""
  Starting for usage at the computer
  
"""
import math
import time
import sys
import struct
import signal
import os
import inspect

from core.bebop import *
drone=Bebop()

dX = 3
dY = 0
dZ = 0
dPsi = 0

def main():
    signal.signal(signal.SIGINT, signal_handler)
    try:
        drone.takeoff()
        time.sleep(1)
        #drone.update( cmd=moveByCmd( dX, dY, dZ, dPsi) )
        drone.hover()
        time.sleep(10)
        drone.moveBy( dX, dY, dZ, dPsi)
        drone.land()
        sys.exit(0)
    except (TypeError):
        print "error"
        pass

def signal_handler(signal, frame):
    drone.update( cmd=navigateHomeCmd( 0 ) )
    print('You pressed Ctrl+C!')
    print('Landing')
    drone.hover()
    if drone.flyingState is None or drone.flyingState == 1: # taking off
        drone.emergency()
    drone.land()
    sys.exit(0)


if __name__ == "__main__":
    main()