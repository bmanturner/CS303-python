import l1p1
import l1p2
import time
import random

if __name__ == '__main__':
	
	for x in range(1,4):

		num_file = 'input%s.txt' % (x)

		open_file = open(num_file, "r")
		line = open_file.readline()
		num_array = map(int, line.split())
		open_file.close()

		print ''
		print "Testing: ", num_file
		print "Array size: ", len(num_array)
		print ''
		print '================================================================'
		print "Now testing linear search with array of length ", len(num_array)
		print "Will run test 10000 times."
		print "Running..."
		start = time.clock()
		found = 0
		for x in range(10000):
			query = random.randint(0,1001)
			if (l1p1.linearSearch(num_array, query) != -1):
				found += 1
		end = time.clock()
		total = (end-start)
		print "This took %s seconds in total" % (total)
		print "%s nanoseconds on average" % ((total/10000)*1000000)
		print "Found %s of 10000 [irrelevant]" % (found)
		print '================================================================'
		print ''
		print '================================================================'
		print "Now testing recursive binary search with array of length ", len(num_array)
		print "Will run test 10000 times."
		print "Running..."
		start = time.clock()
		found = 0
		for x in range(10000):
			query = random.randint(0,1001)
			if (l1p2.recursiveBinarySearch(num_array, query) != -1):
				found += 1
		end = time.clock()
		total = (end-start)
		print "This took %s seconds in total" % (total)
		print "%s nanoseconds on average" % ((total/10000)*1000000)
		print "Found %s of 10000 [irrelevant]" % (found)
		print '================================================================'
		print ''

	