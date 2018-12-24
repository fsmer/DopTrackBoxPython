
def FormatYML(Eazimuth, Elevation, Length, Sazimuth, timeUTC,  timezone, line1, line2, start, numsample, samplerate, time1, time2, time3, antenna, ID, name, priority, freq, stat1, stat2, stat3, stat4): 

    yml = 'Sat: \n\tPredict: \n' 
    yml = yml+ '\t\tEazimuth: '+  str(Eazimuth) + '\n'
    yml = yml+ '\t\tElevation: ' + str(Elevation) + '\n'
    yml = yml+ '\t\tLength of pass: ' + str(Length) + '\n'
    yml = yml+ '\t\tSazimuth: ' + str(Sazimuth) + '\n'
    yml = yml+ '\t\ttime Used UTC: ' + str(timeUTC) + '\n'
    yml = yml+ '\t\ttimezone used: ' + str(timezone) + '\n'
    yml = yml+ '\t\tused TLE line1: ' + str(line1) + '\n'
    yml = yml+ '\t\tused TLE line2: ' + str(line2) + '\n'
    
    yml = yml+ '\tRecord: \n'
    yml = yml+ '\t\tStart of recording: ' + str(start) + '\n'
    yml = yml+ '\t\tnum_sample: ' + str(numsample) + '\n'
    yml = yml+ '\t\tsample_rate: ' + str(samplerate) + '\n'
    yml = yml+ '\t\ttime1 UTC: ' + str(time1) + '\n'
    yml = yml+ '\t\ttime2 UTC: ' + str(time2) + '\n'
    yml = yml+ '\t\ttime3 LT: ' + str(time3) + '\n'

    yml = yml+ '\tState: \n'
    yml = yml+ '\t\tAntenna: ' + str(antenna) + '\n'
    yml = yml+ '\t\tNORADID: ' + str(ID) + '\n'
    yml = yml+ '\t\tName: ' + str(name) + '\n'
    yml = yml+ '\t\tPriority: ' + str(priority) + '\n'
    yml = yml+ '\t\tTuning Frequency: ' + str(freq) + '\n'

    yml = yml+ '\tStation: \n'
    yml = yml+ '\t\tHeight: ' + str(stat1) + '\n'
    yml = yml+ '\t\tLat: ' + str(stat2) + '\n'
    yml = yml+ '\t\tLon: ' + str(stat3) + '\n'
    yml = yml+ '\t\tName: ' + str(stat4) + '\n'


    #print(yml)

    return(yml)


