def playerTurn(G,P1,P2):
    P1.UpdateLocationsList(G)
    P2.UpdateLocationsList(G)
    print("Player turn: "+P1.GetColor())
    print("Enter 0 to move or 1 to skip your turn:")
    print("DEBUG: USER INPUT HERE!")
    choose = input(">")
    if (choose == "0"):
        # Pick a from node
        print("Select a source node to move: ")
        for i in range(0,len(P1.GetLocationsList())):
            print("-- node: "+str(P1.GetLocationsList()[i]))
        fromnode = input(">")
        while (not( int(fromnode) in P1.GetLocationsList())):
            print("ERROR: You can only select "+P1.GetColor()+" nodes")
            fromnode = input(">")

        # Pick a to node
        print("Select a destination node:")
        for i in range(0,len(G.GetNeighbors(int(fromnode)))):
            print("-- node: "+str(G.GetNeighbors(int(fromnode))[i]))
        tonode = input(">")
        while (not( int(tonode) in G.GetNeighbors(int(fromnode)))):
            print("ERROR: You can only select neighboring nodes.")
            print(G.GetNeighbors(int(fromnode)))
            tonode = input(">")
        print("Moving "+fromnode+" to "+tonode)

        # perform the move
        P1.MoveChar(G,int(fromnode),int(tonode))



def checkWin(G):
    print("Checking for a winner...")
    hasblue = False
    hasred = False
    # check if the board contains blue and red
    for i in range(0,G.GetVertexCount()-1):
        #if (G.GetColor(i)!="red" and G.GetColor(i)!="green"):
        if (G.GetColor(i)=="blue"):
            hasblue = True
        #if (G.GetColor(i)!="blue" and G.GetColor(i)!="green"):
        if (G.GetColor(i)=="red"):
            hasred = True

    if (hasred and not hasblue):
        print("Red wins!")
        return False
    elif (hasblue and not hasred):
        print("Blue wins!")
        return False
    elif (not(hasblue) and not(hasred)):
        print("Draw!")
        return False
    else:
        return True


def printGameStats(G,P1,P2):
    print("print game stats")
def printWinLoseScreen(G,P1,P2):
    print("win lose screen")
