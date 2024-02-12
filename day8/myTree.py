# In Progress

class myTree:
    myParent:str
    myLeft: self.myTree
    myRight: self.myTree

    def __init__(self, theStringArray=[], theLeft="", theRight=""):
        if len(theStringArray) == 3:
            self.myParent = theStringArray[0]
            self.myLeft = self.myTree(theStringArray[1])
            self.myRight = self.myRight(theStringArray[1])