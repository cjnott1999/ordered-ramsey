from igraph import *

def to_simple_path(edges):
	"""Converts an edgeslist to a simple path"""
	edge_list = []
	for i in range(len(edges) - 1):
		first_pair = edges[i]
		second_pair = edges[i + 1]
		
		if first_pair[0] == second_pair[0]:
			edge_list.append(first_pair[1])
			if i == len(edges) - 2:
				edge_list.append(first_pair[0])
				edge_list.append(second_pair[1])
				
		if first_pair[1] == second_pair[1]:
			edge_list.append(first_pair[0])
			if i == len(edges) - 2:
				edge_list.append(first_pair[1])
				edge_list.append(second_pair[0])
				
		if first_pair[0] == second_pair[1]:
			edge_list.append(first_pair[1])
			if i == len(edges) - 2:
				edge_list.append(first_pair[0])
				edge_list.append(second_pair[0])
				
		if first_pair[1] == second_pair[0]:
			edge_list.append(first_pair[0])
			if i == len(edges) - 2:
				edge_list.append(first_pair[1])
				edge_list.append(second_pair[1])
	return edge_list

def label_vertices(graph):
    """Label the vertices of the given igraph object with the current edge ordering"""
    number = graph.vcount()
    for i in range(number):
        graph.vs[i]["label"] = str(i)


def label_edges(graph):
    """Label the edges of the given igraph object with the current edge ordering"""
    number = graph.ecount()
    for i in range(number):
        graph.es[i]["label"] = str(i)

def complete_graph(N):
	"""returns the complete graph on N vertices"""
	return Graph.Full(N)