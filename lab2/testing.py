import sys
import l2p1
import time
import checksort

if __name__ == '__main__':
	for x in range(1,10):
		num_file = "input%s.txt" % (x)

		open_file = open(num_file, "r")
		line = open_file.readline()
		num_array = map(int, line.split())
		open_file.close()

		print '========================================='
		print "Testing: ", num_file
		print 'Testing insertion sort with array of length ', len(num_array)
		print 'Running...'
		start = time.clock()
		sorted_array = l2p1.insertionSort(num_array)
		end = time.clock()
		total = (end - start)
		print 'This took %s seconds in total' % (total)
		print 'Verified: ', checksort.checksortAsc(sorted_array)
		print ''

	