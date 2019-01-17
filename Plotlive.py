def Plotlive(mode, line0, line1,line2,Rstation, Posstation, DeltaLat, DeltaLon, index):
    import matplotlib.pyplot as plt
    import numpy as np
    import datetime
    from Live import Live
    import matplotlib.animation as animation
    

   
    plt.ion()
    img = plt.imread("map.png")
    # implot = plt.imshow(im)

    fig1, ax = plt.subplots(clear = True)
    ax.imshow(img, extent=[-180, 180, -90, 90])
    ax.set_aspect(1)

    x,y, colors= [],[],[]
    for m in range (len(line0)):
        colors.append('b')
    colors[index] = 'r'
    sc = ax.scatter(x,y)

    plt.plot(Posstation[0],Posstation[1],'r+')
    plt.xlabel('Longtitude')
    plt.ylabel('Latitude')
    plt.title('Satellite plot ' + line0[index])
    plt.draw()

    #ax.text(0.05, 0.95, line0[index], transform=ax.transAxes, fontsize=14,
    #    verticalalignment='top')



    while True:
        Latvector,Lonvector, time = Live(mode, line0, line1,line2,Rstation, Posstation, DeltaLat, DeltaLon, index )
        x = Lonvector
        y = Latvector

        try:
            sc.set_offsets(np.c_[x,y])
            sc.set_color(colors)
            fig1.canvas.draw_idle()
            plt.pause(1)

        except:
            print('stop plotting live')
            return()
       

    return
