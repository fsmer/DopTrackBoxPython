def Run(mode, line0, line1, line2, PosStation,prioritylist, index, indexvector, priorityvector)
#select path to run
#Posstation might be 3 seperate numbers


Rstation = GEOD2CART(PosStation)


if mode == 0:
    LoopallSats(mode, line0, line1,line2,Rstation)
elif mode == 1:
    #in the UI the priority list is added to the plot and also the one selected now. In case no priority list then just satelliteindex
    LoopxSats(mode, line0, line1,line2,Rstation, prioritylist ,index, indexvector)
elif mode == 2:
    MakeYMLfiles(mode, line0, line1,line2,Rstation)
elif mode == 3:
    LifeUpdating(mode, line0, line1,line2,Rstation)
else:
    print("Mode Error")

