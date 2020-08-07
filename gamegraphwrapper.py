import random
import subprocess
from igraph import *


class GameGraphWrapper:
    # the internal graph
    G = Graph()
    # will be setup in constructor
    ReusableLayout = []
    #constructor
    def __init__(self):
        print("Generating random graph.")
        print("###########################################################################")
        print("Current graph:")

        # we can do green for no player red for player 1 blue for player 2
        # and use the label for points display and node id
        self.G.add_vertices(1)
        points = random.randint(1,50)
        self.G.vs[0]["label"] = "0:"+str(points)
        self.G.vs[0]["points"] = points
        self.G.vs[0]["color"] = "green"
        self.G.vs[0]["shape"] = "rectangle"
        self.G.vs[0]["size"] = 40

        # build a randomized connected graph
        for x in range(0,random.randint(11,25)):
            self.G.add_vertices(1)
            # assign a random point value, note that this will need to be changed since
            # we have more to display than just points
            points = random.randint(1,50)
            self.G.vs[self.G.vcount()-1]["label"] = str(self.G.vcount()-1)+":"+str(points)
            self.G.vs[self.G.vcount()-1]["points"] = points
            self.G.vs[self.G.vcount()-1]["color"] = "green"
            self.G.vs[self.G.vcount()-1]["shape"] = "rectangle"
            self.G.vs[self.G.vcount()-1]["size"] = 40
            to_vertex = self.G.vcount()-1
            while to_vertex==self.G.vcount()-1:
                to_vertex = random.randint(0,self.G.vcount()-1)
            self.G.add_edge(self.G.vcount()-1,to_vertex)

        # add a couple other random edges for loops
        for x in range(0,random.randint(1,10)):
            from_vertex = random.randint(0,self.G.vcount()-1)
            to_vertex = from_vertex
            while to_vertex==from_vertex:
                to_vertex = random.randint(0,self.G.vcount()-1)
            self.G.add_edge(from_vertex,to_vertex)
        self.ReusableLayout = Graph.layout_lgl(self.G)
        print(self.G)
        print("###########################################################################")

    # this is the default method of displaying the graph
    # this will plot the graph in the default image viewer as well as
    # output a dot file and generate a png from  it
    def DefaultGraphDisplay(self):
        self.DotFileOutput()
        subprocess.call("./convertdotfiletopng.sh")
        # the game will hang until the external image viewer is closed
        # be sure to always place this last
        #plot(self.G, layout = self.ReusableLayout)

    # output a dotfile version of the current graph
    def DotFileOutput(self):
        Graph.write_dot(self.G,"graph.dot")

    # return a count of the vertices in the graph
    def GetVertexCount(self):
        return self.G.vcount()

    # return a random vertex id in the graph
    def GetRandomVertexId(self):
        return random.randint(0,self.G.vcount()-1)

    # return points at vertex v
    def GetPoints(self,v):
        return self.G.vs[v]["points"]

    # return color at vertex v
    def GetColor(self,v):
        return self.G.vs[v]["color"]

    # return label at vertex v
    def GetLabel(self,v):
        return self.G.vs[v]["label"]

    def GetNeighbors(self,v):
        return self.G.neighbors(v)

    def GetVertexList(self):
        return self.G.vs

    def SetPoints(self,v,a):
        self.G.vs[v]["label"] = str(v)+":"+str(a)
        self.G.vs[v]["points"] = a

    def SetColor(self,v,a):
        self.G.vs[v]["color"] = a

    def SetLabel(self,v):
        self.G.vs[v]["label"] = a
