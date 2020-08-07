# graph contains the graph class, player contains the player class, game
# specifics implements functions specific to a given game
from gamegraphwrapper import GameGraphWrapper
from player import Player
from gamespecifics import *
import subprocess
from iofunctions import renderGraph


def main():
    print("")
    print("Welcome to graph game!")
    print("The game map can be monitored by opening graph.png in the browser and refreshing as well as by viewing the plot popups.")
    print("Plot popups must be closed before the next turn can proceed.")
    print("")
    # initialize the graph and player classes
    G = GameGraphWrapper()
    P1 = Player(G,"red",5)  # construct player 1 using graph G
    P2 = Player(G,"blue",5)

    # enter game loop, python does not have do while loops
    # this will do instead
    print("")
    print("Beginning game")
    print("Up next is: "+P1.GetColor())
    renderGraph(G)
    playerTurn(G, P1, P2)
    print("Up next is: "+P2.GetColor())
    renderGraph(G)
    playerTurn(G, P2, P1)
    while(checkWin(G)):
        print("Up next is: "+P1.GetColor())
        renderGraph(G)
        playerTurn(G, P1, P2)
        print("Up next is: "+P2.GetColor())
        renderGraph(G)
        playerTurn(G, P2, P1)

    # the game has ended
    print("Game has ended.")
    #printGameStats(G, P1, P2)
    #printWinLoseScreen(G, P1, P2)
    renderGraph(G)

# call main
main()
