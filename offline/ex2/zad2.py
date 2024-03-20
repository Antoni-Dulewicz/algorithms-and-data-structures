# ANTONI DULEWICZ
from zad2testy import runtests

"""Nie musimy wiedziec jakie sa kolejne kroki algorytmu tylko dla aktualnych wartosci
przyjmujemy najlepsze chwilowe rozwiazanie (zachlanne), wiec program tworzy kopiec z danej
tablicy funkcja buildheap a nastepnie przy kazdej iteracji po tablicy "naprawia" 
funkcja heapify wstawiąjac aktualny najwiekszy element na koniec tablicy. Ostatni 
element przy kazdej iteracji zmniejszamy o zmienna k ktora przy kazdej iteracji 
zwieksza sie o jeden (topienie się sniegu). Jezeli ostatni element jest mniejszy 
lub rowny zero petla się przerywa a jesli nie to dodajemy go to naszej objetosci V.
Zlozonosc obliczeniowa: O(nlogn)
 """

"""def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1)//2

def heapify(S,i,n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l<n and S[l]>S[max_ind]:
        max_ind = l
    if r<n and S[r]>S[max_ind]:
        max_ind = r

    if max_ind != i:
        S[i],S[max_ind] = S[max_ind],S[i]
        heapify(S,max_ind,n)

def build_heap(S):
    n = len(S)
    for i in range(parent(n-1),-1,-1):
        heapify(S,i,n)

def snow(S):
    V = 0
    n = len(S)
    k = 0
    build_heap(S)
    for i in range(n-1,0,-1):
        S[0],S[i] = S[i],S[0]
        if S[i] - k <= 0:
            break 
        V += S[i] - k
        k += 1
        heapify(S,0,i)
    
    return V
"""

def snow(S):
    S.sort()
    S = S[::-1]
    cnt = 0
    n = len(S)
    sum = 0
    for i in range(n):
        if S[i]-cnt <= 0:
            return sum
        else:
            sum += S[i]-cnt
        cnt += 1
    
    return sum



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
