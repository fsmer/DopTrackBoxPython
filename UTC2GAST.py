def UTC2GAST(Date):  
    import numpy as np
    from JD2GMST import JD2GMST
    
    # an option to consider is calculating this once and then adding the rotation whihch is easier.
    pi = np.pi
    # this is not compatible with vectors
    Year, Month, Day, Hour, Minute ,Second = Date
    Tday = 24*3600
    # We get a date string with Year, Month, Day, Hour, Minute ,Second
    Year = Year-2000
    #compute JulianDayFraction since 2000 January 1 12:00 
    leapyears = np.ceil(Year/4) 
    YearSec = ((Year-leapyears)*365+leapyears*366)*Tday

    if np.remainder(Year,4)==0:
        leapyear = 1
    else:
        leapyear = 0


    if Month == 1:
        MonthSec = 0
    elif Month == 2:
        MonthSec = 31*Tday
    elif Month == 3:
        MonthSec = (31+28+leapyear)*Tday
    elif Month == 4:
        MonthSec = MonthSec = (31+28+31+leapyear)*Tday
    elif Month == 5:
        MonthSec = MonthSec = (31+28+31+30+leapyear)*Tday
    elif Month == 6:
        MonthSec = MonthSec = (31+28+31+30+31+leapyear)*Tday
    elif Month == 7:
        MonthSec = MonthSec = (31+28+31+30+31+30+leapyear)*Tday
    elif Month == 8:
        MonthSec = MonthSec = (31+28+31+30+31+30+31+leapyear)*Tday
    elif Month == 9:
        MonthSec = MonthSec = (31+28+31+30+31+30+31+31+leapyear)*Tday
    elif Month == 10:
        MonthSec = MonthSec = (31+28+31+30+31+30+31+31+30+leapyear)*Tday
    elif Month == 11:
        MonthSec = MonthSec = (31+28+31+30+31+30+31+31+30+31+leapyear)*Tday
    elif Month == 12:
        MonthSec = MonthSec = (31+28+31+30+31+30+31+31+30+31+30+leapyear)*Tday
    else:
        MonthSec = 0

    #total JD time in seconds
    JDs = YearSec+MonthSec+Day*Tday+Hour*3600+Minute*60+Second-12*3600
    JDscentury = (75*365+25*366)*Tday
    #Compute amount of centuries since J2000 as in fraction from the centuries
    T = JDs/JDscentury

    # in matlab it is in days since somehwere -4700
    JD = T*36525+2451540 #days

    #Get THETAm from JD2GMST
    THETAm = JD2GMST(JD)

    EPSILONm = 23.439291-0.0130111*T-1.64E-07*(T*T*T) + 5.04E-07*(T*T*T)
    L =  280.4665+36000.7698*T
    dL = 218.3165+481267.8813*T
    OMEGA = 125.04452-1934.136261*T

    dPSI = -17.20*np.sin(OMEGA/180*pi)-1.32*np.sin(2.*L/180*pi)-0.23*np.sin(2*dL/180*pi)+.21*np.sin(2*OMEGA/180*pi)
    dEPSILON = 9.20*np.cos(OMEGA/180*pi)+0.57*np.cos(2*L/180*pi) + .10*np.cos(2*dL/180*pi)-0.09*np.cos(2*OMEGA/180*pi)

    dPSI = dPSI/3600
    dEPSILON = dEPSILON/3600
    GAST = np.remainder(THETAm + dPSI*np.cos((EPSILONm+dEPSILON)/180*pi),360)

    return (GAST)