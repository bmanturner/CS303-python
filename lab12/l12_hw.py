from collections import defaultdict

# LINKED LIST CLASS
class linkedList(object):

	# NODE CLASS
	class node(object):
		#NODE FUNCTIONS
		def __init__(self, vertice, time):
			self.vertice = vertice
			self.time = time
			self.nextNode = None


	# LINKEDLIST FUNCTIONS
	def __init__(self):
		self.head = None
		self.length = 0

	def add(self, vertice, time):
		if not self.head:
			self.head = node(vertice, time)
		else:
			newNode = node(vertice, time)
			newNode.nextNode = self.head
			self.head = newNode



# GRAPH
class Graph(object):
	#GRAPH FUNCTIONS
	def __init__(self, directed = False):
		self.graph = defaultdict(list)
		self.directed = directed

	def __str__(self):
		result = ''
		for key in self.graph:
			result += "key %s: " % (key)
			result += str(self.graph[key])
			result += '\n'
		return result

	def addEdge(self, start, end):
		self.graph[start].append(end)
		if not self.directed:
			self.graph[end].append(start)

	def BFS(self, start, end):
		queue = []
		queue.append([start])
		visited = set()

		while queue:
			path = queue.pop(0)

			node = path[ len(path)-1 ]

			if node == end:
				return path

			elif node not in visited:

				for adjacent in self.graph[node]:
					new_path = list(path)
					new_path.append(adjacent)
					queue.append(new_path)

					visited.add(node)

		return "Path not found"

	def DFS(self, start = 0):
		self.black = set()
		self.gray = set()
		self.time = 0
		self.stack = []
		vertices = self.graph.keys()
		self.DFS_Visit(start)
		#for v in vertices:
		#	if v not in self.black and v not in self.gray:
		#		self.DFS_Visit(v)

	def DFS_Visit(self, v):
		self.stack.append(v)
		self.time += 1
		self.gray.add(v)
		for adjacent in self.graph[v]:
			if adjacent not in self.black and adjacent not in self.gray:
				self.DFS_Visit(adjacent)
		print "from 0 to %s" % (self.stack[len(self.stack) - 1])
		print self.stack
		print ''
		self.stack.pop()
		self.gray.remove(v)
		self.black.add(v)
		self.time += 1

	def topologicalSort(self):
		self.black = set()
		self.stack = []
		for vertice in self.graph.keys():
			if vertice not in self.black:
				self.topologicalSortVisit(vertice)

		while len(self.stack) > 0:
			print self.stack.pop()

	def topologicalSortVisit(self, v):
		if v:
			self.black.add(v)
			for adjacent in self.graph[v]:
				if adjacent not in self.black:
					self.topologicalSortVisit(adjacent)
			self.stack.append(v)


	def printAllPaths(self, source):
		keys = self.graph.keys()
		for k in keys:
			if k and not int(k) == source:
				print "From %s to %s: " % (source, k)
				print self.DFS(source)
				print ''




if __name__ == '__main__':

	G = Graph(True)

	graph_file = "tinyDG.txt"

	open_file = open(graph_file, "r")
	lines = open_file.readlines()
	open_file.close()

	for line in lines:
		nums = [int(n) for n in line.split()]
		if len(nums) > 1:
			G.addEdge(nums[0],nums[1])
		else:
			G.addEdge(nums[0], None)

	for vertice in G.graph.keys():
		print "%s: %s" % (vertice,G.graph[vertice])

	#print G.graph

	G.topologicalSort()

	#print G.BFS(245,0)
	#print G.BFS(245,60)






