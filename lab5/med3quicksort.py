import insertionsort

def quickSort(A,p,r,cutoff):
	N = r - p + 1
	if (N <= cutoff):
		insertionsort.insertionSort(A,p,r)
		return A
	if p < r:
		m = median3(A,p,r,p+(N/2))
		A[p], A[m] = A[m], A[p]
		q = partition(A,p,r)
		quickSort(A, p, q-1, cutoff)
		quickSort(A, q+1, r, cutoff)
	return A

def partition(A,p,r):
	x = A[r]
	i = p-1
	for j in range(p,r):
		if A[j] <= x:
			i+=1
			A[i],A[j] = A[j],A[i]
	A[i+1],A[r] = A[r],A[i+1]
	return i+1

def median3(A,i,j,k):
	if A[i] < A[j]:
		return j if A[j] < A[k] else k
	else:
		return i if A[i] < A[k] else k

if __name__ == '__main__':
	ary = [1,12,5,26,7,14,3,4,2,83,23,6]

	print quickSort(ary,0,len(ary)-1,20)

