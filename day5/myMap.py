class myMap:
    myMap: []
    # theStringArray = ['\d\d', '\d\d', '\d\d']
    def __init__(self, theStringArray=[]):
        
        if len(theStringArray) == 3:
           self.myMap = [[int(x) for x in theStringArray]]
        else: 
            self.myMap = []


    def get(self, key:int):

        for elem in self.myMap:
            if elem[1] + elem[2] - 1 >= key >=  elem[1]:
                return key - elem[1] + elem[0]
            
        return key

    """Return a list of [soil, range]. example [10, 19] means soil [10, 11, 12, ..., 18]
    Output = List of pairs and their maps [79, 92]
    Keyword arguments:
    value_range_pair -- A list where [value, range], denoting [value, value+1, value+2, ..., value+range-1]
    """
    def find(self, value_range_pair: []):

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
        for x in theOtherObj.myMap:
            new_map.myMap.append(x)
        for x in self.myMap:
            new_map.myMap.append(x)
        return new_map
    
    def __str__(self):

        theString = str(self.myMap)

        return theString

    

