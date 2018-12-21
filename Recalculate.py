def Recalculate(looptime, loopdays, loophours, loopminutes, satelliteindex, line0, line1, line2, stationlon1, stationlat1, hstation1):    
    from SGP4 import SGP4
    from Choosetime import Choosetime
    from Continue import Continue
    from PlotOnMap import PlotOnMap


    ########################################################################################################################################
    #Define time
    #input: days, hours, minutes, negative minutes
    year, month, day, hour, minute, second, localtime = Choosetime(loopdays, loophours, loopminutes, 0)
    #print(localtime)

    
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

    PosStation = (stationlon1,  stationlat1, hstation1)

    from GEOD2CART import GEOD2CART
    Rstation = GEOD2CART(PosStation)
    #print('Rstation', Rstation)

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
            timevector.append(time)
            j +=1
    elif looptime == 1:
        j = satelliteindex
        for k in range(0,len(year)-1):
            Carthesian = (SGP4(line1[j], line2[j], year[k], month[k], day[k], hour[k], minute[k], second[k]))
            cartesianvector.append(Carthesian)
            time = (year[k], month[k], day[k], hour[k], minute[k], second[k])
            cartesianvector.append(Carthesian)
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
    #####################################################################################################################
    #Split passings, needed inviewvector and time
    beginpassing = []
    endpassing = []
    #begin or end is in passing
    if inviewvector[0] is True:
        beginpassing.append(0)


    
    for j in range(1, len(inviewvector)):
        if inviewvector[j]  is True and inviewvector[j-1] is False:
           beginpassing.append(j)
           j=j+1
        elif inviewvector[j]  is False and inviewvector[j-1] is True:
            endpassing.append(j)

    if inviewvector[len(inviewvector)-1] is True:
        endpassing.append(len(inviewvector)-1)


    for j in range(0, len(beginpassing)):
        timepassing = []
        for n in range(beginpassing[j], endpassing[j]):
            timepassing.append(timevector[n])
        filename = 'doptrackinfo' + str(j) + '.yml'
        file = open(filename, 'w')
        file.write(str(timepassing))
        file.close()


    print(beginpassing, endpassing)
    #print(timevector)


    PlotOnMap(latitudevector, longitudevector, timevector, inviewvector,PosStation)
    print("done")
    # plt.show()

    return
