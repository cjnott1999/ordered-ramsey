from Ramsey import ramseySAT
from Ramsey import graphFunctions
from igraph import *

K3 = graphFunctions.complete_graph(3)
K4 = graphFunctions.complete_graph(4)


ramsey = ramseySAT.RamseySolver()
ramsey.ordered_ramsey_tree_complete(K3, K4, 9)
ramsey.writeCNF()
