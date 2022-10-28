import itertools

def max_edges(V:int):
	return int((V * (V - 1)) / 2)


def subsets(lst):
	res = []
	
	for i in range(len(lst)):
		res.extend(list(itertools.combinations(lst, i)))
	return res
