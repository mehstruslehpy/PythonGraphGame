class Player:
    # shared variables between classes can be declared at this level
    def __init__(self, G, color, chars):
        # instance variables need to be declared in the constructor
        # player locations stores node id's for each player
        # player color stores the current players color
        self.playerlocations = []
        self.color = color
        for x in range(0,chars):
            v = G.GetRandomVertexId()
            while (G.GetColor(v)!="green"):
                v = G.GetRandomVertexId()
            G.SetColor(v,color)
            self.playerlocations.append(v)

    #update the list of locations for this player
    def UpdateLocationsList(self,G):
        self.playerlocations.clear()
        #for i in range(0,G.GetVertexCount()-1):
        for i in range(0,G.GetVertexCount()):
            if (G.GetColor(i)==self.color):
                self.playerlocations.append(i)

    def GetColor(self):
        return self.color

    def GetLocationsList(self):
        return self.playerlocations

    # attempt to move a character at f to t returns boolean if move is successful
    def MoveChar(self,G,f,t):
        if (f >= G.GetVertexCount() or t >= G.GetVertexCount()):
            print("ERROR: Selection is out of vertex id range")
            return False
        if (G.GetColor(f)!=self.color):
            print("ERROR: You must select your own characters to move")
            return False
        if (G.GetColor(t)=="green"):
            oldpoints = G.GetPoints(f)
            newpoints = G.GetPoints(t)
            G.SetPoints(f,0)
            G.SetPoints(t,oldpoints+newpoints)
            G.SetColor(f,"green")
            G.SetColor(t,self.color)
            return True
        if (G.GetColor(t)!=self.color and G.GetColor(t) != "green"):
            #landed on opposing player char spot
            oldpoints = G.GetPoints(f)
            newpoints = G.GetPoints(t)
            if (oldpoints > newpoints):
                #you have more points, you win
                G.SetPoints(f,0)
                G.SetPoints(t,oldpoints-newpoints)
                G.SetColor(f,"green")
                G.SetColor(t,self.color)
            elif (oldpoints < newpoints):
                #you have less points, you lose
                G.SetPoints(f,0)
                G.SetPoints(t,newpoints-oldpoints)
                G.SetColor(f,"green")
            else:
                #you have the same amount of points, you both lose
                G.SetPoints(f,0)
                G.SetPoints(t,0)
                G.SetColor(f,"green")
                G.SetColor(t,"green")
            return True

        def UpdateLocationsList(self,G):
            self.playerlocations.clear()
            for i in range(0,G.GetVertexCount()-1):
                if (G.GetColor(i)==self.color):
                    playerlocations.append(i)
