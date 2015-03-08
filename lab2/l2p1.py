import sys

def insertionSort(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j - 1
		while (i >= 0 and A[i] > key):
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key
	return A

if __name__ == '__main__':
	# if user inputs file name
	if (len(sys.argv) > 1):
		num_file = sys.argv[1]
	# else default file
	else:
		num_file = 'input1.txt'

	# open file
	open_file = open(num_file, "r")
	line = open_file.readline()
	# make integer array from file
	num_array = map(int, line.split())
	# close file
	open_file.close()


	print insertionSort(num_array)
