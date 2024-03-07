from typing import List
class Heap:
    def __init__(self,max_heap,mediana,min_heap):
        self.max_heap = max_heap
        self.mediana = mediana
        self.min_heap = min_heap

def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1)//2
def heapify_max(T,i,n):
    l = left(i)
    r = right(i)
    max_idx = i

    if l < n and T[l] > T[max_idx]:
        max_idx = l
    if r < n and T[r] > T[max_idx]:
        max_idx = r
    
    if max_idx != i:
        T[max_idx],T[i] = T[i],T[max_idx]
        heapify_max(T,max_idx,n)
def heapify_min(T,i,n):
    l = left(i)
    r = right(i)
    min_idx = i

    if l < n and T[l] < T[min_idx]:
        min_idx = l
    if r < n and T[r] < T[min_idx]:
        min_idx = r
    
    if min_idx != i:
        T[min_idx],T[i] = T[i],T[min_idx]
        heapify_min(T,min_idx,n)
def build_max_heap(T):
    n = len(T)
    for i in range(parent(n-1),-1,-1):
        heapify_max(T,i,n) 
def build_min_heap(T):
    n = len(T)
    for i in range(parent(n-1),-1,-1):
        heapify_min(T,i,n)

def print_heap(heap: Heap):
    print(heap.max_heap)
    print(heap.mediana)
    print(heap.min_heap)
  
def make(T: List)->Heap:
    T = sorted(T)
    n = len(T)
    mid = n//2
    if n%2 == 1:
        mediana = T[mid]
        T_max = T[:mid]
        T_min = T[mid+1:]
        build_max_heap(T_max)
        build_min_heap(T_min)
    else:
        mediana = (T[mid]+T[mid-1])/2
        T_max = T[:mid-1]
        T_min = T[mid+1:]
        build_max_heap(T_max)
        build_min_heap(T_min)

    heap = Heap(T_max,mediana,T_min)
    return heap

T = [4,2,7,5,3,3]

kopiec = make(T)
print_heap(kopiec)

