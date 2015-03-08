class item(object):
	def __init__(self, int):
		self.priority = int

	def compareTo(self, comparator):
		if self.priority <= comparator.priority:
			return True
		else:
			return False

	def equals(self, item):
		if self == item:
			return True
		else:
			return False


class PriorityQueue(object):
	def __init__(self):
		self.queue = []
		self.length = 0

	def insert(self, item):
		if len(self.queue) > self.length:
			self.queue[self.length] = item
		else:
			self.queue.append(item)
		index = self.length
		self.length += 1
		return self.float(index)

	def float(self, index):
		k = index
		while (k > 0 and self.queue[k].compareTo(self.queue[k/2])):
			self.queue[k], self.queue[k/2] = self.queue[k/2], self.queue[k]
			k = k/2
		return k

	def sink(self, index):
		A = self.queue
		parent = index
		left = parent*2+1
		right = left + 1
		if left <= self.length-1 and A[left].compareTo(A[parent]):
			swap_index = left
		else:
			swap_index = parent
		if right <= self.length-1 and A[right].compareTo(A[swap_index]):
			swap_index = right
		if swap_index != parent:
			A[parent], A[swap_index] = A[swap_index], A[parent]
			self.sink(swap_index)
		return swap_index

	def findItemIndex(self, item):
		A = self.queue
		for parent in range((self.length-2)/2,-1,-1):
			if A[parent].compareTo(item):
				left = parent*2+1
				right = left + 1
				if left <= self.length-1 and A[left].equals(item):
					return left
				elif right <= self.length-1 and A[right].equals(item):
					return right
				elif A[parent].equals(item):
					return parent
		return -1

	def remove(self, item):
		A = self.queue
		index = self.findItemIndex(item)
		if index == -1:
			return False
		else:
			A[index], A[self.length-1] = A[self.length-1], A[index]
			self.length -= 1
			A[self.length] = None
			self.sink(index)
			return True

	def printQueue(self):
		print "===Printing Queue==="
		for index in range(self.length):
			print self.queue[index].priority


if __name__ == '__main__':
	PQ = PriorityQueue()
	A = item(10)
	B = item(9)
	C = item(8)
	D = item(7)
	E = item(6)
	F = item(5)
	G = item(4)
	H = item(3)
	I = item(2)
	J = item(1)
	PQ.insert(A)
	PQ.insert(B)
	PQ.insert(C)
	PQ.insert(D)
	PQ.insert(E)
	PQ.insert(F)
	PQ.insert(G)
	PQ.insert(H)
	PQ.insert(I)
	PQ.insert(J)
	print PQ.remove(J)
	print PQ.remove(A)
	print PQ.remove(H)
	PQ.insert(H)
	print PQ.remove(H)
	PQ.printQueue()