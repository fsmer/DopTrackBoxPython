
def PlotOnMap(Latvector,Lonvector, time, insight, station, minback, mode, satelliteindex, satellites, indexer):

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
        #print groundtrack of satellites in index or indexvector
        #go 120 minutes back and 120 minutes forward
        #give the past a differnt color and maybe an arrow
        #plot from indexer
        forward = minback #groundtrack propegation forward
        img = plt.imread("map.png")
        fig1, ax = plt.subplots()
        ax.imshow(img, extent=[-180, 180, -90, 90])
        ax.set_aspect(1)
        plt.xlabel('Lontitude')
        plt.ylabel('Latitude')
        plt.text(90, 100, 'Satellites in database', horizontalalignment='center')
        plt.plot(station[0],station[1],'r+', label='Groundstation')

        # we can change the color of each ground track through going through a list.
        colorlist = ['#7e1e9c', '#15b01a', '#0343df', '#ff81c0', '#95d0fc', '#f97306', '#029386', '#c20078',' #ffff14', '#033500', '#650021' , '#e6daa6']
        indexlen = len(indexer)
        lenlon = len(Lonvector[0])
        for i in range(0,indexlen):
            plt.plot(Lonvector[i][minback], Latvector[i][minback], 'bx',zorder=10)
            if i >= len(colorlist)/2:
                print('To many inputs for color scale')
                
            for j in range(0, minback+forward):
                if j < minback:
                    
                    plt.plot(Lonvector[i][j], Latvector[i][j], marker = '.', color = colorlist[2*i],zorder=2)
                else:
               
                    plt.plot(Lonvector[i][j], Latvector[i][j],marker = '.', color = colorlist[2*i+1],zorder=1)
            #the arrows are pointed over the map from point to the next point, this means that they can be very buggy
            plt.arrow(Lonvector[i][minback], Latvector[i][minback], (Lonvector[i][minback+1]-Lonvector[i][minback])/1000, (Latvector[i][minback+1]-Latvector[i][minback])/1000,shape='full', lw=4, length_includes_head=True, head_width=3, color = 'r',zorder=5 )    
            ax.annotate(satellites[indexer[i]], (Lonvector[i][minback], Latvector[i][minback]), size = 7)
       
       
        plt.show(block=False)
       
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