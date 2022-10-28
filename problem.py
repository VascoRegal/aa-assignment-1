import random

from consts import NMEC, MIN_COORDS, MAX_COORDS
from utils import max_edges
from solution import MinVertexCoverSolver

import networkx as nx
import matplotlib.pyplot as plt
import time

random.seed(NMEC)

class Vertex:
	def __init__(self,id: str, x: int, y: int):
		self.x = x
		self.y = y
		self.id = id

	def __str__(self):
		return str(f"V{self.id}({self.x}, {self.y})")

	def __eq__(self, other):
		return (isinstance(other, Vertex) and self.id == other.id) 
	
	def __hash__(self):
		return self.id

class Edge:
	def __init__(self, v1: Vertex, v2: Vertex):
		self.v1 = v1
		self.v2 = v2

	def get_vertexes(self):
		return [self.v1, self.v2]

	def __str__(self):
		return f"{self.v1.id} ---- {self.v2.id}"

class Graph:
	def __init__(self, V: int, E: int):
		self.vertexes = []
		self.edges = []

	def get_incident_edges(self, vertex):
		return [edge for edge in self.edges if vertex in edge.get_vertexes()]


class Problem:
	def __init__(self, V: int):
		self.V = V
		self.E = int(0.5 * max_edges(V))
		self.graph = Graph(self.V, self.E)
		self.visual = []
		self.generate_graph()				
		self.solution = []
		self.time = 0

	def generate_graph(self):
		positions = []
		for i in range(self.V):
			while True:
				x = random.randint(MIN_COORDS, MAX_COORDS)
				y = random.randint(MIN_COORDS, MAX_COORDS)
				if (x, y) not in positions:
					break
			self.graph.vertexes.append(Vertex(i, x, y))
	
		edges = []
		priority_vertexes = self.graph.vertexes.copy()
		passed_vertexes = []
		for i in range(self.E):
			while True:
				if (not priority_vertexes):
					v1 = random.choice(self.graph.vertexes)
				else:
					v1 = priority_vertexes[0]

				v2 = random.choice(self.graph.vertexes)	
				if ((v1 != v2) and (((v1,v2) not in edges)) and ((v2,v1) not in edges)):
					break
			
			if v1 in priority_vertexes: priority_vertexes.remove(v1)
			if v2 in priority_vertexes: priority_vertexes.remove(v2)	
			self.graph.edges.append(Edge(v1, v2))
			self.visual.append([v1.id, v2.id]) 	
			edges.append((v1,v2))

	def solve(self):
		init = time.time()
		solver = MinVertexCoverSolver(self)
		self.solution = solver.solve()
		self.time = time.time() - init

	def results(self):
		print(f"V = {self.V} | E = {self.E}")
		print(f"Solution computed in {self.time} s")
		print(f"Min Vertex Cover: {len(self.solution)}")
		print(f"C = {[str(x) for x in self.solution]}")
	
	def plot_graph(self):
		G = nx.Graph()
		G.add_edges_from(self.visual)
		nx.draw_networkx(G)
		plt.show()
			
			
if __name__ == '__main__':
	p = Problem(6)
	p.plot_graph()
	p.solve()
	p.results()
