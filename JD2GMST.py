def JD2GMST(JD):  
    import numpy as np

    #find the JD from the previous midnight JD0
    JDmin = np.floor(JD)-0.5
    JDmax = np.floor(JD)+0.5

    #if the distance is negative it means that JDmax is the next midnight
    if (JD-JDmax)<0:
        JD0 = JDmin
    else:
        JD0 = JDmax

    
    H = (JD-JD0)*24 # hours past previous midnight
    D = JD-2451545 #compute number of days since J2000 (has already been calculated earlier but shhh)
    D0 = JD0-2451545  #Compute the number of days since J2000
    T = D/36525 #Compute number of centuries since J2000

    GMST = np.remainder(6.697374558+0.06570982441908*D0+1.00273790935*H +0.000026*(T*T),24)*15
    return (GMST)