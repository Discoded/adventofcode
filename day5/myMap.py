class myMap:
    myDestination = []
    mySource = []
    # theStringArray = ['\d\d', '\d\d', '\d\d']
    def __init__(self, theStringArray=[]):
        if len(theStringArray) == 3:
            # [[50, 51]]
            self.myDestination = [[theStringArray[0], theStringArray[0]+theStringArray[2]-1]]
            # [[98, 99]]
            self.mySource = [[theStringArray[1], theStringArray[1]+theStringArray[2]-1]]
        else: 
            self.myDestination = []
            self.mySource = []
        #print("myDestination: ", self.myDestination)
        #print("mySource: ", self.mySource)

    """
    def append(self, theStringArray):
        self.myDestination.append([theStringArray[0], theStringArray[0]+theStringArray[2]-1])
        self.mySource.append([theStringArray[1], theStringArray[1]+theStringArray[2]-1])
    """
    """Return a list of [soil, range]. example [10, 19] means soil [10, 11, 12, ..., 18]
    Output = List of pairs and their maps [79, 92]
    Keyword arguments:
    value_range_pair -- A list where [value, range], denoting [value, value+1, value+2, ..., value+range-1]
    """
    def find(self, value_range_pair: []):
        #print("value_range_Pair", value_range_pair)
        seedStart = value_range_pair[0] # 57
        seedEnd = value_range_pair[0] + value_range_pair[1] - 1
        seed_pair =  []
        remainder = []
        for elem in self.mySource:
            sourceStart = elem[0] # 53
            sourceEnd = elem[1] # 60
            if sourceEnd >= seedStart >= sourceStart:
                #print(seedStart, sourceEnd)
                if sourceEnd >= seedEnd:
                    seed_pair = [seedStart, seedEnd]
                    return [seed_pair]
                # Need to return  the remainer
                else:
                    seed_pair = [seedStart, sourceEnd]
                    remainder = [sourceEnd + 1, seedEnd - sourceEnd]
                    return [seed_pair] + self.find(remainder)
        
        return [[seedStart, seedEnd]]
        
            


    def __or__(self, theOtherObj):
        new_map = myMap()
        #print("theOtherObj: ", theOtherObj)
        #print("self: ", self)
        for x in theOtherObj.myDestination:
            new_map.myDestination.append(x)
        for x in theOtherObj.mySource:
            new_map.mySource.append(x)
        for x in self.myDestination:
            new_map.myDestination.append(x)
        for x in self.mySource:
            new_map.mySource.append(x)
        #print("new_map: ", new_map)
        return new_map
    
    def __str__(self):
        theString = "mySource: " + str(self.mySource)
        theString += '||'
        theString += "myDestination: " + str(self.myDestination)
        theString += '\n'
        return theString
    
    ## Example: 79 -> 81
    def get(self, theKey):
        
        for i, value in enumerate(self.mySource):

            if(theKey >= value[0] and theKey <= value[1]):
                difference = value[1] - theKey
                destination_end = self.myDestination[i][1]
                return destination_end - difference
        
        return theKey
    

