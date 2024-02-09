class myHand:
    myHand: str
    myBid: int

    
    def __init__(self, theHand: str, theBid:int):

        self.myHand = theHand
        self.myBid = theBid
    
    def __str__(self):

        theString = self.myHand + ', ' + str(self.myBid)  

        return theString

    

