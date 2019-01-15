def MakeYMLfiles(mode, line0, line1,line2,Rstation,index, indexvector, loopdays, loophours, loopminutes, PosStation, minback, priorityvector, priority, info, DeltaLat, DeltaLon):
    
    from SGP4 import SGP4
    from Continue import Continue
    from Choosetime import Choosetime   
    from PlotOnMap import PlotOnMap
    from FormatYML import FormatYML
    from tzlocal import get_localzone
    import datetime
    import os 
    import shutil
    import psutil
    #make yml files for all sattelites but with priority vector
    #select satellite (J) run until in sight store when in sight run until out of sight store when out of sight
    #append in index J
    #select next satellite and run again
    #what if it ends in view
    oldpath = os.getcwd()
    path = oldpath + '/YML'
    try:
        shutil.rmtree(path)
    except:
        print('')
    os.makedirs(path, mode=511, exist_ok= False)
    os.chdir(path)


    time1, year, month, day, hour, minute, second, regionaltime = Choosetime(loopdays, loophours, loopminutes, 0) #run time selection
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
        indexer = index
        amount = 1
    else:
        indexer = indexvector
        amount = len(indexer)
        

    for l in range(0,amount):
        if amount is 1:
            j = index
        else:
            j = indexer[l]

        # Do the calculations
        for k in range(0,len(year)-1):

            Carthesian = (SGP4(line1[j], line2[j], year[k], month[k], day[k], hour[k], minute[k], second[k]))
            cartesianvector.append(Carthesian)

            time = (year[k], month[k], day[k], hour[k], minute[k], second[k])

            inview, latitude, longitude, elevation, azimuth = Continue(Carthesian[0], time, Rstation, DeltaLat, DeltaLon)
            elevationvector.append(elevation)
            azimuthvector.append(azimuth)
            inviewvector.append(inview)
            latitudevector.append(latitude)
            longitudevector.append(longitude)
            timevector.append(time)
            
        #Split passings, needed inviewvector and time
        firstline = line1[j]
        secondline = line2[j]
        IDTLE = str(secondline[2:7])
        namesat = line0[j]   
        freq = info[j]
        if len(priorityvector) is 0:
            pio = priority
        else:
            pio = priorityvector[l]

        beginpassing = []
        endpassing = []
        beginregional = []
        beginUTC = []
        endUTC = []
        
        #begin or end is in passing
        if inviewvector[0] is True:
             beginpassing.append(0)
             beginregional.append(regionaltime[0])
             beginUTC.append(time1[0])
             
        for j in range(1, len(inviewvector)):
             if inviewvector[j]  is True and inviewvector[j-1] is False:
                beginpassing.append(j)
                beginregional.append(regionaltime[j])
                beginUTC.append(time1[j])
             elif inviewvector[j]  is False and inviewvector[j-1] is True:
                 endpassing.append(j)
                 endUTC.append(time1[j])

        if inviewvector[len(inviewvector)-1] is True:
             endpassing.append(len(inviewvector))
             endUTC.append(time1[len(inviewvector)])

        #print(inviewvector)
        #print(beginpassing, endpassing)

        # Write data to file
        if len(beginpassing) is not 0:
            for m in range(0, len(beginpassing)):
                 beginregional1 = beginregional[m]
                 timezone = get_localzone()
                 beginregionaldate = [str(beginregional1.year), str(beginregional1.month), str(beginregional1.day), str(beginregional1.hour), str(beginregional1.minute)]
                 beginUTCdate = [str(beginUTC[m].year), str(beginUTC[m].month), str(beginUTC[m].day), str(beginUTC[m].hour), str(beginUTC[m].minute)]
                 timedelta = (endUTC[m]-beginUTC[m]).total_seconds()

                 elevationpass = elevationvector[beginpassing[m]:endpassing[m]]
                 maxelevation = max(elevationpass)

                 numsample = timedelta*PosStation[4]

                 yml = FormatYML(azimuthvector[endpassing[m]], maxelevation, int(timedelta), azimuthvector[beginpassing[m]], ''.join(beginUTCdate), timezone, firstline, secondline, ''.join(beginregionaldate), numsample, PosStation[4], '', '', '', 'ANTENNA', IDTLE, namesat, pio, freq, PosStation[2], PosStation[1], PosStation[0], PosStation[3])

                 filename = namesat.rstrip()+ '_' + IDTLE + '_' + ''.join(beginregionaldate) +'.yml'
                 file = open(filename, 'w')
                 file.write(yml)
                 file.close()

                 CPU = psutil.cpu_percent()
                 print('CPU usage = ', CPU)

        # Clear all the vectors
        elevationvector.clear()
        azimuthvector.clear()
        inviewvector.clear()
        latitudevector.clear()
        longitudevector.clear()
        timevector.clear()
        beginpassing.clear()
        endpassing.clear()
        beginregional.clear()
        beginUTC.clear()
        endUTC.clear()
        #print(l)

    os.chdir(oldpath)

    #make txt file
    #maketxtfile()
    #make yml file
    # makeyamlfile()
    #plot all sats on map
    #PlotOnMap(latitudevector, longitudevector, timevector, inviewvector,PosStation)
    print("done")
    #plot view of sky
    #plotinsight()