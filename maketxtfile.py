def maketxtfile(inview, time, sat):
    #also add the elevation?
    import os
    if os.path.isfile("inview.txt"):
        os.remove("inview.txt")

    file = open("inview.txt", 'w')
    length = len(inview)
    # print(len(sat))
    j = 0
    for i in range(0, length):
        if inview[i] == True:
            j = 0
            if(len(sat)==length):
                file.write(sat[i])
            else:
                file.write(sat[0]) #KLOPT NIET
            file.write("\t")

            file.write('%s' %(time[i],))
            file.write("\n")
        else:
            while j < 1:
                file.write("\n")
                j = j+1
    
            


    file.close()
    
    return