import heapsort
import quicksort
import med3quicksort
import checksort
import mixedsort
import insertionsort
import mergesort
import time

if __name__ == '__main__':

	for x in range(1,11):
		num_file = "input_%s.txt" % (x)

		open_file = open(num_file, "r")
		line = open_file.readline()
		o_array = map(int, line.split())
		open_file.close()

		print '========================================='
		print "Testing: ", num_file
		print 'Testing MIXED SORT with array of length ', len(o_array)
		print 'Sorting...'
		num_array = []
		for k in range(0,len(o_array)):
			num_array.append(o_array[k])
		tmp = []
		for k in range(0,len(num_array)):
			tmp.append(num_array[k])
		start = time.clock()
		sorted_array = mixedsort.mixedSort(num_array,tmp,0,len(num_array)-1,16)
		end = time.clock()
		total = (end - start)
		print 'This took %s nanoseconds in total' % (total*100000)
		print 'Verified: ', checksort.checksortAsc(sorted_array)
		print ''

		print '========================================='
		print "Testing: ", num_file
		print 'Testing MERGE SORT with array of length ', len(o_array)
		print 'Sorting...'
		num_array = []
		for k in range(0,len(o_array)):
			num_array.append(o_array[k])
		tmp = []
		for k in range(0,len(num_array)):
			tmp.append(num_array[k])
		start = time.clock()
		sorted_array = mergesort.mergeSort(num_array,tmp,0,len(num_array)-1)
		end = time.clock()
		total = (end - start)
		print 'This took %s nanoseconds in total' % (total*100000)
		print 'Verified: ', checksort.checksortAsc(sorted_array)
		print ''

		print '========================================='
		print "Testing: ", num_file
		print 'Testing HEAP SORT with array of length ', len(o_array)
		print 'Sorting...'
		num_array = []
		for k in range(0,len(o_array)):
			num_array.append(o_array[k])
		start = time.clock()
		sorted_array = heapsort.heapSort(num_array)
		end = time.clock()
		total = (end - start)
		print 'This took %s nanoseconds in total' % (total*100000)
		print 'Verified: ', checksort.checksortAsc(sorted_array)
		print ''

		print '========================================='
		print "Testing: ", num_file
		print 'Testing INSERTION SORT with array of length ', len(o_array)
		print 'Sorting...'
		num_array = []
		for k in range(0,len(o_array)):
			num_array.append(o_array[k])
		start = time.clock()
		sorted_array = insertionsort.insertionSort(num_array,0,len(num_array)-1)
		end = time.clock()
		total = (end - start)
		print 'This took %s nanoseconds in total' % (total*100000)
		print 'Verified: ', checksort.checksortAsc(sorted_array)
		print ''

		print '========================================='
		print "Testing: ", num_file
		print 'Testing QUICK SORT with array of length ', len(o_array)
		print 'Sorting...'
		num_array = []
		for k in range(0,len(o_array)):
			num_array.append(o_array[k])
		start = time.clock()
		sorted_array = quicksort.quickSort(num_array,0,len(num_array)-1)
		end = time.clock()
		total = (end - start)
		print 'This took %s nanoseconds in total' % (total*100000)
		print 'Verified: ', checksort.checksortAsc(sorted_array)
		print ''

		print '========================================='
		print "Testing: ", num_file
		print 'Testing MED-3 QUICK SORT with array of length ', len(o_array)
		print 'Sorting...'
		num_array = []
		for k in range(0,len(o_array)):
			num_array.append(o_array[k])
		start = time.clock()
		sorted_array = med3quicksort.quickSort(num_array,0,len(num_array)-1, 20)
		end = time.clock()
		total = (end - start)
		print 'This took %s nanoseconds in total' % (total*100000)
		print 'Verified: ', checksort.checksortAsc(sorted_array)
		print ''

	print '========================================='
	print 'Now loading a really really big text file'
	num_file = "input_2pow25.txt"
	open_file = open(num_file, "r")
	line = open_file.readline()
	num_array = map(int, line.split())
	open_file.close()
	print '========================================='

	