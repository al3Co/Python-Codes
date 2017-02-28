import time
import sys
#import struct
#import threading
from pathplanning import *
from core.bebop import *

cicle=1
LatHome = None
LonHome = None

f = open('puntosGPS')


def main():
    global LatHome, LonHome, cicle, kill
    for line in f:
        tmp = line.split()
        lat = float(tmp[0])
        lon = float(tmp[1])
        print "Path Planning:", cicle, lat, lon
        [LatHome, LonHome, kill] = mainPP(lat, lon, cicle)
        cicle = cicle+1
        print "Home place", LatHome, LonHome
        if kill:
            sys.exit(0)
    time.sleep(1)
    cicle = None
    [LatHome, LonHome, kill] = mainPP(lat, lon, cicle)


if __name__ == "__main__":
    main()