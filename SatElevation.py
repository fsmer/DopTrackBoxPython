def SatElevation(station , sat):
    import numpy as np
    #we have to do vector operations so get numpy and get vectors going

    #check if input is actually possible to work with
    P = sat
    S = station


    O = P-S

    normS = np.linalg.norm(S)
    normO = np.linalg.norm(O)

   
    OSdefOS = O.dot(S)/(normS*normO)

    omega = np.arccos(OSdefOS)
 
    elev =  (omega*180/np.pi - 90)*-1
   
    azi = 0


    return (elev, azi)