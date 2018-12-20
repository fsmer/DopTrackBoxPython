def maketxtfile(inviewvector,line0,elevationvector,azimuthvector,mode, indexer, timevector):
    import os

    if os.path.isfile("inview.txt"):
        os.remove("inview.txt")

    file = open("inview.txt", 'w')

    

    if mode == 0:
        length = len(inviewvector)
        file.write("Satellite" "\t" "\t" "\t" "\t" "\t" "Inview" "\t" "\t""Elevation" "\t" "Azimuth" "\n" "\n")
        for i in range(0,length):
            if inviewvector[i] ==True:
                file.write(line0[i])
                file.write("\t")
                file.write("Now")
                file.write("\t" "\t" "\t")
                file.write('%d' %(elevationvector[i]))
                file.write("\t" "\t" "\t")
                file.write('%d' %(azimuthvector[i]))
                file.write("\n")
        
    
    if mode == 1:   #mode 1 we have an index andor a indexvector 
                    # we also route it back a little bit first we can just filter them out later
        for k in range(0,len(indexer)):

            file.write("Satellite" '%s' %(line0[indexer[k]]))
            file.write("\n")
            file.write("Start time" "\t" "\t" "\t" "||""\t" "\t" "End time" "\t" "\t" "\t" "||"" " "Maximum elevation"" " "||" " ""Start azimuth" " ""||" " ""End azimuth" "\n")

            # print("first loop")
            # print(elevationvector[k][0][0])

            runlen = len(inviewvector[0])
            # print(runlen)
            inviewvector[k][0]= False
            inviewvector[k][(runlen-2)] = False
            inviewvector[k][(runlen-1)] = False
            maxelevation = 0
      
            for i in range(0,runlen-2):
                # print(i)
                # print(elevationvector[0][0][i])
                if elevationvector[k][0][i] > maxelevation:
                    maxelevation = elevationvector[k][0][i]


                if (inviewvector[k][i] == False) & (inviewvector[k][i+1] == True):
                    file.write('%s'"-"'%s'"-"'%s' " " '%s'":"'%s'":"'%s' %(timevector[k][0][i+1])) 
                    file.write("\t" "\t")
                    startazimuth = azimuthvector[k][0][i+1]

                elif (inviewvector[k][i] == True) & (inviewvector[k][i+1] == False):
                    file.write('%s'"-"'%s'"-"'%s' " " '%s'":"'%s'":"'%s'  %(timevector[k][0][i]))
                    file.write("\t" "\t" "\t" "\t" )
                    file.write('%d' %(maxelevation))
                    file.write("\t" "\t" "\t" "\t" "\t")
                    file.write('%d' %(startazimuth))
                    file.write("\t" "\t" "\t" "\t")
                    file.write('%d' %(azimuthvector[k][0][i]))
                    file.write("\n")
                    file.write("\n")
                    maxelevation = 0

            file.write("\n")
            file.write("\n")

    file.close()
    return 