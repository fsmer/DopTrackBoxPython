def makeyamlfile(inviewvector, timevector):
    import os


    #Split passings, needed inviewvector and time
    beginpassing = []
    endpassing = []
    #begin or end is in passing

    if inviewvector[0] is True:
        beginpassing.append(0)


    
    for j in range(1, len(inviewvector)):
        if inviewvector[j]  is True and inviewvector[j-1] is False:
           beginpassing.append(j)
           j=j+1
        elif inviewvector[j]  is False and inviewvector[j-1] is True:
            endpassing.append(j)

    if inviewvector[len(inviewvector)-1] is True:
        endpassing.append(len(inviewvector)-1)

        
    for j in range(0, len(beginpassing)):
        timepassing = []
        for n in range(beginpassing[j], endpassing[j]):
            timepassing.append(timevector[n])
        filename = 'doptrackinfo' + str(j) + '.yml'
            
        file = open(filename, 'w')
        file.write(str(timepassing))
        file.close()


    print(beginpassing, endpassing)
    return