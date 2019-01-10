def LoopxSats(mode, line0, line1,line2,Rstation,index, indexvector, loopdays, loophours, loopminutes, PosStation, minback):
    from SGP4 import SGP4
    from Continue import Continue
    from Choosetime import Choosetime   
    from PlotOnMap import PlotOnMap
    import psutil
 
    
    
    
    


    #create time vector from -2 hour to 2 hour                #add run time
    time1, year, month, day, hour, minute, second, regionaltime = Choosetime(loopdays, loophours, loopminutes, minback)
    #isolate 
    indexer = []
    cartesianvector = []
    elevationvector = []
    azimuthvector = []
    inviewvector = []
    latitudevector = []
    longitudevector = []
    timevector = []
    CPUvector = []

    lenindexvector = len(indexvector)
    if lenindexvector is 0:
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

            CPU = psutil.cpu_percent()
            print('CPU usage = ', CPU)

            

        cartesianvector.append(cartesianvector[l])
        elevationvector.append(elevationvector[l])
        azimuthvector.append(azimuthvector[l])
        inviewvector.append(inviewvector[l])
        latitudevector.append(latitudevector[l])
        longitudevector.append(longitudevector[l])
        timevector.append(timevector[l])

        

      

    #make txt file
    #maketxtfile()
    #make yml file
    # makeyamlfile()
    #plot all sats on map
    PlotOnMap(latitudevector, longitudevector, timevector, inviewvector,PosStation)
    print("done")
    #plot view of sky
    #plotinsight()

    


