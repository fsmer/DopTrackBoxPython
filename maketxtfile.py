def maketxtfile(inviewvector,line0,elevationvector,azimuthvector,mode):
    import os


    if os.path.isfile("inview.txt"):
        os.remove("inview.txt")

    file = open("inview.txt", 'w')
    length = len(inviewvector)

    if mode == 0:
        file.write("Satellite" "\t" "Inview" "\t" "Elevation" "\t" "Azimuth" "\n" "\n")
        for i in range(0,length):
            if inviewvector[i] ==True:
                file.write(line0[i])
                file.write("\t")
                file.write("Now")
                file.write("\t")
                file.write('%d' %(elevationvector[i]))
                file.write("\t")
                file.write('%d' %(azimuthvector[i]))
                file.write("\t")
                file.write("\n")
        
    
    file.close()
    return 