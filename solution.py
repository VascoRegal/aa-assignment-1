import random

class Search:
	def __init__(self, problem):
		self.problem = problem
		self.root = None
		self.open_nodes = []

	def search(self):
		pass

	def add_to_open_nodes(self):
		pass

class ExhaustiveSearch(Search):
	def __init__(self, problem):
		super().__init__(problem)

	def search(self):
		solutions = []
		for edge in self.problem.graph.edges:
			C = []
			root = edge
			self.open_nodes = [root]
		
			while (self.open_nodes):
				node = self.open_nodes.pop(0)
				new_nodes = []
				incident_edges = []

				for vertix in node.get_vertixes():
					C.append(vertix)
					incident_edges += self.problem.graph.get_incident_edges(vertix)

				new_nodes.append()

	def add_to_open_nodes(self):
