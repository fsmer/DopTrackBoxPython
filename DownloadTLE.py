def DownloadTLE(): 
    import requests

    ############################################################################################################
    #Download TLE
    try:

        url='http://celestrak.com/NORAD/elements/active.txt'

        r = requests.get(url, allow_redirects=True)
    #    print(r.content)

        TLEold = str(r.content)

        #write file
        file = open("TLE.txt", 'w')
        file.write(TLEold)
        file.close()

        #download frequency

        url1='http://www.ne.jp/asahi/hamradio/je9pel/satslist.csv'

        f = requests.get(url1, allow_redirects=True, timeout=1)
     #   print(f.content)

        freqold = str(f.content)
   
        #print(satnamefreq[j],ID[j], uplink[j], downlink[j], active[j])
        #write file
        file = open("Freq.txt", 'w')
        file.write(freqold)
        file.close()

        print('internet')
        return
    except:
        print('no internet')
        return









    
