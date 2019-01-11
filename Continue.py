def Continue(Rsat, time, Rstation, DeltaLat, DeltaLon):
    #hoogte bepaald uit CART2GEOD blijkt erg slecht te zijn is hier iets anders voor zoals de baan - radus van de aarde?
    #Verder output naar txt bestand en mooi printen
    
    
    #time is in year, month, days, hour, minute, second
    #Rsat is in KM [x, y, z]
    #Rgroundstation in KM [x, y, z]

    #imports
    # import numpy as np
    #functions
    from UTC2GAST import UTC2GAST
    from RotationMatrix import RotationMatrix
    from CART2GEOD import CART2GEOD
    from Insight import Insight
    from SatElevation import SatElevation
    from AzimuthCalc import AzimuthCalc 
    #Get GAST for interested time
    #input time in year, month, days, hour, minute, second
    GAST = UTC2GAST(time)
    #output is GAST in degrees

    #print('GAST',GAST)
    
    #Rotate position vector
    #input is position [x,y,z] km
    RsatRotated = RotationMatrix(GAST, Rsat)
    #output is rotated position [x,y,z] km
    #print('RSatRotated', RsatRotated)
    #get Geodetic coordinates of satellite and height.
    #input Rotated satellite position km
    
    latitude, longitude, h = CART2GEOD(RsatRotated)
    #print('lat long h',latitude ,longitude ,h)
    #output radius from center of earth km, latitude degrees, longitude in degrees height from blob sphere km.

    #check if satellite is insight
    #input Rstation km, RsatRotaded km and Height of satellite. 
    inview = Insight(Rstation, RsatRotated)
    #print('inview',inview)
    #output is 1 when in sight 0 when not

    #get elevation and azimuth?
    #input Rstation and Rsatrotated
    minimumelevation = 0
    elevation, azimuth = SatElevation(Rstation, RsatRotated)

    if inview == True:
        if elevation <= minimumelevation:
            inview = 0

    azimuth = AzimuthCalc(DeltaLat, DeltaLon, Rstation, RsatRotated)
    #output in degrees
    #print('elev, azi',elevation,azimuth)
    #return insight, latitude, longitude, elevation, azimuth
    return (inview, latitude, longitude, elevation, azimuth)


