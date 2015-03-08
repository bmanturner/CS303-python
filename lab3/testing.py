import mergesort
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
		print 'Testing MERGE SORT with array of length ', len(num_array)
		print 'Running...'
		tmp = []
		for k in range(0,len(num_array)):
			tmp.append(num_array[k])
		start = time.clock()
		sorted_array = mergesort.mergeSort(num_array, tmp, 0, len(num_array)-1, 20)
		end = time.clock()
		total = (end - start)
		print 'This took %s nanoseconds in total' % (total*100000)
		print 'Verified: ', checksort.checksortAsc(sorted_array)
		print ''
