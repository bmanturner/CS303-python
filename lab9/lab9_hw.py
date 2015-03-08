import csv
import time

# NODE CLASS
class node(object):
	#NODE FUNCTIONS
	def __init__(self, data=None, quantity=None, product=None):
		self.key = data
		self.leftChild = None
		self.rightChild = None
		self.parent = None
		self.color = None
		self.quantity = quantity
		self.product = product

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

	def hasValue(self):
		if not self.key:
			return False
		else:
			return True

	def getValue(self):
		return self.key

	def getQuantity(self):
		return self.quantity

	def getProduct(self):
		return self.product

	def getColor(self):
		return self.color

	def isLessThan(self, comparator):
		if self.key < comparator.getValue():
			return True
		else:
			return False


# BINARY TREE CLASS
class RedBlackTree(object):

	# REDBLACKTREE FUNCTIONS
	def __init__(self):
		self.size = 0
		self.nil = node()
		self.nil.leftChild = self.nil
		self.nil.rightChild = self.nil
		self.nil.parent = self.nil
		self.root = self.nil


	def __str__(self):
		return self.printTreeHelper(self.root,0)

	def printTreeHelper(self, node, depth, position="root"):
		result = ""

		result += "value: %s     depth: %s     side: %s     color: %s \n" % (node.getValue(),depth,position,node.color)

		if node.leftChild != self.nil:
			result += (self.printTreeHelper(node.leftChild,depth+1,"left"))		

		if node.rightChild != self.nil:
			result += (self.printTreeHelper(node.rightChild,depth+1,"right"))

		return result


	def insert(self, newNode):
		self.size += 1
		y = self.nil
		curNode = self.root

		while curNode != self.nil:
			y = curNode

			if newNode.isLessThan(curNode):
				curNode = curNode.leftChild

			else:
				curNode = curNode.rightChild

		newNode.parent = y

		if y == self.nil:
			self.root = newNode

		elif newNode.isLessThan(y):
			y.leftChild = newNode

		else:
			y.rightChild = newNode

		newNode.leftChild = self.nil
		newNode.rightChild = self.nil
		newNode.color = "RED"
		self.insertFixUp(newNode)


	def insertFixUp(self, newNode):
		while newNode.parent.color == 'RED':

			if newNode.parent == newNode.parent.parent.leftChild:
				y = newNode.parent.parent.rightChild
				if y.color == 'RED':
					newNode.parent.color = 'BLACK'
					y.color = 'BLACK'
					newNode.parent.parent.color = 'RED'
					newNode = newNode.parent.parent
				else:
					if newNode == newNode.parent.rightChild:
						newNode = newNode.parent
						self.rotateLeft(newNode)
					newNode.parent.color = 'BLACK'
					newNode.parent.parent.color = 'RED'
					self.rotateRight(newNode.parent.parent)

			else:
				y = newNode.parent.parent.leftChild
				if y.color == 'RED':
					newNode.parent.color = 'BLACK'
					y.color = 'BLACK'
					newNode.parent.parent.color = 'RED'
					newNode = newNode.parent.parent
				else:
					if newNode == newNode.parent.leftChild:
						newNode = newNode.parent
						self.rotateRight(newNode)
					newNode.parent.color = 'BLACK'
					newNode.parent.parent.color = 'RED'
					self.rotateLeft(newNode.parent.parent)

		self.root.color = 'BLACK'


	def rotateLeft(self, pivotNode):
		rightOfPivot = pivotNode.rightChild
		pivotNode.rightChild = rightOfPivot.leftChild

		if rightOfPivot != self.nil:
			rightOfPivot.leftChild.parent = pivotNode

		rightOfPivot.parent = pivotNode.parent

		if pivotNode.parent == self.nil:
			self.root = rightOfPivot
		elif pivotNode == pivotNode.parent.leftChild:
			pivotNode.parent.leftChild = rightOfPivot
		else:
			pivotNode.parent.rightChild = rightOfPivot

		rightOfPivot.leftChild = pivotNode
		pivotNode.parent = rightOfPivot


	def rotateRight(self, pivotNode):
		leftOfPivot = pivotNode.leftChild
		pivotNode.leftChild = leftOfPivot.rightChild

		if leftOfPivot != self.nil:
			leftOfPivot.rightChild.parent = pivotNode

		leftOfPivot.parent = pivotNode.parent

		if pivotNode.parent == self.nil:
			self.root = leftOfPivot
		elif pivotNode == pivotNode.parent.rightChild:
			pivotNode.parent.rightChild = leftOfPivot
		else:
			pivotNode.parent.leftChild = leftOfPivot

		leftOfPivot.rightChild = pivotNode
		pivotNode.parent = leftOfPivot

	def search(self, UPC):
		product = self.searchHelper( UPC, self.root)
		print "\n UPC: ", product.getValue()
		print "Qty: ", product.getQuantity()
		print "Description: ", product.getProduct()

	def searchHelper(self, UPC, curNode):
		if (curNode.getValue() == UPC):
			return curNode
		elif (UPC < curNode.getValue()):
			return self.searchHelper(UPC, curNode.leftChild)
		else:
			return self.searchHelper(UPC, curNode.rightChild)







if __name__ == '__main__':
	
	storeInventory = RedBlackTree()

	with open("UPC.csv", "rb") as csv_file:

		print "\nLoading CSV..."
		start = time.clock()
		for product in csv.reader(csv_file.read().splitlines()):
			storeInventory.insert( node( product[0] , product[1], product[2]))
		end = time.clock()
		print "SUCCESS! CSV was loaded into memory in %s seconds." % (end - start)
		print "It contains %s products.\n" % (storeInventory.size)

		csv_file.close()

		query = ''

		while query != "done":
			query =  raw_input("\nInput UPC to search (type 'done' to exit): ")
			if query == 'done': break
			start = time.clock()
			storeInventory.search(query)
			end = time.clock()
			print "This took %s nanoseconds" % ((end-start)*1000000)

		




	#RBT = RedBlackTree()
	#print ''
	#for value in num_array:
	#	print "inserting %s" % (value)
	#	nodeToInsert = node(value)
	#	RBT.insert(nodeToInsert)
	#print ''
	#print RBT
	
	