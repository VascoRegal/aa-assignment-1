import random
from utils import max_edges
from solution import exhaustive
import time

class Node:
	def __init__(self, vertix: int):
		self.vertix = vertix
		self.next_node = None


class Graph:
	def __init__(self, V: int):
		self.V = V
		self.adjacency_list = [None] * V
	
	def add_edge(self, src:int, dest:int):
		dest_node = Node(dest)
		dest_node.next = self.adjacency_list[src]
		self.adjacency_list[src] = dest_node
		
		src_node = Node(src)
		src_node.next = self.adjacency_list[dest]
		self.adjacency_list[dest] = src_node

	def __str__(self):
		s = ""
		for i in range(self.V):
            		s += f"Adjacency list of  V{i}\n V{i} "
            		temp = self.adjacency_list[i]
            		while temp:
                		s+= f" -> V{temp.vertix} "
                		temp = temp.next
            		s+= " \n"
		return s



class Problem:
	def __init__(self, V: int, E: int):
		self.V = V
		self.E = E
		self.graph = Graph(V)
		max_E = max_edges(V)
		if (E > max_E):
			E = max_E

		self.generate_random_edges(V, E)
		self.time = 0
		self.solution = []

	def generate_random_edges(self, V:int, E:int):
		generated_edges = []
		v1 = 0
		v2 = 0	

		for e in range(E):
			while ((v1 == v2) or ((v1,v2) in generated_edges) or ((v2,v1) in generated_edges )):
				v1 = random.randint(0, V-1)
				v2 = random.randint(0, V-1)			
			self.graph.add_edge(v1, v2)
			generated_edges.append((v1,v2))
			v1 = 0
			v2 = 0

	def solve(self):
		self.time = time.time()

		

		self.time = time.time() - self.time
		self.results()

	def results(self):
		print(f"V = {self.V} | E = {self.E}")
		print(f"Finished in {self.time}")
		print(f"Min Vertex Cover: {self.solution}")


