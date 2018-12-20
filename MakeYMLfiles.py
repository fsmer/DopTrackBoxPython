def MakeYMLfiles(mode, line0, line1,line2,Rstation,index, indexvector, loopdays, loophours, loopminutes, PosStation, minback, priorityvector):
    
    from SGP4 import SGP4
    from Continue import Continue
    from Choosetime import Choosetime   
    from PlotOnMap import PlotOnMap
    import datetime
    import os 
    #make yml files for all sattelites but with priority vector
    #select satellite (J) run until in sight store when in sight run until out of sight store when out of sight
    #append in index J
    #select next satellite and run again
    #what if it ends in view
    year, month, day, hour, minute, second, regionaltime = Choosetime(loopdays, loophours, loopminutes, 0) #run time selection

    indexer = []
    cartesianvector = []
    elevationvector = []
    azimuthvector = []
    inviewvector = []
    latitudevector = []
    longitudevector = []
    timevector = []

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

            #Split passings, needed inviewvector and time

        secondline = line2[j]
        IDTLE = str(secondline[2:7])
        namesat = line0[j]           

        beginpassing = []
        endpassing = []
        beginregional = []
        #begin or end is in passing
        if inviewvector[0] is True:
             beginpassing.append(0)
             
    
        for j in range(1, len(inviewvector)):
             if inviewvector[j]  is True and inviewvector[j-1] is False:
                beginpassing.append(j)
                beginregional.append(regionaltime[j])
                j=j+1
             elif inviewvector[j]  is False and inviewvector[j-1] is True:
                 endpassing.append(j)

        if inviewvector[len(inviewvector)-1] is True:
             endpassing.append(len(inviewvector)-1)

        oldpath = os.getcwd()
        path = oldpath + '/YML'
        try:
            os.rmdir(path)
        except:
            print('')
        os.makedirs(path, mode=511, exist_ok= False)
        os.chdir(path)

        
        

        for m in range(0, len(beginpassing)):
             beginregional1 = beginregional[m]
             beginregionaldate = [str(beginregional1.year), str(beginregional1.month), str(beginregional1.day), str(beginregional1.hour), str(beginregional1.minute)]
             filename = namesat.rstrip()+ '_' + IDTLE + '_' + ''.join(beginregionaldate) +'.yml'
             file = open(filename, 'w')
             file.write('test')
             file.close()
             
        print(beginpassing, endpassing)
        os.chdir(oldpath)

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