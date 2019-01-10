def AzimuthCalc(PosStation, Rsat, Rstation):
    import numpy as np

    #LAT LON in degrees



    #Create plane from Rstation




    # use this https://gssc.esa.int/navipedia/index.php/Transformations_between_ECEF_and_ENU_coordinates 





    normStation = np.linalg.norm(Rstation)
    normSat = np.linalg.norm(Rsat)

    # print('test')
    # print(Rsat)
    # print(Rstation)

    p = (Rsat - Rstation)/(normSat-normStation)

    #omega and lambda are ellipsoid coordinates lat and long of the station
    #degrees for calc

    LON = PosStation[0]
    LAT = PosStation[1]

    OMG = LON/180*np.pi
    LAM = LAT/180*np.pi


    e = (-1*np.sin(LAM), np.cos(LAM), 0)
    n = (-1*np.cos(LAM)*np.sin(OMG), -1*np.sin(LAM)*np.sin(OMG), np.cos(OMG))
    u = (np.cos(LAM)*np.cos(OMG), np.sin(LAM)*np.cos(OMG), np.sin(OMG))

    
    # Elev = np.arcsin(p.dot(u))
    AZ = np.arctan(p.dot(e)/(p.dot(n)))
    Elev=0

    # Elev = Elev*180/(np.pi)
    AZ = AZ*180/(np.pi)

    if AZ < 0:
        AZ = 360 + AZ

    return (AZ, Elev)