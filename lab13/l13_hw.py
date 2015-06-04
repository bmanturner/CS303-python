import time

class Vertex(object):

  def __init__(self, key):
    self.id = key
    self.connectedTo = []
    self.priority = 99999999
    self.parent = None

  def __str__(self):
    return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

  def printAdjacent(self):
    print str(self.id) + ' is connected to:'
    for adj in self.connectedTo:
      print "                     %s (weight: %s)" % (adj[0].id, adj[1])

  def addConnection(self, adjacent, weight):
    self.connectedTo.append((adjacent, weight))

  def getConnections(self):
    return self.connectedTo.keys()

  def getId(self):
    return self.id

  def getWeight(self,adjancent):
    return self.connectedTo[adjacent]


class Graph(object):

  def __init__(self, directed = False):
    self.vertList = {}
    self.numVert = 0
    self.directed = directed

  def __iter__(self):
    return iter(self.vertList.values())

  def printAdjacencyList(self):
    for v in self.vertList:
      self.vertList[v].printAdjacent()

  def addVertex(self, key):
    self.numVert += 1
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex

  def getVertex(self, key):
    if key in self.vertList:
      return self.vertList[key]
    else:
      return None

  def addEdge(self, f, t, weight):
    if not self.getVertex(f):
      self.addVertex(f)
    if not self.getVertex(t):
      self.addVertex(t)
    self.vertList[f].addConnection(self.vertList[t], weight)
    if not self.directed:
      self.vertList[t].addConnection(self.vertList[f], weight)

  def getVertices(self):
    return self.vertList.keys()

  def primMST(self):
    verts = []
    for vert in self.getVertices():
      self.vertList[vert].priority = 99999999
      self.vertList[vert].parent = None
      verts.append(vert)
    while (len(verts) > 0):
      #print "verts: "
      #for vert in verts:
        #print "%s: %s" % (vert, self.vertList[vert].priority)
      #extract min
      curVec = None
      for vert in verts:
        if curVec == None:
          curVec = vert
        elif self.vertList[curVec].priority > self.vertList[vert].priority:
          curVec = vert
      verts.remove(curVec)
      #print "curVec: %s" % (curVec)
      for adjacent in self.vertList[curVec].connectedTo:
        #print "adjacent: "
        #print adjacent[0].id
        if adjacent[0].id in verts and adjacent[1] < self.vertList[curVec].priority:
          adjacent[0].parent = self.vertList[curVec]
          adjacent[0].priority = adjacent[1]




if __name__ == '__main__':
  g = Graph()

  graph_file = "xlarge.txt"
  print graph_file

  open_file = open(graph_file, "r")
  lines = open_file.readlines()
  open_file.close()

  for line in lines:
    nums = [n for n in line.split()]
    if len(nums) > 2:
      g.addEdge(int(nums[0]),int(nums[1]),float(nums[2]))
    else:
      g.addVertex(int(nums[0]))

  start = time.clock()
  g.primMST()
  end = time.clock()
  print 'This took %s seconds in total' % ((end-start))
