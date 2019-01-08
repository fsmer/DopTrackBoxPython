
def LoopallSats(mode, line0, line1,line2,Rstation, PosStation, satelliteindex):
    from SGP4 import SGP4
    from Continue import Continue
    from Choosetime import Choosetime
    from PlotOnMap import PlotOnMap
    from maketxtfile import maketxtfile
    #create time vector (1 time value)
    time1, year, month, day, hour, minute, second, regionaltime = Choosetime(0, 0, 1, 0)

    cartesianvector = []
    elevationvector = []
    azimuthvector = []
    inviewvector = []
    latitudevector = []
    longitudevector = []
    timevector = []
    #Recalculate SGP4 and Continue
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

    #make txt file

    maketxtfile(inviewvector,line0,elevationvector,azimuthvector,mode, 0, timevector, 0)
    
    #make yml file
    # makeyamlfile()
    #plot all sats on map
    # PlotOnMap(latitudevector, longitudevector, timevector, inviewvector, PosStation, 0, mode)
    print("done")
    #plot view of sky
    #plotinsight
    return

