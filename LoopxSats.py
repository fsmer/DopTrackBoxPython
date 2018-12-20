def LoopxSats(mode, line0, line1,line2,Rstation,index, indexvector, loopdays, loophours, loopminutes, PosStation, minback):
    from SGP4 import SGP4
    from Continue import Continue
    from Choosetime import Choosetime   
    from PlotOnMap import PlotOnMap
    from maketxtfile import maketxtfile
    
    
    


    #create time vector from -2 hour to 2 hour                #add run time
    year, month, day, hour, minute, second, regionaltime = Choosetime(loopdays, loophours, loopminutes, minback)
    #isolate 
    indexer = []
    cartesianvector = []
    elevationvector = []
    azimuthvector = []
    inviewvector = []
    latitudevector = []
    longitudevector = []
    timevector = []

    lenindexvector = len(indexvector)

    if lenindexvector > 0:
        
        for i in range(0,lenindexvector-1):
            indexer.append(indexvector[i])

    else:
        indexer.append(index)
        
    print(indexer)
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
            

    #make txt file
    maketxtfile(inviewvector,line0,elevationvector,azimuthvector,mode, indexer, timevector)
    #make yml file
    # makeyamlfile()
    #plot all sats on map
    PlotOnMap(latitudevector, longitudevector, timevector, inviewvector,PosStation)
    print("done")
    #plot view of sky
    #plotinsight()

    


