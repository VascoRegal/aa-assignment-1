import random
import os

from consts import NMEC, MIN_COORDS, MAX_COORDS
from utils import max_edges
from solution import GreedySolver, ExhaustiveSolver, RandomizedSolver

import networkx as nx
#import matplotlib.pyplot as plt
import time
import json

random.seed(NMEC)

class Vertex:
	def __init__(self,id: str, x: int, y: int, cost: int = 0):
		self.x = x
		self.y = y
		self.id = id
		self.cost = cost

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

	def get_neighbors(self, vertex):
		N = []
		for edge in self.get_incident_edges(vertex):
			N.extend([v for v in edge.get_vertexes() if v != vertex])
		return N


class Problem:
	def __init__(self, V: int, percent_edges: float, solver: str = 'e'):
		self.V = V
		self.E = int(percent_edges/100 * max_edges(V))
		self.graph = Graph(self.V, self.E)
		self.visual = []
		self.generate_graph()				
		self.solution = []
		self.solver = solver
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
		if self.solver == 'g':
			solver = GreedySolver(self)
		elif self.solver == 'e':
			solver = ExhaustiveSolver(self)
		else:
			solver = RandomizedSolver(self)

		self.solution = solver.solve()
		self.time = time.time() - init

	def results(self):
		print()
		print("#######################################")
		print(f"V = {self.V} | E = {self.E}")
		print(f"Solver : {self.solver}")
		print(f"Solution computed in {self.time} s")
		print(f"Min Vertex Cover: {len(self.solution)}")
		print(f"C = {[str(x) for x in self.solution]}")
		print("#######################################")
		print()
	
	def plot_graph(self):
		G = nx.Graph()
		G.add_edges_from(self.visual)
		nx.draw_networkx(G)
		plt.show()
	
	def export(self, output_folder):
		if not os.path.exists(output_folder):
			os.makedirs(output_folder)

		file_name = f"{output_folder}/{self.V}"
		file_name += f" {self.solver}"

		with open(file_name, 'w') as f:
			json.dump({
				"solver": self.solver,
				"seed": NMEC,
				"V": self.V,
				"E": self.E,
				"solution": [v.id for v in self.solution],
				"time": self.time
			}, f)
	
			
