#install sgp4(propegation), pytz(utc time), requests(download)
import tkinter as tk
from tkinter import ttk
from tkinter import *
from DownloadTLE import DownloadTLE
#from Downloadfreq import Downloadfreq
from ReadTLE import ReadTLE
from Recalculate import Recalculate


########################################################################################################################################
#Download TLE

DownloadTLE()
line0,line1,line2, info  = ReadTLE()
   
########################################################################################################################################
#Download frequency
#Downloadfreq()


########################################################################################################################################
#Test GUI
#Recalculate function

def recalc():
    stationlon1 = float(stationlon.get())
    stationlat1 = float(stationlat.get())
    hstation1 = float(hstation.get())
    looptime1 = looptime.get()
    loopdays = int(days.get())
    satelliteindex = satellitebox.current()
    satellitename = satellitebox.get()
    Recalculate(looptime1, loopdays, satelliteindex, line0, line1,line2, stationlon1, stationlat1, hstation1)

    #plot
    return

#Callback function after drop down menu
def callbackFunc(event):
     satelliteindex = satellitebox.current()
     satellitename = satellitebox.get()
     print("New Element Selected", satelliteindex, satellitename)
     return


#GUI
root = tk.Tk()
frame = tk.Frame(root)
frame.grid()
root.title("Doptrack pass predictor")

#Button
button = tk.Button(frame, 
                   text="Quit", 
                   fg="red",
                   command=root.destroy)
button.grid(row = 0, column = 3)
slogan = tk.Button(frame,
                   text="Recalculate",
                   command=recalc)
slogan.grid(row = 0, column = 4)

#Dropdown menu choosing a satellite
tk.Label(root, 
        text="""Choose satellite:""",
        padx = 20).grid(row = 1, column = 0)
satellitebox = ttk.Combobox(frame, values= line0)
satellitebox.grid(row = 1, column = 0)
satellitebox.current(19) #set default value

satellitebox.bind("<<ComboboxSelected>>", callbackFunc)

#Radiobutton choose loop
looptime = tk.IntVar()
tk.Label(root, 
        text="Choose loop:",
        padx = 20).grid(row = 2, column = 0)
tk.Radiobutton(root, 
              text="Loop time",
              padx = 20, 
              variable=looptime, 
              value=1).grid(row = 2, column = 1)
tk.Radiobutton(root, 
              text="Loop satellites",
              padx = 20, 
              variable=looptime, 
              value=0).grid(row = 2, column = 2)


#Choose days propagating
minutes = tk.IntVar()
tk.Label(root, 
        text="""Days time loop:""",
        padx = 20).grid(row = 3, column = 0)
days = tk.Entry(root)
days.grid(row = 3, column = 1)
days.insert(tk.END,1) #set default value



#Choose longitude propagating
stationlon = tk.IntVar()
tk.Label(root, 
        text="""Longitude station (degree):""",
        padx = 20).grid(row = 8, column = 0)
stationlon = tk.Entry(root)
stationlon.grid(row = 8, column = 1)
stationlon.insert(tk.END,4.3570677) #set default value

#Choose latitude propagating
stationlat = tk.IntVar()
tk.Label(root, 
        text="""Latitude station (degree):""",
        padx = 20).grid(row = 9, column = 0)
stationlat = tk.Entry(root)
stationlat.grid(row = 9, column = 1)
stationlat.insert(tk.END,52.0115769) #set default value

#Choose height propagating
hstation = tk.IntVar()
tk.Label(root, 
        text="""Heigth station (m):""",
        padx = 20).grid(row = 10, column = 0)
hstation = tk.Entry(root)
hstation.grid(row = 10, column = 1)
hstation.insert(tk.END,0) #set default value

#Text
#S = tk.Scrollbar(root)
#T = tk.Text(root, height=10, width=50)
#S.pack(side=tk.RIGHT, fill=tk.Y)
#T.pack(side=tk.LEFT, fill=tk.Y)
#S.config(command=T.yview)
#T.config(yscrollcommand=S.set)
#quote = '\n'.join(line0)
#T.insert(tk.END, quote)

root.mainloop()
