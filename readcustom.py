def readcustom():
    from ReadTLE import ReadTLE

    line0,line1,line2, info  = ReadTLE()

    locvector = []
    fileloc = open("fileloc.txt", "r")
    locv1 = fileloc.readlines()
    for i in range (0, len(locv1)):
        locvector.append(str(locv1[i]).rstrip())
    fileloc.close
    #print(locvector)

    lonvector = []
    filelon = open("filelon.txt", "r")
    lonv1 = filelon.readlines()
    for i in range (0, len(lonv1)):
        lonvector.append(str(lonv1[i]).rstrip())
    filelon.close
    #print(lonvector)

    latvector = []
    filelat = open("filelat.txt", "r")
    latv1 = filelat.readlines()
    for i in range (0, len(latv1)):
        latvector.append(str(latv1[i]).rstrip())
    filelat.close
    #print(latvector)

    hvector = []
    fileh = open("fileh.txt", "r")
    hv1 = fileh.readlines()
    for i in range (0, len(hv1)):
        hvector.append(str(hv1[i]).rstrip())
    fileh.close
    #print(hvector)
    try: 
        file0 = open("file0.txt", "r")
        added0 = file0.readlines()
        for i in range (0, len(added0)):
            line0.append(str(added0[i]).rstrip())
        file0.close
        #print(line0)

        file1 = open("file1.txt", "r")
        added1 = file1.readlines()
        for i in range (0, len(added1)):
            line1.append(str(added1[i]).rstrip())
        #print(line1)
        file1.close

        file2 = open("file2.txt", "r")
        added2 = file2.readlines()
        for i in range (0, len(added2)):
            line2.append(str(added2[i]).rstrip())
        file2.close
        #print(line2)

        filedownlink = open("downlink.txt", "r")
        addeddownlink = filedownlink.readlines()
        for i in range (0, len(addeddownlink)):
            info.append(str(addeddownlink[i]).rstrip())
        filedownlink.close
        #print(info)
        return (locvector, lonvector, latvector, hvector, line0, line1, line2, info )
    except:
        return (locvector, lonvector, latvector, hvector, line0, line1, line2, info )
