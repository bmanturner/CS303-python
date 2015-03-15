import time
import csv

# hashELEMENT
class HashElement(object):
	#hashELEMENT FUNCTIONS
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def getKey(self):
		return self.key

	def getValue(self):
		return self.value


# hashMAP CLASS
class HashMap(object):

	# hashMap FUNCTIONS
	def __init__(self, size = 100):
		self.size = size
		self.map = [None]*size

	def put(self, key, value):
		index = key % self.size
		while self.map[index] and self.map[index].getKey() != key:
			index = (7 * index + 1) % self.size
		self.map[index] = HashElement(key, value)

		return index

	def get(self, key):
		index = key % self.size
		while self.map[index] and self.map[index].getKey() != key:
			index = (7 * index + 1) % self.size

		return self.map[index].getValue()

	def linearPut(self, key, value):
		index = key % self.size
		linear_progress = 1
		while self.map[index] and self.map[index].getKey() != key:
			index = (key + linear_progress) % self.size
			linear_progress += 1
		self.map[index] = HashElement(key, value)

		return index

	def linearGet(self, key):
		index = key % self.size
		linear_progress = 1
		while self.map[index] and self.map[index].getKey() != key:
			index = (key + linear_progress) % self.size
			linear_progress += 1

		return self.map[index].getValue()

	def quadraticPut(self, key, value):
		index = key % self.size
		timesProbed = 0
		while self.map[index] and self.map[index].getKey() != key:
			timesProbed += 1
			index = (key + (2 * timesProbed) - 1) % self.size
		self.map[index] = HashElement(key, value)

	def quadraticGet(self, key):
		index = key % self.size
		timesProbed = 0
		while self.map[index] and self.map[index].getKey() != key:
			timesProbed += 1
			index = (key + (2 * timesProbed) - 1) % self.size
			
		return self.map[index].getValue()



if __name__ == '__main__':

	with open("UPC.csv", "rb") as csv_file:

		HM = HashMap(650000)

		print "\nLoading CSV..."
		start = time.clock()
		for product in csv.reader(csv_file.read().splitlines()):
			print product[0]
			HM.quadraticPut(long(product[0]),product[2])
		csv_file.close()
		end = time.clock()
		print "This took %s seconds." % (end-start)

		query = ''

		while query != "done":
			query =  raw_input("\nInput UPC to search (type 'done' to exit): ")
			if query == 'done': break
			start = time.clock()
			print "Quadratic: ", HM.quadraticGet(long(query))
			end = time.clock()
			print "This took %s nanoseconds" % ((end-start)*1000000)
	
	