import random


class SearchNode:
	def __init__(self, edge, open_edges, parent):
		self.parent = parent
		self.edge = edge
		self.open_edges = open_edges
		
	def edge_in_parent(self, edge):
		if (self.edge == edge):
			return True
		return False if not self.parent else self.parent.edge_in_parent(edge)

class Search:
	def __init__(self, problem):
		self.problem = problem		 
 		
		self.root_nodes = []

		for edge in problem.graph.edges:
			incident_edges = []
			for v in edge.get_vertexes():
				incident_edges += [e for e in self.problem.graph.get_incident_edges(v)]		
			self.root_nodes.append(SearchNode(edge, [e for e in self.problem.graph.edges if (e != edge) and e not in incident_edges], None))

	def search(self):
		pass

	def add_to_open_nodes(self):
		pass

class ExhaustiveSearch(Search):
	def __init__(self, problem):
		super().__init__(problem)

	def search(self):
		solutions = []
		for vertex in self.problem.graph.vertexes:
			C = []
			self.open_nodes = [vertex]
			self.open_nodes += [v for v in self.problem.graph.vertexes if v != vertex]	
			while (self.open_nodes):
				print(len(self.open_nodes))
				node = self.open_nodes.pop(0)
				incident_edges = self.problem.graph.get_incident_edges(vertex)
				
				passed_vertexes = []
				for edge in incident_edges:
					vertexes = edge.get_vertexes()
					[C.append(v) for v in vertexes if v not in C]
					passed_vertexes += vertexes 
				
				self.open_nodes = [v for v in self.open_nodes if v not in passed_vertexes]
			solutions.append(C)
		self.problem.graph.solution = min(solutions, key=lambda l: len(l))

	def path(self, node):
		if node.parent == None:
			return [node.edge]
		return self.path(node.parent) + [node.edge]

	def search2(self):
		solutions = []
		for root in self.root_nodes:
			self.open_nodes = [root]
			while (self.open_nodes):
				node = self.open_nodes.pop(0)				
				print(f"EDGE: {node.edge}\n")

				print(f"OPEN_EDGES:\n")
				for e in node.open_edges:
					print(str(e))
				print()

				if len(node.open_edges) == 0:
					sol = []
					for e in self.path(node):
						sol += e .get_vertexes()
					solutions.append(sol)

				else:
					vertixes = node.edge.get_vertexes()
					inc_edges = []
					for v in vertixes:
						inc_edges += self.problem.graph.get_incident_edges(v)
					print(inc_edges)
					open_edges = [edge for edge in node.open_edges if edge not in inc_edges and edge != node.edge]	
					for edge in open_edges:
						next_open = open_edges.copy()
						next_open.remove(edge)
						if not node.edge_in_parent(edge):
							self.open_nodes.append(SearchNode(edge, next_open, node))
		return min(solutions, key = lambda l: len(l))
