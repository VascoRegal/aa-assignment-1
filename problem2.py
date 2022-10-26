import random

from consts import NMEC, MIN_COORDS, MAX_COORDS
import networkx as nx
import matplotlib.pyplot as plt

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
	def __init__(self, V: int, E: int):
		self.V = V
		self.E = E
		self.graph = Graph(V, E)
		self.visual = []
		self.generate_graph()				

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
		passed_vertexes = []
		last_vertex = 0
		for i in range(self.E):
			while True:
				if (len(passed_vertexes) >= self.V):
					print(f"{len(passed_vertexes)} {self.V}")
					v1 = random.choice(self.graph.vertexes)
				else:
					print(last_vertex)
					v1 = self.graph.vertexes[last_vertex]
					last_vertex += 1

				v2 = random.choice(self.graph.vertexes)

				if ((v1 != v2) and (((v1,v2) not in edges)) and ((v2,v1) not in edges)):
					break
			
			passed_vertexes.append(v1)
			passed_vertexes.append(v2)	
			self.graph.edges.append(Edge(v1, v2))
			self.visual.append([v1.id, v2.id]) 	
			edges.append((v1,v2))
	
	def plot_graph(self):
		G = nx.Graph()
		G.add_edges_from(self.visual)
		nx.draw_networkx(G)
		plt.show()
			
			
if __name__ == '__main__':
	p = Problem(10,25)
	print([str(x) for x in p.graph.vertexes])
	p.plot_graph()
