
def Insight(station, sat):
    import numpy as np
    
    #we need sat location and groundstation location in carthesian
    sat = np.asarray(sat)
    station = np.asanyarray(station)

    # print(sat)
    # print(station)
    # print(h)

    R = 6371
    Rsat = np.linalg.norm(sat)
    Rstat =np.linalg.norm(station)

    RdefRH = R/(Rsat)
    Rdotr = station.dot(sat)
    RdotrdefRr = Rdotr/(Rsat*Rstat)

    # print(RdefRH)
    # print(RdotrdefRr)

    if RdefRH >= RdotrdefRr:
        out = False
    else:
        out = True
    # print(out)
    return out