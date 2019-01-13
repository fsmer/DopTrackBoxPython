def LoopallSats(mode, line0, line1,line2,Rstation, PosStation, satelliteindex, DeltaLat, DeltaLon, frequency, minelevation):
    from SGP4 import SGP4
    from Continue import Continue
    from Choosetime import Choosetime
    from PlotOnMap import PlotOnMap
    from maketxtfile import maketxtfile
    from PlotSkyView import PlotSkyView
    #create time vector (1 time value)
    import psutil
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
    for j in range (0, len(line0)):
        Carthesian = (SGP4(line1[j], line2[j], year[k], month[k], day[k], hour[k], minute[k], second[k]))
        time = (year[k], month[k], day[k], hour[k], minute[k], second[k])

        cartesianvector.append(Carthesian)
        inview, latitude, longitude, elevation, azimuth = Continue(Carthesian[0], time, Rstation, DeltaLat, DeltaLon, minelevation)
        
        elevationvector.append(elevation)
        azimuthvector.append(azimuth)
        inviewvector.append(inview)
        latitudevector.append(latitude)
        longitudevector.append(longitude)
        timevector.append([time])
        j +=1
        
        
        CPU = psutil.cpu_percent()
        # print('CPU usage = ', CPU)

    #make txt file
    

    maketxtfile(inviewvector,line0,elevationvector,azimuthvector, 0, satelliteindex, timevector, 0, frequency, latitudevector, longitudevector)

    #plot all sats on map
    PlotOnMap(latitudevector, longitudevector, timevector, inviewvector, PosStation, 0, mode, satelliteindex, line0, 0, elevationvector, azimuthvector)

    #plot view of sky
    # PlotSkyView(inviewvector, elevationvector, azimuthvector)

    
    print("done")
    
    return

