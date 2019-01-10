def SGP4(line1, line2, year, month, day, hour, minute, second):
    from sgp4.earth_gravity import wgs72
    from sgp4.io import twoline2rv


    satellite = twoline2rv(line1, line2, wgs72)
    position, velocity = satellite.propagate(year, month, day, hour, minute, second)

 #  print(satellite.error)    # nonzero on error
 #   print(satellite.error_message)
 #   print(position)
 #   print(velocity)
    return(position,velocity)
