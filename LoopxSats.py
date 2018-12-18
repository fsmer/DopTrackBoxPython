def LoopxSats(mode, line0, line1,line2,Rstation, index,indexvector):
    #first check priority list?

    #create time vector from -2 hour to 2 hour                120 minutes forward 120 minutes back
    year, month, day, hour, minute, second = Choosetime(0, 0, 120, 120)
    #isolate 
    indexer = []
    lenindexvector = len(indexvector)
    indexer.append(index)
    if lenindexvector > 0:
        
        for i in range(0,lenindexvector-1):
            indexer.append(indexvector[i])
        

    for l in range(0,len(indexer)):
        j = indexer[l]
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

        cartesianvector.append(cartesianvector[j])
        elevationvector.append(elevationvector[j])
        azimuthvector.append(azimuthvector[j])
        inviewvector.append(inviewvector[j])
        latitudevector.append(latitudevector[j])
        longitudevector.append(longitudevector[j])
        timevector.append(timevector[j])

        j +=1
