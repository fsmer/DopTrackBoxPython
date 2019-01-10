def LoopxSats(mode, line0, line1,line2,Rstation,index, indexvector, loopdays, loophours, loopminutes, PosStation, minback):
    from SGP4 import SGP4
    from Continue import Continue
    from Choosetime import Choosetime   
    from PlotOnMap import PlotOnMap
    from maketxtfile import maketxtfile
    
    
    
    #in order to plot backward we add a minutes back this should not be used in the output I guess but only in the forward. 

    #create time vector from -2 hour to 2 hour                #add run time
    if minback < 10:
        minback = 10
    time1, year, month, day, hour, minute, second, regionaltime = Choosetime(loopdays, loophours, loopminutes, minback)

    samplesback = minback
    
    #isolate 
    indexer = []
    cartesianvector = []
    elevationvector = []
    azimuthvector = []
    inviewvector = []
    latitudevector = []
    longitudevector = []
    timevector = []
    
    xelevationvector = []
    xazimuthvector = []
    xinviewvector = []
    xlatitudevector = []
    xlongitudevector = []
    xtimevector = []

    lenindexvector = len(indexvector)

    if lenindexvector > 0:
        
        for i in range(0,lenindexvector):
            indexer.append(indexvector[i])

    else:
        indexer.append(index)
        
    # indexer klopt nu niet
    # print("indexer" '%s' %(indexer))

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

        # print(inviewvector)
        # all of them are now in dubble brackets which is not needed can be removed but then also has to be remove din the next files
        xelevationvector.append(elevationvector)
        xazimuthvector.append(azimuthvector)
        xinviewvector.append(inviewvector)
        xlatitudevector.append(latitudevector)
        xlongitudevector.append(longitudevector)
        xtimevector.append(timevector)
        

        cartesianvector = []
        elevationvector = []
        azimuthvector = []
        inviewvector = []
        latitudevector = []
        longitudevector = []
        timevector = []




    

    #make txt file
    maketxtfile(xinviewvector,line0,xelevationvector,xazimuthvector,mode, indexer, xtimevector, samplesback)
    #make yml file
    # makeyamlfile()
    #plot all sats on map
    PlotOnMap(xlatitudevector, xlongitudevector, xtimevector, xinviewvector, PosStation, samplesback, mode, index, line0, indexer)
    print("done")
    #plot view of sky
    #plotinsight()
