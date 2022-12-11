from problem import Problem
import argparse

SOLVERS = ['e', 'g', 'r']

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

	parser.add_argument('-s', '--solver',
						help='Shoose solver - (E)xhaustive | (G)reedy | (R)andomized')
	parser.add_argument('-i', '--iters',
						help='Random algorithm iterations')	

	args = parser.parse_args()



	s = args.solver.lower() if args.solver else None
	kwargs = {}
	if s and s == 'r':
		iters = args.iters if args.iters else None
		if iters:
			kwargs['iters'] = int(iters)

	p = Problem(args.vertexes, args.percent_edges, args.solver, kwargs)

	if args.plot:
		p.plot_graph()

	p.solve()

	if args.export:
		p.export(args.export)

	p.results()
