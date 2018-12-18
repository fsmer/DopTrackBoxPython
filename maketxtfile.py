def maketxtfile(inviewvector,line0,elevationvector,azimuthvector,mode, indexer, timevector):
    import os


    if os.path.isfile("inview.txt"):
        os.remove("inview.txt")

    file = open("inview.txt", 'w')
    length = len(inviewvector)

    if mode == 0:
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
        if len(indexer) == 1:
            file.write("Satellite" '%s' %(line0[indexer[0]]))
            file.write("\n")
            file.write("Start time" "\t" "End time" "\t" "Maximum elevation" "\t" "Start azimuth" "\t" "End azimuth" "\n")

            print(inviewvector)
            inviewvector[0] = False
            inviewvector[len(inviewvector-1)] = False

            for i in range(0,len(inviewvector)-1):
                maxelevation = 0
                if elevationvector[i] > maxelevation:
                    maxelevation = elevationvector[i]

                if (inviewvector[i] == False) & (inviewvector[i+1] == True):
                    file.write('%s' %(timevector[i]))
                    file.write("\t")
                    startazimuth = azimuthvector[i]

                elif (inviewvector[i] == True) & (inviewvector[i+1] == False):
                    file.write('%s' %(timevector[i]))
                    file.write("\t")
                    file.write('%d' %(maxelevation))
                    file.write("\t")
                    file.write('%d' %(startazimuth))
                    file.write("\t")
                    file.write('%d' %(azimuthvector[i]))
                    file.write("\n")
                    maxelevation = 0

    file.close()
    return 