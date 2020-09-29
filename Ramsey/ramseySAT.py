#import necessary packages
import itertools
from igraph import *

from pysat.solvers import Glucose4
from pysat.formula import IDPool
from pysat.formula import CNF

class RamseySolver:
    #set the IDpool for assigning ID to variables
    #set the CNF object for holding the SAT clauses
    def __init__(self):
        self.vpool = IDPool()
        self.cnf = CNF()

    def generate_clauses(self, graph, N, color):
        """Takes an igraph Graph object and Candidate ramsey number, and the color of the edges"""
        number_of_vertices = graph.vcount()
        list_of_edges = graph.get_edgelist()

        #dictionary to hold the current variables 
        variables = {}
        for combo in itertools.combinations(range(N), number_of_vertices):
            for i in range(number_of_vertices):
                variables[str(i)] = combo[i]

            clause = []
            for edge in list_of_edges:
                if color:
                    clause.append(self.vpool.id((variables[str(edge[0])], variables[str(edge[1])])))
                else:
                    clause.append(-self.vpool.id((variables[str(edge[0])], variables[str(edge[1])])))
            self.cnf.append(clause)

    def generate_directional_clauses(self, graph, N, color):
        """Takes an igraph Graph object and Candidate ramsey number, and the color of the edges"""
        number_of_vertices = graph.vcount()
        list_of_edges = graph.get_edgelist()

        #dictionary to hold the current variables 
        variables = {}
        for combo in itertools.permutations(range(N), number_of_vertices):
            for i in range(number_of_vertices):
                variables[str(i)] = combo[i]

            clause = []
            for edge in list_of_edges:
                if color:
                    clause.append(self.vpool.id((variables[str(edge[0])], variables[str(edge[1])])))
                else:
                    clause.append(-self.vpool.id((variables[str(edge[0])], variables[str(edge[1])])))
            self.cnf.append(clause)
    
    def ordered_ramsey(self, red_graph, blue_graph, N):
        """Generte a Solver object with the generated CNF from the red and blue graphs"""
        self.generate_clauses(red_graph, N, True)
        self.generate_clauses(blue_graph, N, False)
        return Glucose4(self.cnf, use_timer=True)

    def directional_ramsey(self, red_graph, blue_graph, N):
        self.generate_directional_clauses(red_graph, N, True)
        self.generate_directional_clauses(blue_graph, N, False)
        return Glucose4(self.cnf, use_timer=True)

    def ordered_ramsey_tree_complete(self, tree_graph, complete_graph, N = None):
        """Special case when the provided graphs are a tree and a complete graph; in this case the ramsey number is known"""
        if N == None:
            N = (tree_graph.vcount() - 1) * (complete_graph.vcount()- 1) + 1
        return self.ordered_ramsey(tree_graph, complete_graph, N)
    
    def ordinary_ramsey_tree_complete(self, list_of_trees, number_of_vertices, complete_graph, N):
        """Tests the ordinary ramsey number of a tree and a complete graph, given a list of all orderings on that tree"""
        for tree in list_of_trees:
            graph = Graph()
            graph.add_vertices(number_of_vertices)
            graph.add_edges(tree)
            self.generate_clauses(graph, N, True)
        
        self.generate_clauses(complete_graph, N, False)
        return Glucose4(self.cnf)
    
    def writeCNF(self, name="clasues.cnf"):
        self.cnf.to_file(name)

