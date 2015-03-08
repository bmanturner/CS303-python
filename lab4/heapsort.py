def heapSort(A):
	buildMaxHeap(A)
	for i in range(len(A)-1,0,-1):
		A[0], A[i] = A[i], A[0]
		maxHeapify(A,0,i-1)
	return A

def buildMaxHeap(A):
	for parent in range((len(A)-2)/2,-1,-1):
		maxHeapify(A,parent,len(A)-1)

def maxHeapify(A,parent,heap_size):
	left = parent*2+1
	right = left + 1
	if left <= heap_size and A[left] > A[parent]:
		largest = left
	else:
		largest = parent
	if right <= heap_size and A[right] > A[largest]:
		largest = right
	if largest != parent:
		A[parent], A[largest] = A[largest], A[parent]
		maxHeapify(A,largest, heap_size)

if __name__ == '__main__':
	ary = [3,6,5,4,8,9,1,2,7]

	print heapSort(ary)

