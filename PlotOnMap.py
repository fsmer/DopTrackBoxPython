
def PlotOnMap(Latvector,Lonvector, time, insight, station, minback, mode):

    import matplotlib.pyplot as plt
    import numpy as np
    import datetime


    
    img = plt.imread("map.png")
    # implot = plt.imshow(im)

    fig1, ax = plt.subplots()
    ax.imshow(img, extent=[-180, 180, -90, 90])
    ax.set_aspect(1)



    # print(Lonvector[0][0][0])

    plt.plot(Lonvector[0][0], Latvector[0][0], 'b.') 
    plt.plot(station[0],station[1],'r+')
    plt.plot(Lonvector[0][0][minback], Latvector[0][0][minback],'rx')

    plt.xlabel('Lontitude')
    plt.ylabel('Latitude')
    plt.title('Satellite or groundtrack plot')



    fig2, ax2 = plt.subplots()
    x = np.linspace(1,len(insight))
    plt.plot(insight, '.')
    # ax2.set_aspect(2)

    plt.xticks(x, time)
    plt.xticks(rotation=90)

    
    plt.show(block=False)
    # print('hello')
    return