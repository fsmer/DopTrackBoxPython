
def RotationMatrix(GAST, Position):
    import numpy as np

    # input 
    # GAST should be a number
    # Position is a list 
    #t in minutes?

    #Make an array from list and rotate the posistion to the correct shape
    a = np.asarray(Position)
    a = a.reshape(3,1)

    # w0 =   7.2921158553E-5/60
    #omega calculation from GAST
    omega = GAST/180*np.pi

    #Rotation matrix
    # [cos(omega)  sin(omega)  0;
    #  -sin(omega) cos(omega)  0;
    #  0           0           1];
    U = np.array([[np.cos(omega), np.sin(omega), 0], [-1*np.sin(omega), np.cos(omega), 0], [0, 0, 1]])

    #Rotate position array with U
    PositionR = U.dot(a) #simple dot product
    #returns an array of 1 by 3 
    PositionR = np.array(PositionR).ravel()
    return (PositionR)


