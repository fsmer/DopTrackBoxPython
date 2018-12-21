def ReadTLE():
    import requests

    file = open("TLE.txt", 'r')
    TLEold = file.read()
    file.close()

    TLE = TLEold.split("\\r\\n")
    #Remove extra from download
    lengthTLE = len(TLE)
    TLE = TLE[:(lengthTLE-1)]
    TLE0 = TLE[0]
    TLE0 = TLE0[2:]
    TLE[0] = TLE0

    #split lines
    zerolines = TLE[0::3]
    firstlines = TLE[1::3]
    secondlines = TLE[2::3]

    #split ID
    IDTLE = []
    for j in range (0,len(secondlines)):
        secondline = secondlines[j]
        IDTLE.append(secondline[2:7])

    ############################################################################################################
    file = open("Freq.txt", 'r')
    freqold = file.read()
    file.close()

    freq= freqold.split("\\r\\n")

    #split colomns
    satnamefreq = []
    IDfreq = []
    uplink = []
    downlink = []
    beacon = []
    mode = []
    callsign = []
    active = []

    for i in range(0, len(freq)-1):
        freq1 = str(freq[i])
        freq1 = freq1.split(";")
        satnamefreq.append(freq1[0])
        IDfreq.append(freq1[1])
        uplink.append(freq1[2])
        downlink.append(freq1[3])
        beacon.append(freq1[4])
        mode.append(freq1[5])
        callsign.append(freq1[6])
        active.append(freq1[7])
 


    j = 0
    #print(satnamefreq[j],ID[j], uplink[j], downlink[j], active[j])
    #write file
    file = open("Freq.txt", 'w')
    file.write(freqold)
    file.close()


    #Check for same ID and remove inactive 
    info = []
    info1 = []
    line0 = []
    line1 = []
    line2 = []

    notactive = 'inactive'
    for k in range (0,len(IDTLE)-1):
            if IDTLE[k] in IDfreq:
                m = IDfreq.index(IDTLE[k],0,len(IDfreq)-1)
                if notactive not in active[m]:
                    info.append(downlink[m])
                    info1.append(active[m])
                    line0.append(zerolines[k])
                    line1.append(firstlines[k])
                    line2.append(secondlines[k])

    #print(line0, info)
    #print(info1)
    return(line0, line1, line2, info)