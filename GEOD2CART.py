def GEOD2CART(p):

    import numpy as np
    # https://gssc.esa.int/navipedia/index.php/Ellipsoidal_and_Cartesian_Coordinates_Conversion
    #works fine if on earth about 4 km 
    a = 6378.1
    b = 6356.8
    esq =(a*a - b*b)/(a*a)

    # lon an lat are turned around??
    lon = p[0]/180*np.pi
    lat = p[1]/180*np.pi
    h = p[2]
    
    N = a / np.sqrt(1 - esq*np.power(np.sin(lon),2))

    X = ((N+h)*np.cos(lon)*np.cos(lat))
    Y = ((N+h)*np.cos(lon)*np.sin(lat))
    Z = ((1-esq)*N+h)*np.sin(lon)


    
    return [X, Z, Y]