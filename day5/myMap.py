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

    """Return a list of [value, range]. example [10, 19] means soil [10, 11, 12, ..., 18]
    Output = List of pairs and their maps [[value0, range1], [value2, range2], [value3, range3], ...]
    Keyword arguments:
    value_range_pair -- An integer list where [value, range], denoting [value, value+1, value+2, ..., value+range-1]
    """
    def find(self, value_range_pair: []):
        # [81, 14]
        #print("value_range_pair: ", value_range_pair)
        #print(self.myMap)
        #print("find() value_range_pair: ", value_range_pair)
        keyStart = value_range_pair[0] # 81
        keyRange = value_range_pair[1] # 14
        keyEnd =  keyStart + keyRange - 1 #93
        for elem in self.myMap:
            sourceStart = elem[1] # 25
            sourceRange = elem[2] # 70
            sourceEnd = sourceStart + sourceRange - 1
            
            # if keyStart is between sourceEnd and sourceStart
            if (sourceEnd >= keyStart >= sourceStart): 
                # If sourceEnd is greaterthan or equal to keyEnd,
                # The entire range will fit
                if(sourceEnd >= keyEnd):
                    seed_pair = [keyStart, keyRange]
                    return [seed_pair]
                
                # Else if the entire range doesn't fit
                # Return the ones that fit and calculate the ones that don't(remainder)
                # 
                else:
                    remainderRange = keyEnd - sourceEnd
                    remainder = [sourceEnd + 1, remainderRange]
                
                    return [[keyStart, sourceEnd - keyStart + 1]] + self.find(remainder)
        
        
        # Map does not map these values so simply return them.
        seed_pair = [keyStart, keyRange]
        return [seed_pair]
        
            
    """Return a new Map of values merging two maps.

    theOtherObj: Map to be merged
    self: Map to be merged
    """
    def __or__(self, theOtherObj):
        new_map = myMap()
        for x in theOtherObj.myMap:
            new_map.myMap.append(x)
        for x in self.myMap:
            new_map.myMap.append(x)
        return new_map
    
    """Return a string of the Map in list form

    """
    def __str__(self):

        theString = str(self.myMap)

        return theString

    

