def MakeYMLfiles(mode, line0, line1,line2,Rstation, index,indexvector, prioritylist, looptime):
    
    #make yml files for all sattelites but with priority vector
    #select satellite (J) run until in sight store when in sight run until out of sight store when out of sight
    #append in index J
    #select next satellite and run again
    #what if it ends in view
    year, month, day, hour, minute, second, regionaltime = Choosetime(0, 0, 0, 0) #run time selection

    cartesianvector = []
    elevationvector = []
    azimuthvector = []
    inviewvector = []
    latitudevector = []
    longitudevector = []
    timevector = []

    for j in range(0,len(line0)-1):
        for k in range(0,len(year)-1):

            Carthesian = (SGP4(line1[j], line2[j], year[k], month[k], day[k], hour[k], minute[k], second[k]))
            time = (year[k], month[k], day[k], hour[k], minute[k], second[k])
            inview, latitude, longitude, elevation, azimuth = Continue(Carthesian[0], time, Rstation)

            if inview == True:
                while m <1:
                    cartesianvector.append(Carthesian)
                    elevationvector.append(elevation)
                    azimuthvector.append(azimuth)
                    inviewvector.append(inview)
                    latitudevector.append(latitude)
                    longitudevector.append(longitude)
                    timevector.append(time)
                    m +=1
            else:
                while l < 1:
                    cartesianvector.append(Carthesian)
                    elevationvector.append(elevation)
                    azimuthvector.append(azimuth)
                    inviewvector.append(inview)
                    latitudevector.append(latitude)
                    longitudevector.append(longitude)
                    timevector.append(time)
                   

                    #make yml file here?
                    MakeYMLfile(line0[j], line1[j], line2[j], indexvector, prioritylist, elevationvector,timevector)
                    MakeTXTfile()
                    #reset vectors
                    cartesianvector = []
                    elevationvector = []
                    azimuthvector = []
                    inviewvector = []
                    latitudevector = []
                    longitudevector = []
                    timevector = []
                    l = l+1
  

    #make txt file
    #make yml files
        