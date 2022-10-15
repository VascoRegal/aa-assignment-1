from problem import Problem

if __name__ == '__main__':
	problem = Problem(5,4)
	problem.solve()
	print(problem.graph)
	print([node.vertix for node in problem.graph.get_adjacent_nodes(0)])
