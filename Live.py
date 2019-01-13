def Live(mode, line0, line1,line2,Rstation, PosStation, DeltaLat, DeltaLon, index):
    from SGP4 import SGP4
    from Continue import Continue
    from Choosetime import Choosetime
    from datetime import datetime
    import psutil
    #create time vector (1 time value)

    startcalctime= datetime.now()

    time1, year, month, day, hour, minute, second, regionaltime = Choosetime(0, 0, 1, 0)

    

    cartesianvector = []
    elevationvector = []
    azimuthvector = []
    inviewvector = []
    latitudevector = []
    longitudevector = []
    timevector = []

    latitudevector.clear()
    longitudevector.clear()
  
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

        #CPU = psutil.cpu_percent()
        #print('CPU usage = ', CPU)



    endcalctime = datetime.now()
    calculatingtime = endcalctime - startcalctime
    print('Time calculating = ', calculatingtime)
    print("done")

    return(latitudevector,longitudevector, time)

