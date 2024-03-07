def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1)//2

def heapify(A,i,n):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and A[l]>A[max_ind]:
        max_ind = l
    if r < n and A[r]>A[max_ind]:
        max_ind = r

    if max_ind != i:
        A[max_ind],A[i] = A[i],A[max_ind]
        heapify(A,max_ind,n)

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,i,n)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i],A[0]
        heapify(A,0,i)

    return A

A = [1,7,3,4,1]
print(heap_sort(A))    