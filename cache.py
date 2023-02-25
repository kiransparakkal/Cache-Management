cache = [] #List of cache elements
requests = [] # List of requests given by user
reqCount = [] # No of requests against each user input

#function for First In First Out [FIFO] algorithm
def fifo():
    
    while "true":
        value = int(input("Enter value"))
        if(value != 0):
            requests.append(value) # Storing each user input inside requests list
            reqvalue = requests[-1] # Taking the latest value inputted by user
            
            # Adding new value in cache from main memory,when cache is not full
            if ((reqvalue not in cache) and (len(cache)!=8)):
                    print("Miss")
                    cache.append(reqvalue)
            #Retrieving data from cache when the element is present        
            elif(reqvalue in cache):
                    print("Hit")
            # Adding new value in cache from main memory,when cache is full using FIFO        
            elif ((reqvalue not in cache) and (len(cache)==8)):
                    print ("Miss")
                    cache.remove(cache[0])
                    cache.append(reqvalue)
        else:
            break
    print("Final Cache is",cache)
    cache.clear()
    mainmenu()
    
#function for Least Frequently Used [LFU] algorithm
def lfu():
    while "true":
        
        value = int(input("Enter value"))
        if(value != 0):
            requests.append(value)
            reqvalue = requests[-1]
            
            

            if ((reqvalue not in cache) and len(cache)!=8):
                print("Miss")
                cache.append(reqvalue)
                reqCount.append(1)
                
            elif(reqvalue in cache):
                print("Hit")
                cacheIndex = cache.index(reqvalue)
                reqCount[cacheIndex] = reqCount[cacheIndex] +1
            
            elif ((reqvalue not in cache) and (len(cache)==8)):
                    print ("Miss")
                    
                    minrequest = []
                    minvalue_req = min(reqCount)
                    for x in range (0,len(reqCount)):
                        if(reqCount[x] == minvalue_req):
                            #minrequest.append(reqCount.index(reqCount[x]))
                              minrequest.append(x)

                    if (len(minrequest) == 1):
                        cache.pop(minrequest[0])
                        reqCount.pop(minrequest[0])
                    elif(len(minrequest)>1):
                        smallestElement_List = []
                        #for item in minrequest:
                        for i in range (0,len(minrequest)):
                            smallestElement_List.append(cache[minrequest[i]])
                        smallestElement_List.sort()
                        
        
                        reqCount.pop(cache.index(smallestElement_List[0]))
                        cache.remove(smallestElement_List[0])
                        

                    
                    cache.append(reqvalue)
                    reqCount.append(1)
                    
                    
        else:
                break
    print("Final Cache is",cache)
    #print("request count",reqCount)
    #print(reqCount)
    cache.clear()
    reqCount.clear()
    #minrequest.clear()
    

    mainmenu()

            
def mainmenu():
 print("press 1 for fifo, or press 2 for lfu, or press Q to quit the program.")
 userinput = (input())
 if (userinput == '1'): 
  fifo()
 elif(userinput == '2'):
    lfu()
 elif(userinput == 'Q'):
    exit()
    

mainmenu()







