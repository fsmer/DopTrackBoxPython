
def SatElevation(station , sat):
    import numpy as np
    #we have to do vector operations so get numpy and get vectors going

    #check if input is actually possible to work with
    P = sat
    S = station

    O = P-S
    normP = np.linalg.norm(P)
    normS = np.linalg.norm(S)

    OSdefOS = O.dot(S)/(normP*normS)

    omega = np.arccos(OSdefOS)
    elev = omega*180/np.pi-90
    azi = 0
    
    return (elev, azi)