from problem import Problem
import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description = "Calculate min vertex cover of an undirected graph")

	parser.add_argument('vertexes',
						type=int,
						help='Number of Vertexes in the Graph')

	parser.add_argument('percent_edges',
						type=float,
						default=75,
						help='\% edges of number of vertices')

	parser.add_argument('-p', '--plot',
						action='store_true',
						help='Show the graph in a plot')

	
	parser.add_argument('-e', '--export',
						help='Export run to file')

	parser.add_argument('-g', '--greedy',
						action='store_true',
						help='Use greedy heuristics')

	args = parser.parse_args()

	p = Problem(args.vertexes, args.percent_edges, args.greedy)

	if args.plot:
		p.plot_graph()

	p.solve()

	if args.export:
		p.export(args.export)

	p.results()
