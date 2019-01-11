def AzimuthCalc(N, E, Rstation, RsatRotated):
    import numpy as np 
    
    # print('azi calc')
    N = np.asarray(N)
    E = np.asarray(E)
    Rstation = np.asanyarray(Rstation)
    RsatRotated = np.asanyarray(RsatRotated)

    # print(N)
    # print(E)
    # print(Rstation)
    # print(RsatRotated)

    x = RsatRotated-Rstation
    # print(x)
    MN = x.dot(N)/(N.dot(N))
    ME = x.dot(E)/(E.dot(E))
    # print(MN)
    # print(ME)
    A = MN*N + ME*E
    

    # print(A)
    NN =np.linalg.norm(N)
    AA =np.linalg.norm(A)

    Azimuth = np.arccos(N.dot(A)/(NN*AA))*180/np.pi
    if A[1]<0:
        Azimuth = 360-Azimuth

    # print(Azimuth)
    return(Azimuth)
