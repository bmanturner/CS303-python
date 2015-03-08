def checksortAsc(A):
	for j in range(len(A)-1):
		if A[j] > A[j+1]:
			return False
	return True