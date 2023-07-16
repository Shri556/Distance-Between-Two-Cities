#Calculates the distance between two cities and allows the user to specify a unit of distance. 
#This program may require finding coordinates for the cities like latitude and longitude.

from math import radians,sin,cos,asin,sqrt

def inpt():
    while True:
        lat1 = input("LATITUDE of Postion 1: ")
        try:
            lat1 = float(lat1)
        except:
            pass

        if type(lat1) == float:
            print(f"LATITUDE 1: {lat1}")
            break
    
    while True:
        long1 = input("LONGITUDE of Postion 1: ")
        try:
            long1 = float(long1)
        except:
            pass

        if type(long1) == float:
            print(f"LONGITUDE 1: {long1}")
            break

    while True:
        lat2 = input("LATITUDE of Postion 2: ")
        try:
            lat2 = float(lat2)
        except:
            pass

        if type(lat2) == float:
            print(f"LATITUDE 2: {lat2}")
            break

    while True:
        long2 = input("LONGITUDE of Postion 2: ")
        try:
            long2 = float(long2)
        except:
            pass

        if type(long2) == float:
            print(f"LONGITUDE 2: {long2} ")
            break

    return lat1,long1,lat2,long2

def calc():
    lat1,long1,lat2,long2 = inpt()

    lat1 = radians(lat1)
    lat2 = radians(lat2)
    long1 = radians(long1)
    long2 = radians(long2)

    dlat = lat2 - lat1
    dlon = long2 - long1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2) **2

    c = 2 * asin(sqrt(a))

    r = 6371

    return (c*r)

if __name__ == '__main__':
    print(f"The distance between two places is {calc()} KM")