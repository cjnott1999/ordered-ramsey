from igraph import *

bad_four_paths = [[0, 2, 1, 3],
[0, 2, 3, 1],
[0, 3, 1, 2],
[0, 3, 2, 1],
[1, 0, 3, 2],
[1, 2, 0, 3],
[1, 3, 0, 2],
[2, 0, 1, 3],
[2, 1, 0, 3]]

bad_four_paths_ramsey = {"[0, 2, 1, 3]]" : 11,
"[0, 2, 3, 1]" : 13,
"[0, 3, 1, 2]" : 11,
"[0, 3, 2, 1]" : 13,
"[1, 0, 3, 2]" :13,
"[1, 2, 0, 3]" : 11,
"[1, 3, 0, 2]" : 14,
"[2, 0, 1, 3]" : 13,
"[2, 1, 0, 3]" :13 }


#Function to convert an ordered path to a standard ordered path 
# [6,32,1,3] -> [2,3,0,1]		
def convert_to_standard_path(path):
	"""Takes a path in non standard form and converts to a standard path"""
	"""[6,32,1,3] -> [2,3,0,1]"""
	#store the indices of the current values 
	mappings = {}
	for i in range(len(path)):
		mappings[path[i]] = i

	#loop through and replace values in the path with their standard value, smallest to highest
	for i in range(len(path)):
		min_value = min(mappings)
		path[mappings[min_value]] = i
		del mappings[min_value]
	return path
	

#This function "slides" through the paths of a graph and checks if these are bad paths
#tree - tree provided as edgelist 
#N - the number of vertices in the tree 
#path - the isomorphic sub path to forbid
#bad_paths - the list of bad paths to compare to 
def graph_slide(tree, N, path, bad_paths):
    """ \"Slides\" through the subpaths of a graph and checks theese against the given bad paths"""	
    #Create the igraph object from the list of edges given
    #We do this so we can find the isomporphic subgraphs 
    graph = Graph()
    graph.add_vertices(N)
    graph.add_edges(tree)

	#get all the subpaths isomorphic to the path provided
    sub_paths = graph.get_subisomorphisms_vf2(path)

	#for each of these sub paths, convert it to a standard path and check if its in the list of bad paths
    for sub_path in sub_paths:
        standardized = convert_to_standard_path(sub_path)
		#if one of the sub-paths is in there, we dont need to keep looking
		#count it as a graph with a bad sub path
        if standardized in bad_paths:
            print(graph.get_edgelist())
            return 1
            break
		#we also need to check if the reverse path is in bad paths
        standardized.reverse()
        if standardized in bad_paths:
            print(graph.get_edgelist())
            return 1
            break
	#if the graph had no bad sub paths, report it
    return 0

def contains_bad_subpath(graph,subpath, bad_paths):
	"""Detemines if a graph contains a bad bath"""
	number_of_vertices = graph.vcount()
	if graph_slide(graph, number_of_vertices, subpath, bad_paths) == 1:
		print("Graph contained a bad subpath")
	else:
		print("Graph did not contain a bad subpath")
	
def check_list_of_graphs(list_of_edgelists, N, subpath, bad_paths):
	"""Checks a given lists of graphs as edgelists to see if all or none contain a bad four path"""
	count = 0
	for graph in list_of_edgelists:
		count =  count + graph_slide(graph, N, subpath, bad_paths)
	if count == len(list_of_edgelists):
		print("Every graph contained a bad subpath")
	elif count == 0:
		print("No graph contained a bad subpath")
	else:
		print("Some graph did (not) contain a bad subpath")
