def testPlotMap():
    # https://plot.ly/python/images/ 

    # use dash to get updating stuff?
    # https://stackoverflow.com/questions/51367567/interactive-plot-with-slider-using-plotly check this out

    #most solutions seem difficutl maybe look at matplot for live updating tutorials on youtube
    import plotly as py 
    import plotly.graph_objs as go 

    import numpy as np

    py.offline.init_notebook_mode(connected=True) 
    x=[-180,180]
    y=[-90,90]

    x2 = [180,540]
    x3 = [-540,-180]


    trace1= go.Scatter(
        x=x, 
        y=y,
        name = "trace 1",
        line = dict(
            color = ("green"),
            width = 4,
            dash = 'dot' #dashdot, dash
            )
        )
    trace2= go.Scatter(x=x2, y=y)
    trace3= go.Scatter(x=x3, y=y)
    layout= go.Layout(images= [dict(
                      source= "map.png",
                      xref= "x",
                      yref= "y",
                      x= -180,
                      y= 90,
                      sizex= 360,
                      sizey= 180,
                      sizing= "stretch",
                      opacity= 1,
                      layer= "below"),
                      dict(
                      source= "map.png",
                      xref= "x",
                      yref= "y",
                      x= 180,
                      y= 90,
                      sizex= 360,
                      sizey= 180,
                      sizing= "stretch",
                      opacity= 1,
                      layer= "below"),
                      dict(
                      source= "map.png",
                      xref= "x",
                      yref= "y",
                      x= -540,
                      y= 90,
                      sizex= 360,
                      sizey= 180,
                      sizing= "stretch",
                      opacity= 1,
                      layer= "below")
                      ],
                      xaxis = dict(
                          range = [-180,180]
                      ),
                      yaxis = dict(
                          range = [-90,90]
                      )
                      )
                  
    fig=go.Figure(data=[trace1, trace2, trace3],layout=layout)
    py.offline.plot(fig,filename='map.png')
    print('end test plot')
    return