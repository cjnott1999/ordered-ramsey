from Ramsey import graphFunctions
from Ramsey import ramseyFunctions
from igraph import *


K4 = graphFunctions.complete_graph(4)


#current directory
file_path = ""

#four path
four_path = Graph(4, [(0,1),(1,2),(2,3)])

#display it 
plot(four_path)

#check all orderings and save them to text files
ramseyFunctions.check_all_orderings_tree_complete(four_path, K4, 40, file_path)