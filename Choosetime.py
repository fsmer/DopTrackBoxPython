def Choosetime(looptime,loopdays):
    from datetime import datetime
    from datetime import timedelta
    import pytz

    j = 0
    
    time = datetime.now(pytz.utc)
    #print(time)
    year = []
    month = []
    day = []
    hour = []
    minute = []
    second = []



    #Loop
    if looptime == 1:
        addedminutes = loopdays*24*60
    else:
        addedminutes= 1
    for j in range (0,addedminutes):
          year.append(time.year)
          month.append(time.month)
          day.append(time.day)
          hour.append(time.hour)
          minute.append(time.minute)
          second.append(time.second)

          time = time + timedelta(minutes=1) 
          j +=1

    #print(minute)

    return(year, month, day, hour, minute, second) 
