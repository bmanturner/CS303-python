def quickSort(A,p,r):
	if p < r:
		q = partition(A,p,r)
		quickSort(A,p,q-1)
		quickSort(A,q+1,r)
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

if __name__ == '__main__':
	ary = [1,12,5,26,7,14,3,4,2,83,23,6]

	print quickSort(ary,0,len(ary)-1)

