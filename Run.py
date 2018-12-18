def Run(mode1, line0, line1, line2, PosStation, satelliteindex, indexvector, priorityvector, loopdays, loophours, loopminutes, minback):
    from LoopallSats import LoopallSats
    from GEOD2CART import GEOD2CART
    from LoopxSats import LoopxSats
    from MakeYMLfiles import MakeYMLfiles
    
    #select path to run
    #Posstation might be 3 seperate numbers


    Rstation = GEOD2CART(PosStation)
    mode = mode1
 

    if mode == 0:
        LoopallSats(mode, line0, line1,line2,Rstation, PosStation, satelliteindex)
    elif mode == 1:
        #in the UI the priority list is added to the plot and also the one selected now. In case no priority list then just satelliteindex
        LoopxSats(mode, line0, line1,line2,Rstation,satelliteindex, indexvector, loopdays, loophours, loopminutes, PosStation, minback)
    elif mode == 2:
        MakeYMLfiles(mode, line0, line1,line2,Rstation)
    elif mode == 3:
        # LifeUpdating(mode, line0, line1,line2,Rstation)
        print("LifeUpdating mode has not yet been developed")
    else:
        print("Mode Error")

