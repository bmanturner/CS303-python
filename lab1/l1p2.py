def recursiveBinarySearch(sorted_array, query, start=0, end='first_run'):
	if (end == 'first_run'):
		end = len(sorted_array) - 1
	if (end <= start):
		return -1

	midpoint = ((end - start) / 2) + start

	if (sorted_array[midpoint] == query):
		return midpoint
	elif (query < sorted_array[midpoint]):
		return recursiveBinarySearch(sorted_array, query, start, midpoint)
	else:
		return recursiveBinarySearch(sorted_array, query, midpoint + 1, end)



if __name__ == '__main__':
	sample_array = [1,2,3,4,5]
	result = recursiveBinarySearch(sample_array, 3)
	print ''
	print "==========="
	print sample_array
	print "Searching for %i using Recursive Binary Search:" % (2)
	result = recursiveBinarySearch(sample_array, 2)
	if result != -1:
		print "The number %i was found at index %i" % (2, result)
	else:
		print "The number is not in supplied number array."
	print "==========="