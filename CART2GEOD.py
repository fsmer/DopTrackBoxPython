def CART2GEOD(p):
    import numpy as np
    # HEIGHT DOESNT MAKE SENCE
    # https://stackoverflow.com/questions/41966945/ecef-to-lla-lat-lon-alt-in-python? 
    x = p[0]*1000
    y = p[1]*1000
    z = p[2]*1000

    a = 6378137
    asq = a*a

    e = 0.081819190842622
    esq = e*e

    b = np.sqrt(asq*(1-esq))
    bsq = b*b

    ep = np.sqrt((asq-bsq)/bsq)
    p = np.sqrt(x*x + y*y)
    th = np.arctan2(a*z, b*p)

    lon = np.arctan2(y,x)
    lat = np.arctan2( (z + ep*ep*b*np.power(np.sin(th), 3)), (p - esq*a*np.power(np.cos(th), 3)) )
    N = a/(np.sqrt(1-esq*np.power(np.sin(lat),2)))
    alt = p/np.cos(lat) - N

    lat = lat*180/np.pi
    lon = lon*180/np.pi
    
    alt = alt/1000
    return (lat, lon, alt)
