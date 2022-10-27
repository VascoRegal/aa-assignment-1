
import random
import time

from solution import ExhaustiveSearch

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def get_vertixes(self):
        return [self.v1, self.v2]

    def __eq__(self, other):
        return (isinstance(other, Edge) and (self.v1 + self.v2) == (other.v1 + other.v2))

    def __str__(self):
        return f"{self.v1}  -  {self.v2}"

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E 
        self.edges = []

    def add_edge(self, src, dst):
        new_edge = Edge(src, dst)
        if new_edge not in self.edges:
            self.edges.append(Edge(src, dst))

    def get_incident_edges(self, vertix):
        return [edge for edge in self.edges if vertix in edge.get_vertixes()]

    def print_graph(self):
        s = ""
        for e in self.edges:
            print(e)
            print()
        print()

class Problem:
    def __init__(self, V, E):
        self.graph = Graph(V, E)
        self.generate_random_edges(V, E)
        self.solution = []

    def generate_random_edges(self, V, E):
        generated_edges = []
        v1 = 0
        v2 = 0	

        for e in range(E):
            while ((v1 == v2) or ((v1,v2) in generated_edges) or ((v2,v1) in generated_edges )):
                v1 = random.randint(0, V-1)
                v2 = random.randint(0, V-1)			
            self.graph.add_edge(v1, v2)
            generated_edges.append((v1,v2))
            v1 = 0
            v2 = 0
    
    def solve(self):
        self.time = time.time()
        es = ExhaustiveSearch(self)
        es.search2()
        self.time = time.time() - self.time
        self.results()

    def results(self):
        print(f"V = {self.graph.V} | E = {self.graph.E}")
        print(f"Finished in {self.time}")
        print(f"Min Vertex Cover: {len(self.solution)}")
        print(f"\t Vertex List: {self.solution}")






