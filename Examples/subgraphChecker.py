from igraph import *
import Ramsey.badnessChecking
import Ramsey.ramseyFunctions


number_of_vertices = 8

bad_graphs = ramseyFunctions.load_graphs("Trees/K4/8 Vertices/Isomorphism17/badTrees.txt")
good_graphs = ramseyFunctions.load_graphs("Trees/K4/8 Vertices/Isomorphism17/goodTrees.txt")

four_path = Graph.Tree(4,1)

badnessChecking.check_list_of_graphs(bad_graphs, number_of_vertices, four_path, badnessChecking.bad_four_paths)
badnessChecking.check_list_of_graphs(good_graphs, number_of_vertices, four_path, badnessChecking.bad_four_paths)