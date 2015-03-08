def linearSearch(array, query):
	for index in range(len(array)):
		if array[index] == query:
			return index
		elif array[index] > query:
			return -1
	return -1

if __name__ == '__main__':
	sample_array = [1,2,3,4,5]
	result = linearSearch(sample_array, 2)
	print ''
	print "==========="
	print sample_array
	print "Searching for %i using Linear Search:" % (2)
	result = linearSearch(sample_array, 2)
	if result != -1:
		print "The number %i was found at index %i" % (2, result)
	else:
		print "The number is not in supplied number array."
	print "==========="
