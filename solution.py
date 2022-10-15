
class Search:
	def __init__(self, problem):
		self.problem = problem
		root = self.problem.graph.adjacency_list[0]
		self.open_nodes = [root]

	def search(self):
		pass

	def add_to_opens(sel):
		pass

class ExhaustiveSearch(Search):
	def __init__(self, problem):
		super().__init__(problem)

	def search(self):
		while (self.open_nodes) != []:
			node = self.open_nodes.pop(0)

			lnewnodes= []
			adjacent_nodes = []
