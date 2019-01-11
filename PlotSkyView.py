def PlotSkyView(inviewvector, elevationvector, azimuthvector):
    import numpy as np
    import matplotlib.pyplot as plt
    
    fig2, ax1 = plt.subplot( projection='polar')
    
    ax1.set_rmax(90)
    ax1.set_rticks([15, 30, 45, 60,75,90])  # less radial ticks
    ax1.set_rlabel_position(-112.5)  # get radial labels away from plotted line
    ax1.set_theta_zero_location("N")
    ax1.grid(True)
    

    ax1.set_title("Sky View", va='bottom')
    for i in range(0,len(inviewvector)):
        if inviewvector[i] == True:
            plt.figure(2)
            ax1.plot(azimuthvector[i], elevationvector[i], 'b.')
    
    plt.show(block=False)
    