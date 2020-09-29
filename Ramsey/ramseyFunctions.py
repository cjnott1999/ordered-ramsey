import itertools
import Ramsey.ramseySAT as ramseySAT
import re

from pysat.solvers import Glucose4
from threading import Timer


def _interrupt(s):
    """Interupt the current solver"""
    s.interrupt()

def load_graphs(filepath):
    """load graphs, given as edgelists, from a given file path"""
    f = open(filepath, "r")
    loaded_graphs = [] 
    for graph_string in f:
        graph =[]
        parsed = re.findall("\((.*?)\)", graph_string)
        for string in parsed:
            res = tuple(map(int, string.split(',')))
            graph.append(res)
        loaded_graphs.append(graph)

    return loaded_graphs

def check_all_orderings_tree_complete(tree_graph, complete_graph,timeout, path = ""):
    """Check all possible orderings on a given tree and complete graph"""
    #All permuted orderings on a particular tree
    orderings = itertools.permutations(range(tree_graph.vcount()), tree_graph.vcount())

    bad = open(path + "badTrees.txt", "w")
    good = open(path + "goodTrees.txt", "w")

    #Sets have constant time lookup
    edge_orderings = set()

    #Gotta check them all
    for order in orderings:
        #create a new Ramsey Solver
        ramsey = ramseySAT.RamseySolver()
        #permute the tree, given a permutation 
        tree_permute = tree_graph.permute_vertices(list(order))

        #generate the edgelist for saving to the files
        #then check if the edgelist is in fact, unique, we only care about unique edge sets
        edgelist = tree_permute.get_edgelist()
        hashable_edge_list = frozenset(edgelist)

        if hashable_edge_list in edge_orderings:
            continue
        else:
            edge_orderings.add(hashable_edge_list)
            pass

        #generate the Glucose instance 
        g = ramsey.ordered_ramsey_tree_complete(tree_permute, complete_graph)

        #set the time limit and start the timer
        timer = Timer(timeout, _interrupt, [g])
        timer.start() 

        #attempt to compute the result, it will timeout after the elapsed time and return None
        result = g.solve_limited(expect_interrupt=True)

        #if it computes instantly, cancel the timer so that we dont wait
        timer.cancel()

        #if it returned none, it was interrupted, likely good ordering
        if result == None:
            good.write(str(edgelist) + "\n")
        #otherwise, it returned a satisfying assignment and is therefore a bad ordering
        else:
            if result == False:
                good.write(str(edgelist) + "\n")
            else:
                bad.write(str(edgelist) + "\n")  
 
        #clear the interrupt then remove from memory so the cycle can continue
        g.clear_interrupt()
        g.delete()
        del ramsey

    bad.close()
    good.close()

def ordered_ramsey(red_graph, blue_graph, N):
    """Tests for satisfiability between two ordered graphs"""
    ramsey = ramseySAT.RamseySolver()
    g = ramsey.ordered_ramsey(red_graph, blue_graph, N)
    return g

def directional_ramsey(red_graph, blue_graph, N):
    """Tests for satisfiability between two directed graphs"""
    ramsey = ramseySAT.RamseySolver()
    g = ramsey.directional_ramsey(red_graph, blue_graph, N)
    return g

def ordered_ramsey_tree_complete(tree, complete_graph, N = None):
    """Tests for satisfiability between an ordered tree and a complete graph"""
    ramsey = ramseySAT.RamseySolver()
    g = ramsey.ordered_ramsey_tree_complete(tree, complete_graph, N)
    return g


def ordinary_ramsey_tree_complete(list_of_trees, number_of_vertices ,complete_graph, N):
    """Test for satisfiability between an unordered tree and a complete graph"""
    ramsey = ramseySAT.RamseySolver()
    g = ramsey.ordinary_ramsey_tree_complete(list_of_trees, number_of_vertices, complete_graph, N)
    return g

