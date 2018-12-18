


#Update database
DownloadTLE()
line0,line1,line2, info  = ReadTLE()


#Run UI
#Input line0 line1 line2, info

#output
#mode, Ground station, tijd, add new satellite,  prioritylist, elevation

#when run is pressed get values from UI and run execution path
Run(line0, line1, line2, mode, info, index, indexvector, priority)