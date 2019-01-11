def deltacalculator(PosStation, Rstation):
    from GEOD2CART import GEOD2CART
    import numpy as np
    Lat = PosStation[1]
    Lon = PosStation[0]

    # print(Lat)
    # print(Lon)

    LatStep = 0.5
    LonStep = 0.5

    # print(Rstation)
    DeltaN = GEOD2CART((Lon,(Lat+LatStep),0))
    DeltaE = GEOD2CART(((Lon+LonStep),Lat,0))

    # print(DeltaN)
    # print(DeltaE)
    DeltaN = np.asarray(DeltaN)
    DeltaE = np.asarray(DeltaE)
    Rstation = np.asanyarray(Rstation)

    N =  DeltaN - Rstation 
    E =  DeltaE - Rstation 
    # print(N)
    # print(E)


    DeltaLat = 0
    DeltaLon = 0
    return(N, E)