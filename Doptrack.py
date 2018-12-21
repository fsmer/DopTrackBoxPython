#install sgp4(propegation), pytz(utc time), requests(download), matplotlib, numpy 
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Frame, Notebook
import os
from DownloadTLE import DownloadTLE
#from Downloadfreq import Downloadfreq
from ReadTLE import ReadTLE
from readcustom import readcustom
from Run import Run



########################################################################################################################################
#Download and Read

DownloadTLE()

locvector, lonvector, latvector, hvector, line0, line1, line2, info = readcustom()

namevector = []
indexvector = []
priorityvector = []


   
########################################################################################################################################
#Download frequency
#Downloadfreq()


########################################################################################################################################
#Test GUI
#Recalculate function

#run 
#index = satellitebox.current()

####################################################################
def recalc():
    locationindex = locationbox.current()
    satelliteindex = satellitebox.current()
    satellitename = satellitebox.get()
    stationlon1 = float(lonvector[locationindex])
    stationlat1 = float(latvector[locationindex])
    hstation1 = float(hvector[locationindex])
    mode1 = mode.get()
    loopdays = int(days.get())
    loophours = int(hours.get())
    loopminutes = int(minutes.get())
    minback1 = int(minback.get())
    PosStation = [stationlon1, stationlat1, hstation1]

    Run(mode1, line0, line1, line2, PosStation, satelliteindex, indexvector, priorityvector, loopdays, loophours, loopminutes, minback1)
    #plot
    return

###############################################################Addlocation
def addloc():
    #Location name
    locname = loc.get()
    fileloc = open("fileloc.txt", "a")
    fileloc.write(str(locname))
    fileloc.write('\n')
    fileloc.close

    #Longitude
    lon = stationlon.get()
    filelon = open("filelon.txt", "a")
    filelon.write(str(lon))
    filelon.write('\n')
    filelon.close

    #Latitude
    lat = stationlat.get()
    filelat = open("filelat.txt", "a")
    filelat.write(str(lat))
    filelat.write('\n')
    filelat.close

    #Hstation
    h = hstation.get()
    fileh = open("fileh.txt", "a")
    fileh.write(str(h))
    fileh.write('\n')
    fileh.close

    locvector, lonvector, latvector, hvector, line0, line1, line2, info  = readcustom()
    locationbox['values'] = locvector

    return

###############################################################Add TLE
def addTLE():
    #line 0 
    addline01 =addline0.get()
    file0 = open("file0.txt", "a")
    file0.write(str(addline01))
    file0.write('\n')
    file0.close

    #line 1 
    addline11 =addline1.get()
    file1 = open("file1.txt", "a")
    file1.write(str(addline11))
    file1.write('\n')
    file1.close

    #line 2 
    addline21 =addline2.get()
    file2 = open("file2.txt", "a")
    file2.write(str(addline21))
    file2.write('\n')
    file2.close

    #downlink 
    adddownlink1 =adddownlink.get()
    filedownlink = open("downlink.txt", "a")
    filedownlink.write(str(adddownlink1))
    filedownlink.write('\n')
    filedownlink.close

    locvector, lonvector, latvector, hvector, line0, line1, line2, info = readcustom()
    satellitebox['values'] = line0

    return 



###################################################Delete added TLE
def deleteTLE():
    if os.path.exists("file0.txt"):
        os.remove("file0.txt")
    if os.path.exists("file1.txt"):
        os.remove("file1.txt")
    if os.path.exists("file2.txt"):
        os.remove("file2.txt")
    if os.path.exists("downlink.txt"):
        os.remove("downlink.txt")

    line0,line1,line2, info  = ReadTLE()
    satellitebox['values'] = line0

    return

####################################################ADD satellite
def addsatellite():
    addinfo = []
    satelliteindex = satellitebox.current()
    satellitename = satellitebox.get()
    priority1 = priority.get()
    namevector.append(satellitename)
    indexvector.append(satelliteindex)
    priorityvector.append(priority1)
    addinfo = (satellitename, str(priority1), '\t \t',  info[satelliteindex], '\n')
    addinfo = ''.join(addinfo)
    T.insert(END, addinfo)
    print(namevector, indexvector, priorityvector)
    return




#######################################################GUI########################################################################################################
root = tk.Tk()
nb = Notebook(root)
nb.pack(fill=BOTH, expand=1)
frame = Frame(nb)
frame1 = Frame(nb)
frame2 = Frame(nb)
frame3 = Frame(nb)


nb.add(frame, text="Options")
nb.add(frame1, text="Satellite")
nb.add(frame2, text="Location")
nb.add(frame3, text = "Help")



root.title("Doptrack pass predictor")

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Menu", menu=filemenu)
filemenu.add_command(label="Run", command=recalc)
filemenu.add_separator()
filemenu.add_command(label="quit", command=root.destroy)







#Radiobutton choose loop
mode = tk.IntVar()
tk.Label(frame, 
        text="Choose mode:",
        padx = 20).grid(row = 2, column = 0)
tk.Radiobutton(frame, 
              text="Loopallsats",
              padx = 20, 
              variable=mode, 
              value=0).grid(row = 2, column = 1, sticky = W)
tk.Radiobutton(frame, 
              text="Loopxsat",
              padx = 20, 
              variable=mode, 
              value=1).grid(row = 3, column = 1, sticky = W)
tk.Radiobutton(frame, 
              text="MakeYML",
              padx = 20, 
              variable=mode, 
              value=2).grid(row = 4, column = 1, sticky = W)
tk.Radiobutton(frame, 
              text="Live",
              padx = 20, 
              variable=mode, 
              value=3).grid(row = 5, column = 1, sticky = W)


#Choose days propagating
days = tk.IntVar()
tk.Label(frame, 
        text="""Days:""",
        padx = 20).grid(row = 6, column = 0, sticky = W)
days = tk.Entry(frame)
days.grid(row = 6, column = 1, sticky = W)
days.insert(tk.END,1) #set default value

hours = tk.IntVar()
tk.Label(frame, 
        text="""Hours:""",
        padx = 20).grid(row = 6, column = 2, sticky = W)
hours = tk.Entry(frame)
hours.grid(row = 6, column = 3, sticky = W)
hours.insert(tk.END,0) #set default value

minutes = tk.IntVar()
tk.Label(frame, 
        text="""Minutes:""",
        padx = 20).grid(row = 6, column = 4, sticky = W)
minutes = tk.Entry(frame)
minutes.grid(row = 6, column = 5, sticky = W)
minutes.insert(tk.END,0) #set default value

minback = tk.IntVar()
tk.Label(frame, 
        text="""Minutes back:""",
        padx = 20).grid(row = 6, column = 6, sticky = W)
minback = tk.Entry(frame)
minback.grid(row = 6, column = 7, sticky = W)
minback.insert(tk.END,0) #set default value



#################################################################################################### SATELITE

#Dropdown menu choosing a satellite
tk.Label(frame1, 
        text="""Choose satellite:""",
        padx = 20).grid(row = 1, column = 1, sticky = NW)
satellitebox = ttk.Combobox(frame1, values= line0)
satellitebox.grid(row = 1, column = 2, sticky = NW)
satellitebox.current(19) #set default value

#Setpriority 
priority = tk.IntVar()
tk.Label(frame1, 
        text="""Priority:""",
        padx = 20).grid(row = 1, column = 3, sticky = NW)
priority = tk.Entry(frame1)
priority.grid(row = 1, column = 4, sticky = NW)
priority.insert(tk.END, 1) #set default value

button = tk.Button(frame1, 
                   text="ADD Satellite", 
                   command=addsatellite)
button.grid(row = 1, column = 5, sticky = NW)

# create a Text widget
T = tk.Text(frame1, height = 15, width = 43)
T.config(font=("consolas", 12), undo=True, wrap='word')
T.grid(row=1, column=0, sticky='nsw')

# create scrollbar
scrollb = tk.Scrollbar(frame1, command =T.yview)
scrollb.grid(row = 1, column = 1, sticky = 'nsw')
T['yscrollcommand']= scrollb.set

#Addline0
addline0 = tk.IntVar()
tk.Label(frame1, 
        text="""Line0:""",
        padx = 20).grid(row = 2, column = 1, sticky = W)
addline0 = tk.Entry(frame1)
addline0.grid(row = 2, column = 2, sticky = W)
addline0.insert(tk.END,'NAME') #set default value

#Addline1
addline1 = tk.IntVar()
tk.Label(frame1, 
        text="""Line1:""",
        padx = 20).grid(row = 2, column = 3, sticky = W)
addline1 = tk.Entry(frame1)
addline1.grid(row = 2, column = 4, sticky = W)
addline1.insert(tk.END,'LINE1') #set default value

#Addline2
addline2 = tk.IntVar()
tk.Label(frame1, 
        text="""Line2:""",
        padx = 20).grid(row = 2, column = 5, sticky = W)
addline2 = tk.Entry(frame1)
addline2.grid(row = 2, column = 6, sticky = W)
addline2.insert(tk.END,'LINE2') #set default value

#Adddownlink
adddownlink = tk.IntVar()
tk.Label(frame1, 
        text="""Downlink(MHz):""",
        padx = 20).grid(row = 2, column = 7, sticky = W)
adddownlink = tk.Entry(frame1)
adddownlink.grid(row = 2, column = 8, sticky = W)
adddownlink.insert(tk.END,'DOWNLINK') #set default value



button = tk.Button(frame1, 
                   text="ADD TLE", 
                   command=addTLE)
button.grid(row = 3, column = 1, sticky = 'ew')

button = tk.Button(frame1, 
                   text="DELETE TLE", 
                   command=deleteTLE)
button.grid(row = 3, column = 2, sticky = 'ew')

tk.Label(frame1, 
        text="""WARNING: \n removes all \n custom TLE's """,
        padx = 20).grid(row = 3, column = 3, sticky = W)

########################################################################################Location
#Choose longitude propagating
stationlon = tk.IntVar()
tk.Label(frame2, 
        text="""Longitude station (degree):""",
        padx = 20).grid(row = 2, column = 0)
stationlon = tk.Entry(frame2)
stationlon.grid(row = 2, column = 1)
stationlon.insert(tk.END,4.3570677) #set default value

#Choose latitude propagating
stationlat = tk.IntVar()
tk.Label(frame2, 
        text="""Latitude station (degree):""",
        padx = 20).grid(row = 2, column = 2)
stationlat = tk.Entry(frame2)
stationlat.grid(row = 2, column = 3)
stationlat.insert(tk.END,52.0115769) #set default value

#Choose height propagating
hstation = tk.IntVar()
tk.Label(frame2, 
        text="""Heigth station (m):""",
        padx = 20).grid(row = 2, column = 4)
hstation = tk.Entry(frame2)
hstation.grid(row = 2, column = 5)
hstation.insert(tk.END,0) #set default value

#Choose name
loc = tk.IntVar()
tk.Label(frame2, 
        text="""Location:""",
        padx = 20).grid(row = 3, column = 0)
loc = tk.Entry(frame2)
loc.grid(row = 3, column = 1)
loc.insert(tk.END, 'NAME') #set default value

button = tk.Button(frame2, 
                   text="ADD Location", 
                   command=addloc)
button.grid(row = 3, column = 2)

#Dropdown menu choosing a satellite
tk.Label(frame2, 
        text="""Choose Location:""",
        padx = 20).grid(row = 1, column = 0)
locationbox = ttk.Combobox(frame2, values= locvector)
locationbox.grid(row = 1, column = 1)
locationbox.current(0) #set default value

########################################################################Help
# create a Text widget
Thelp = tk.Text(frame3)
Thelp.config(font=("consolas", 12), undo=True, wrap='word')
Thelp.grid(row=1, column=0, sticky="nsew")

# create scrollbar
scrollb1 = tk.Scrollbar(frame3, command =Thelp.yview)
scrollb1.grid(row = 1, column = 1, sticky = 'nsew')
Thelp['yscrollcommand']= scrollb1.set

filehelp = open("README.txt", "r")
readme = filehelp.read()
Thelp.insert(END, readme)
filehelp.close


root.mainloop()
