def countsort(A,k):
    n = len(A)
    C = [0 for _ in range(k+1)]
    for i in range(n):
        C[A[i]] += 1
    
    for i in range(1,n):
        C[i] += C[i-1]
    print(C)
    T = [0 for _ in range(len(A))]
    for i in range(n-1,0,-1):
        T[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    print(T)

A = [0,2,2,5,4,1]
countsort(A,5)