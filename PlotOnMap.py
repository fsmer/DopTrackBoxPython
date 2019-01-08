
def PlotOnMap(Latvector,Lonvector, time, insight, station, minback, mode, satelliteindex, satellites):

    import matplotlib.pyplot as plt
    import numpy as np
    import datetime 


    if (mode == 0):
        # mode 0 is all sats
        # we need to plot all satellites locations and give their names
        # maybe the satellite selected can be an other marker

        img = plt.imread("map.png")
        # implot = plt.imshow(im)

        fig1, ax = plt.subplots()
        ax.imshow(img, extent=[-180, 180, -90, 90])
        ax.set_aspect(1)


   
        plt.plot(Lonvector, Latvector, 'b.', label='Satellites') 
        plt.plot(station[0],station[1],'r+', label='Groundstation')
     
        plt.plot(Lonvector[satelliteindex], Latvector[satelliteindex],'rx', label=satellites[satelliteindex])

        ax.legend(bbox_to_anchor=(0., 1.02, 1., .102),  ncol = 1)

        plt.xlabel('Lontitude')
        plt.ylabel('Latitude')
        plt.text(90, 100, 'Satellites in database',
            horizontalalignment='center')

        # x = Lonvector
        # plt.xticks(x, satellites)
        # plt.xticks(rotation=90)
        # y = Latvector
        # plt.yticks(y, satellites)
        
        # plt.subplots_adjust(left=0.12, right=0.13, top=0.26, bottom=0.25)

        for i, txt in enumerate(satellites):
            ax.annotate(txt, (Lonvector[i], Latvector[i]), size = 7)
        
        #this makes the plot screen size
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())

        plt.show(block=False)


    elif (mode == 1):
        print("Visual for loop x sats is not yet ready")

    elif (mode == 3):
        print("Visual for life updating is not yet ready")

    # img = plt.imread("map.png")
    # # implot = plt.imshow(im)

    # fig1, ax = plt.subplots()
    # ax.imshow(img, extent=[-180, 180, -90, 90])
    # ax.set_aspect(1)



    # # print(Lonvector[0][0][0])

    # plt.plot(Lonvector[0][0], Latvector[0][0], 'b.') 
    # plt.plot(station[0],station[1],'r+')
    # plt.plot(Lonvector[0][0][minback], Latvector[0][0][minback],'rx')

    # plt.xlabel('Lontitude')
    # plt.ylabel('Latitude')
    # plt.title('Satellite or groundtrack plot')



    # fig2, ax2 = plt.subplots()
    # x = np.linspace(1,len(insight))
    # plt.plot(insight, '.')
    # # ax2.set_aspect(2)

    # plt.xticks(x, time)
    # plt.xticks(rotation=90)

    
    # plt.show(block=False)
    # print('hello')
    return