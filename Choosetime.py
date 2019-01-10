def Choosetime(loopdays, loophours, loopminutes, negativeminutes):
    from datetime import datetime
    from datetime import timedelta
    import pytz

    j = 0
    
    time = datetime.now(pytz.utc) + timedelta(minutes = -negativeminutes)
    localtime0 = datetime.now() + timedelta(minutes = -negativeminutes)
    #print(time)
    time1 = []
    localtime = []
    year = []
    month = []
    day = []
    hour = []
    minute = []
    second = []



    #Loop
    addedminutes = loopdays*24*60+loophours*60+loopminutes
    for j in range (-negativeminutes, addedminutes):
          time1.append(time)
          year.append(time.year)
          month.append(time.month)
          day.append(time.day)
          hour.append(time.hour)
          minute.append(time.minute)
          second.append(time.second)
          localtime.append(localtime0)

          time = time + timedelta(minutes=1)
          localtime0 = localtime0 + timedelta(minutes=1)
          j +=1

    #print(minute)
    #

    return(time1, year, month, day, hour, minute, second, localtime) 
