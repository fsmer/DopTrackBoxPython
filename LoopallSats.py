def LoopallSats(mode, line0, line1, line2)

    #create time vector (1 time value)
    year, month, day, hour, minute, second = Choosetime(0, 0, 0, 0)

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
    maketxtfile()
    #make yml file
    makeyamlfile()
    #plot all sats on map
    plotonmap
    #plot view of sky
    plotinsight
