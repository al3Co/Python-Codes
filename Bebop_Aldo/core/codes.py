
def GPS_Home(lat, lon, flagHomePosition):
    LatHome=lat
    LonHome=lon
    flagHomePosition=True
    print "Home position saved", LatHome, LonHome
    return LatHome, LonHome

def VirtualWall_Data(lat, lon, LatPoint_1, LonPoint_1, flagVWdata, flagTrue):
    """Quitar de aqui cuando se elabore con varios puntos"""
    LatAnte=lat
    LonAnte=lon
    """ ^ """
    print LonAnte, lon, LatAnte, lat
    print LatPoint_1, LonPoint_1
    if flagVWdata==False:
        MPoint=abs(LonPoint_1 - LonAnte)
        Long1=LonAnte - (MPoint/2)
        Rlon=(MPoint/2) + 0.00015
        MPoint=abs(LatPoint_1 - LatAnte)
        Lati1=LatAnte - (MPoint/2)
        Rlat=(MPoint/2) + 0.00015
        flagVWdata=True
    if abs(abs(LatAnte)-abs(LatPoint_1))>0.001 or abs(abs(LonAnte)-abs(LonPoint_1))>0.001:
        print "The GPS point given are far away"
        print "Distance between points:",abs(LatAnte-LatPoint_1), "in Latitude",abs(abs(LonAnte)-abs(LonPoint_1)),"in Longitude"
        flagTrue=False
        print "SYSTEM EXIT"
    return Long1, Rlon, Lati1, Rlat, LatAnte, LonAnte, flagVWdata, flagTrue



#if __name__ == "__main__":
#    void()