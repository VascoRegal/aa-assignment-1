from utils import subsets

class MinVertexCoverSolver:
	def __init__(self, problem):
		self.solution = []
		self.problem = problem

	def solve(self):
		for subset in subsets(self.problem.graph.vertexes):
			edges_covered = 0
			visited_edges = []
			for vertex in subset:
				inc_edges = self.problem.graph.get_incident_edges(vertex)
				for edge in inc_edges:
					if edge not in visited_edges:
						visited_edges.append(edge)
						edges_covered += 1

			if edges_covered == self.problem.E:
				if not self.solution or (len(subset) < len(self.solution)):
					self.solution = subset

		return self.solution 


