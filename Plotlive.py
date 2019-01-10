def Plotlive(mode, line0, line1,line2,Rstation, Posstation):
    import matplotlib.pyplot as plt
    import numpy as np
    import datetime
    from Live import Live
    

   
    plt.ion()
    img = plt.imread("map.png")
    # implot = plt.imshow(im)

    fig1, ax = plt.subplots(clear = True)
    ax.imshow(img, extent=[-180, 180, -90, 90])
    ax.set_aspect(1)

    x,y = [],[]
    sc = ax.scatter(x,y)

    plt.plot(Posstation[0],Posstation[1],'r+')
    plt.xlabel('Longtitude')
    plt.ylabel('Latitude')
    plt.title('Satellite or groundtrack plot')

    plt.draw()

    while True:
        Latvector,Lonvector, time = Live(mode, line0, line1,line2,Rstation, Posstation)
        x = Lonvector
        y = Latvector
        try:
            sc.set_offsets(np.c_[x,y])
            fig1.canvas.draw_idle()
            plt.pause(1)
        except:
            print('stop plotting live')
            return()
       

    return
