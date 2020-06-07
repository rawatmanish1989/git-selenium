import time

def customDateTime():
    localTime = time.localtime()
    currentTime = ""
    for i in range(6):
        currentTime = currentTime + str(localTime[i])
    return currentTime

    
    
    