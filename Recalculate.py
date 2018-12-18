def Recalculate(looptime, loopdays, satelliteindex, line0, line1, line2, stationlon1, stationlat1, hstation1):    
    from SGP4 import SGP4
    from Choosetime import Choosetime
    from Continue import Continue
    from PlotOnMap import PlotOnMap
    from maketxtfile import maketxtfile
    from makeyamlfile import makeyamlfile
    ########################################################################################################################################
    #Define time
    #looptime = 1 #set 1 for looping time,
                 #set 0 for 'now'
    #loopminutes = 1 #only used when looptime = 1, 
                 #set for how many days te loop should be
                 #only integers
    year, month, day, hour, minute, second = Choosetime(looptime, loopdays)
    
    ########################################################################################################################################
    #Define satellite
    #Choosing sattelite still needs to be added
    if looptime == 1:
        loopsat = 0
    else:
       loopsat = 1

    ########################################################################################################################################
    #Propegation
    #loop j sattelite
    #loop k time
    j = 0
    k = 0
    cartesianvector = []
    elevationvector = []
    azimuthvector = []
    inviewvector = []
    latitudevector = []
    longitudevector = []
    timevector = []

    PosStation = (stationlon1, stationlat1, hstation1)

    from GEOD2CART import GEOD2CART
    #THIS IS NOT CORRECT just ask user to give XYZ =D
    Rstation = GEOD2CART(PosStation)
    print(Rstation)
    Rstation = [3922.57605980654, 298.869320744213,5003.59629628637]
    print(Rstation)
    # print('Rstation', Rstation)/

    if loopsat == 1:
        k = 0
        for j in range (0, len(line0)-1):
            Carthesian = (SGP4(line1[j], line2[j], year[k], month[k], day[k], hour[k], minute[k], second[k]))
            time = (year[k], month[k], day[k], hour[k], minute[k], second[k])
            cartesianvector.append(Carthesian)
            inview, latitude, longitude, elevation, azimuth = Continue(Carthesian[0], time, Rstation)
            elevationvector.append(elevation)
            azimuthvector.append(azimuth)
            inviewvector.append(inview)
            latitudevector.append(latitude)
            longitudevector.append(longitude)
            timevector.append([time])
            j +=1
    elif looptime == 1:
        j = satelliteindex
        for k in range(0,len(year)-1):
            Carthesian = (SGP4(line1[j], line2[j], year[k], month[k], day[k], hour[k], minute[k], second[k]))
            cartesianvector.append(Carthesian)
            time = (year[k], month[k], day[k], hour[k], minute[k], second[k])
            inview, latitude, longitude, elevation, azimuth = Continue(Carthesian[0], time, Rstation)
            elevationvector.append(elevation)
            azimuthvector.append(azimuth)
            inviewvector.append(inview)
            latitudevector.append(latitude)
            longitudevector.append(longitude)
            timevector.append(time)
            k +=1
            
    else:
        print('errorloop')
    # for n in range(0, len(line0)):
    #     print(latitudevector[n], longitudevector[n], line0[n])
    #print(Carthesian)


    maketxtfile(inviewvector, timevector, line0)
    makeyamlfile(inviewvector, timevector)

    PlotOnMap(latitudevector, longitudevector, timevector, inviewvector, PosStation)
    print("done")
    # plt.show()
    return