from igraph import *
import Ramsey.ramseyFunctions


K2 = Graph.Full(2)
K3 = Graph.Full(3)
K4 = Graph.Full(4)
K5 = Graph.Full(5)
K8 = Graph.Full(8)



K4dir = Graph.Full(4, directed=True)
K3dir = Graph.Full(3, directed=True)
K2dir = Graph.Full(2, directed=True)

dir2path = Graph(2, [(0,1)], directed=True)
dir3path = Graph(3, [(0,1),(1,2)], directed=True)
dir4path = Graph(4, [(0,1),(1,2),(2,3)], directed=True)
dir5path = Graph(5, [(0,1),(1,2),(2,3),(3,4)], directed=True)

paths = [dir2path, dir3path, dir4path, dir5path]

TT3 = Graph(3,[(0,1),(1,2),(0,2)], directed = True)
TT4 = Graph(4,[(1,0),(1,3),(0,2),(2,3),(0,3),(1,2)], directed=True)
TT5 = Graph(5,[(0,1),(1,2),(2,3),(3,4),(0,4),(0,3),(0,2),(1,4),(1,3),(2,4)], directed=True)

g = ramseyFunctions.directional_ramsey(K3dir, TT3, 9)
print(g.solve())




