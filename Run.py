def Run(mode1, line0, line1, line2, PosStation, satelliteindex, indexvector, priorityvector, priority, loopdays, loophours, loopminutes, minback, info):
    from LoopallSats import LoopallSats
    from GEOD2CART import GEOD2CART
    from LoopxSats import LoopxSats
    from MakeYMLfiles import MakeYMLfiles
    from datetime import datetime
    from Plotlive import Plotlive
    import psutil
    from deltacalculator import deltacalculator
    
    #select path to run
    #Posstation might be 3 seperate numbers

    startcalctime= datetime.now()
    Rstation = GEOD2CART(PosStation)
    mode = mode1
    print('test')

    DeltaLat, DeltaLon = deltacalculator(PosStation, Rstation)

    if mode == 0:
        print('Looping all satellites')
        LoopallSats(mode, line0, line1,line2,Rstation, PosStation, satelliteindex, DeltaLat, DeltaLon)
    elif mode == 1:
        #in the UI the priority list is added to the plot and also the one selected now. In case no priority list then just satelliteindex
        print('Looping x satellites')
        LoopxSats(mode, line0, line1,line2,Rstation,satelliteindex, indexvector, loopdays, loophours, loopminutes, PosStation, minback, DeltaLat, DeltaLon)
    elif mode == 2:
        print('Making YML files')
        MakeYMLfiles(mode, line0, line1,line2,Rstation,satelliteindex, indexvector, loopdays, loophours, loopminutes, PosStation, minback, priorityvector, priority, info)
    elif mode == 3:
        Plotlive(mode, line0, line1,line2,Rstation, PosStation)
        # LifeUpdating(mode, line0, line1,line2,Rstation)
        #print("LiveUpdating mode has not yet been developed")
    else:
        print("Mode Error")

    endcalctime = datetime.now()
    calculatingtime = endcalctime - startcalctime
    print('Time calculating = ', calculatingtime)
    return()

