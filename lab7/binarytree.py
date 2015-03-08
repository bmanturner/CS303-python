# BINARY TREE CLASS
class BinaryTree(object):

	# NODE CLASS
	class node(object):
		#NODE FUNCTIONS
		def __init__(self, int=None):
			self.int = int
			self.leftChild = None
			self.rightChild = None

		def hasLeft(self):
			if not self.leftChild:
				return False
			else:
				return True

		def hasRight(self):
			if not self.leftChild:
				return False
			else:
				return True

		def hasValue(self):
			if self.int != None and self.int != -1:
				return True
			else:
				return False
		
	# BINARYTREE FUNCTIONS
	def __init__(self):
		self.root = None
		self.height = 0
		self.max = 0

	def add(self, array, index=0):
		if not self.root:
			self.root = BinaryTree.node(array[0])
			parent = self.root
		else:
			if array[index] != -1:
				parent = BinaryTree.node(array[index])
			else:
				parent = BinaryTree.node()
		left = index*2+1
		right = left + 1
		if left < len(array):
			parent.leftChild = self.add(array, left)
		if right < len(array):
			parent.rightChild = self.add(array, right)
		return parent

	def __str__(self):
		return self.printTreeHelper(self.root,0)
			
	def printTreeHelper(self, node, depth):
		result = ""

		if node.hasValue():
			result += "%s " % (node.int)

		if node.hasLeft():
			result += (self.printTreeHelper(node.leftChild,depth+1))

		if node.hasRight():
			result += (self.printTreeHelper(node.rightChild,depth+1))

		return result

	def getTreeHeight(self):
		self.height = 0
		return self.getTreeHeightHelper(self.root)

	def getTreeHeightHelper(self, node, depth=0):
		if node.hasValue() and depth > self.height:
			self.height = depth

		if node.hasLeft():
			self.getTreeHeightHelper(node.leftChild,depth+1)

		if node.hasRight():
			self.getTreeHeightHelper(node.rightChild,depth+1)

		return self.height

	def getLargestPath(self):
		self.max = self.root.int
		return self.getLargestPathHelper(self.root)

	def getLargestPathHelper(self,node):
		if not node.hasValue():
			return 0

		if node.hasLeft():
			leftVal = max(self.getLargestPathHelper(node.leftChild), 0)
		else:
			leftVal = 0
		
		if node.hasRight():
			rightVal = max(self.getLargestPathHelper(node.rightChild), 0)
		else:
			rightVal = 0

		self.max = (node.int + leftVal + rightVal, self.max)

		return node.int + max(leftVal,rightVal)



if __name__ == '__main__':
	
	#num_file = "Input_lab7.txt" % (x)
	#open_file = open(num_file, "r")
	#line = open_file.readline()
	#num_array = map(int, line.split())
	#open_file.close()

	ary = [6,11,4,10,7,2,9,-1,-1,-1,12,-1,1,5,8,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,3]
	BT = BinaryTree()
	BT.add(ary)
	print BT
	print BT.getTreeHeight()
	print BT.getLargestPath()