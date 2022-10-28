from problem import Problem
import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description = "Calculate min vertex cover of an undirected graph")

	parser.add_argument('vertexes',
						type=int,
						help='Number of Vertexes in the Graph')

	parser.add_argument('-p',
						action='store_true',
						help='Show the graph in a plot (True / False)')


	args = parser.parse_args()

	p = Problem(args.vertexes)

	if args.p:
		p.plot_graph()
	p.solve()
	p.results()
