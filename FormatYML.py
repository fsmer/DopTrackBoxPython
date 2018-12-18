
#how to do the time?
x = 5
y = 'funcube'
file = open('testfile.yml', 'w')
file.write('Sat:')

file.write("\n \t \t")
file.write('Predict: %d' %x)

file.write("\n \t \t")
file.write('EAzimuth: %d' %x)

file.write("\n \t \t")
file.write('Elevation: %d' %x)

file.write("\n \t \t")
file.write('Length of pass: %d' %x)

file.write("\n \t \t")
file.write('SAzimuth: %d' %x)

file.write("\n \t \t")
file.write('time used UTC: %d' %x)

file.write("\n \t \t")
file.write('timezone used: %d' %x)

file.write("\n \t \t")
file.write('used TLE line1: %d' %x)

file.write("\n \t \t")
file.write('used TLE line2: %d' %x)

file.write("\n \t")
file.write('Record:')


file.write("\n \t \t")
file.write('Start of recording: %d' %x)

file.write("\n \t \t")
file.write('num_sample: %d' %x)

file.write("\n \t \t")
file.write('sample_rate: %d' %x)

file.write("\n \t \t")
file.write('time1 UTC: %d' %x)

file.write("\n \t \t")
file.write('time2 UTC: %d' %x)

file.write("\n \t \t")
file.write('time3 LT: %d' %x)


file.write("\n \t")
file.write('State:')

file.write("\n \t \t")
file.write('Antenna: %d' %x)

file.write("\n \t \t")
file.write('NORADID: %d' %x)

file.write("\n \t \t")
file.write('Name: %d' %x)

file.write("\n \t \t")
file.write('Priority: %d' %x)

file.write("\n \t \t")
file.write('Tuning Frequency: %d' %x)


file.write("\n \t")
file.write('Station:')

file.write("\n \t \t")
file.write('Height: %d' %x)

file.write("\n \t \t")
file.write('Lat: %d' %x)

file.write("\n \t \t")
file.write('Lon: %d' %x)

file.write("\n \t \t")
file.write('Name: %s' %y)

file.close()


