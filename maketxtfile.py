def maketxtfile(inviewvector,line0,elevationvector,azimuthvector,mode, indexer, timevector, samplesback, frequency, latitudevector, longitudevector):
    import os
    import webbrowser
    if os.path.isfile("inview.txt"):
        os.remove("inview.txt")

    file = open("inview.txt", 'w')

    

    if mode == 0:
        length = len(inviewvector)
        
        file.write("Inview Now")
        file.write("\n")
        file.write("--------------------------------------------------------------------")
        file.write("\n")
        file.write("Satellite" "\t" "\t" "\t" "\t"   "Elevation" "\t" "Azimuth" "\t""\t" "Frequency" "\t""\t""\t" "Latitude" "\t""\t" "\t""Longitude""\n"  )
        file.write("\n")
        for i in range(0,length):
            if inviewvector[i] ==True:
                file.write(line0[i])
                file.write("\t" "\t" )
                file.write('%d' %(elevationvector[i]))
                file.write("\t" "\t" )
                file.write('%d' %(azimuthvector[i]))
                file.write("\t" "\t" )
                file.write('%s' %(frequency[i]))
                if len(frequency[i]) < 1:
                    file.write("\t" )
                if len(frequency[i]) < 16:
                    file.write("\t" )
                file.write("\t""\t"  )
                file.write('%s' %(latitudevector[i]))
                file.write("\t" "\t" )
                file.write('%s' %(longitudevector[i]))
                file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("Not inview")
        file.write("\n")
        file.write("--------------------------------------------------------------------")
        file.write("\n")
        file.write("Satellite" "\t" "\t" "\t" "\t"  "Elevation""\t" "Azimuth" "\t" "\t""Frequency" "\n" )
        file.write("\n")
        for j in range(0,length):
            if inviewvector[j] ==False:
                file.write(line0[j])
                file.write("\t" "\t" )
                file.write('%d' %(elevationvector[j]))
                file.write("\t" "\t" )
                file.write('%d' %(azimuthvector[j]))
                file.write("\t" "\t" )
                file.write('%s' %(frequency[j]))
                if len(frequency[j]) < 1:
                    file.write("\t" )
                if len(frequency[j]) < 16:
                    file.write("\t" )
                file.write("\t""\t"  )
                file.write('%s' %(latitudevector[i]))
                file.write("\t" "\t" )
                file.write('%s' %(longitudevector[i]))
                file.write("\n")
    
    if mode == 1:   #mode 1 we have an index andor a indexvector 
                    # we also route it back a little bit first we can just filter them out later
        for k in range(0,len(indexer)):

            file.write("Satellite:" "\t"  '%s' %(line0[indexer[k]]))
            file.write("\n")
            file.write("Frequency:" "\t" '%s' %(frequency[indexer[k]]))
            file.write("\n")
            file.write("Start time" "\t" "\t"  "\t" "End time" "\t" "\t"  "\t" "Maximum elevation" "\t"  "Maximum azimuth""\t" "\t"  "Start azimuth""\t"  "\t""End azimuth"    "\n")

            # print("first loop")
            # print(elevationvector[k][0][0])

            runlen = len(inviewvector[0])
            # print(runlen)
            inviewvector[k][0]= False
            inviewvector[k][samplesback]= False
            inviewvector[k][(runlen-2)] = False
            inviewvector[k][(runlen-1)] = False
            maxelevation = 0
            startazimuth = 0
            maxazimuth = 0
      
            for i in range(samplesback, runlen-2):
                # print(i)
                # print(elevationvector[0][0][i])
                if elevationvector[k][i] > maxelevation:
                    maxelevation = elevationvector[k][i]
                    maxazimuth = azimuthvector[k][i]


                if ((inviewvector[k][i] == False) and (inviewvector[k][i+1] == True)):
                    file.write('%s'"-"'%s'"-"'%s' " " '%s'":"'%s'":"'%s' %(timevector[k][i+1])) 
                    # if (((timevector[k][i][3] < 10) and (timevector[k][i][4] < 10) ) or ((timevector[k][i][4] < 10) and (timevector[k][i][5] < 10)) or ((timevector[k][i][3] < 10) and (timevector[k][i][5] < 10))):
                    #     file.write("\t")
                    file.write("\t" "\t")
                    startazimuth = azimuthvector[k][i+1]

                elif ((inviewvector[k][i] == True) and (inviewvector[k][i+1] == False)):
                    file.write('%s'"-"'%s'"-"'%s' " " '%s'":"'%s'":"'%s'  %(timevector[k][i]))
                    # if ((timevector[k][i][3] < 10) or (timevector[k][i][4] < 10) or (timevector[k][i][5] < 10) ):
                    #     file.write("\t")
                    file.write("\t" "\t" )
                    file.write('%d' %(maxelevation))
                    file.write("\t"  "\t" "\t" )
                    file.write('%d' %(maxazimuth))
                    file.write("\t"  "\t" "\t" )
                    file.write('%d' %(startazimuth))
                    file.write("\t""\t" "\t" )
                    file.write('%d' %(azimuthvector[k][i]))
                    file.write("\n")
                    file.write("\n")
                    maxelevation = 0

            file.write("----------------------------------------------------------------------------------------------------------------------------------------------")
            file.write("\n")

    file.close()

    webbrowser.open("inview.txt")

    

    return 