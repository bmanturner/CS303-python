# NODE CLASS
class node(object):
	#NODE FUNCTIONS
	def __init__(self, data=None, parent=None):
		self.key = data
		self.leftChild = None
		self.rightChild = None
		self.parent = parent

	def hasParent(self):
		if not self.parent:
			return False
		else:
			return True

	def hasLeft(self):
		if not self.leftChild:
			return False
		else:
			return True

	def hasRight(self):
		if not self.rightChild:
			return False
		else:
			return True

	def isLeft(self):
		return self.parent and self.parent.leftChild == self

	def isRight(self):
		return self.parent and self.parent.rightChild == self

	def getValue(self):
		return self.key

	def isLessThan(self, comparator):
		if self.key <= comparator.getValue():
			return True
		else:
			return False


# BINARY TREE CLASS
class BinarySearchTree(object):

	# BINARYSEARCHTREE FUNCTIONS
	def __init__(self):
		self.root = None
		self.size = 0

	def __str__(self):
		return self.printTreeHelper(self.root,0)

	def printTreeHelper(self, node, depth):
		result = ""

		if node.hasLeft():
			result += (self.printTreeHelper(node.leftChild,depth+1))

		result += "%s " % (node.getValue())

		if node.hasRight():
			result += (self.printTreeHelper(node.rightChild,depth+1))

		return result

	def insert(self, node):
		if not self.root:
			self.root = node
		else:
			self.insertHelper(node,self.root)
		self.size += 1

	def insertHelper(self, insertNode, curNode):
		if insertNode.isLessThan(curNode):
			if curNode.hasLeft():
				self.insertHelper(insertNode, curNode.leftChild)
			else:
				insertNode.parent = curNode
				curNode.leftChild = insertNode
		else:
			print "curNode was less than insertNode"
			if curNode.hasRight():
				self.insertHelper(insertNode, curNode.rightChild)
			else:
				insertNode.parent = curNode
				curNode.rightChild = insertNode

	def search(self, queryNode):
		return self.searchHelper(queryNode, self.root)

	def searchHelper(self, queryNode, curNode):
		if (curNode.getValue() == queryNode.getValue()):
			return curNode
		elif (queryNode.isLessThan(curNode)):
			return self.searchHelper(queryNode, curNode.leftChild)
		else:
			return self.searchHelper(queryNode, curNode.rightChild)

	def delete(self, queryNode):
		nodeToDelete = self.search(queryNode)
		return self.deleteHelper(nodeToDelete)

	def deleteHelper(self, delNode):
		if not delNode.hasLeft():
			self.transplant(delNode, delNode.rightChild)
		elif not delNode.hasRight():
			self.transplant(delNode, delNode.leftChild)
		else:
			y = self.treeMinimum(delNode.rightChild)
			if delNode != y.parent:
				self.transplant(y, y.rightChild)
				y.rightChild = delNode.rightChild
				y.rightChild.parent = y
			self.transplant(delNode, y)
			y.leftChild = delNode.leftChild
			y.leftChild.parent = y
		self.size -= 1

	def transplant(self, u, v):
		if not u.hasParent():
			self.root = v
		elif u == u.parent.leftChild:
			u.parent.leftChild = v
		else:
			u.parent.rightChild = v
		if v:
			v.parent = u.parent

	def treeMinimum(self,curNode):
		if not curNode.hasLeft():
			return curNode
		else:
			return self.treeMinimum(curNode.leftChild)


if __name__ == '__main__':
	
	#num_file = "Input_lab7.txt" % (x)
	#open_file = open(num_file, "r")
	#line = open_file.readline()
	#num_array = map(int, line.split())
	#open_file.close()

	ary = [7,32,24,54,23,98,1,5,2,8,6,44,78]
	BT = BinarySearchTree()
	for data in ary:
		print "inserting node with value: ", data
		nodeToInsert = node(data)
		print "confirming value of node: ", nodeToInsert.getValue()
		BT.insert(nodeToInsert)
	print BT
	nodeToSearch = node(8)
	result = BT.search(nodeToSearch)
	print result.getValue()
	nodeToDelete = node(1)
	BT.delete(nodeToDelete)
	print BT
	nodeToDelete = node(98)
	BT.delete(nodeToDelete)
	print BT
	nodeToDelete = node(32)
	BT.delete(nodeToDelete)
	print BT
	nodeToDelete = node(7)
	BT.delete(nodeToDelete)
	print BT