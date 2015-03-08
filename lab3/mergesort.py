import sys
import insertionsort

def mergeSort(A, tmp, p, r, k):
	if r - p < k:
		return insertionsort.insertionSort(A, p, r)
	elif p < r:
		q = (p + r) / 2
		mergeSort(A, tmp, p, q, k)
		mergeSort(A, tmp, q + 1, r, k)
		merge(A, tmp, p, q, r)
	return A

def merge(A, tmp, p, q, r):
	i = p
	j = q + 1

	for k in range(p,r+1):
		tmp[k] = A[k]

	for k in range(p,r+1):
		if i > q:
			A[k] = tmp[j]
			j += 1
		elif j > r:
			A[k] = tmp[i]
			i += 1
		elif tmp[j] < tmp[i]:
			A[k] = tmp[j]
			j += 1
		else:
			A[k] = tmp[i]
			i += 1


if __name__ == '__main__':
	# if user inputs file name
	if (len(sys.argv) > 1):
		num_file = sys.argv[1]
	# else default file
	else:
		num_file = 'input_16.txt'

	# open file
	open_file = open(num_file, "r")
	line = open_file.readline()
	# make integer array from file
	num_array = map(int, line.split())
	# close file
	open_file.close()

	tmp = []
	for k in range(0,len(num_array)):
		tmp.append(num_array[k])

	print mergeSort(num_array, tmp, 0, len(num_array)-1)

