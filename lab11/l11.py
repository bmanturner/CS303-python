import collections

# GRAPH
class Graph(object):
	#GRAPH FUNCTIONS
	def __init__(self, directed = False):
		self.graph = collections.defaultdict(lambda: collections.defaultdict(int))
		self.directed = directed

	def __str__(self):
		result = ''
		for key in self.graph:
			result += "key %s: " % (key)
			result += str(self.graph[key])
			result += '\n'
		return result

	def addEdge(self, start, end):
		self.graph[start][end] += 1
		if not self.directed:
			self.graph[end][start] += 1

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
					print 'asdf'
					new_path = list(path)
					new_path.append(adjacent)
					queue.append(new_path)

					visited.add(node)

		return "Path not found"

	def printAllPaths(self, source):
		keys = self.graph.keys()
		for k in keys:
			if k and not int(k) == source:
				print "From %s to %s: " % (source, k)
				print self.BFS(source, int(k))
				print ''




if __name__ == '__main__':

	G = Graph(True)

	graph_file = "mediumG.txt"

	open_file = open(graph_file, "r")
	lines = open_file.readlines()
	open_file.close()

	for line in lines:
		nums = [int(n) for n in line.split()]
		if len(nums) > 1:
			G.addEdge(nums[0],nums[1])
		else:
			G.addEdge(nums[0], None)

	#print G

	print G.graph

	#G.printAllPaths(165)

	print G.BFS(245,0)
	print G.BFS(245,60)






