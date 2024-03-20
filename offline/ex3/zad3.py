#ANTONI DULEWICZ
from zad3testy import runtests

"""Program appenduje do danej tablicy slow te slowa ktore nie sa palindromami w odwroconej kolejnosci,
nastepnie sortuje i zlicza najdluzszy ciag tych samych wyrazow.
Program ma złożoność: O(2N + nlogn*n)
"""

"""def partition(T,p,r):
    n = len(T)
    x = T[r]
    i = p - 1
    for j in range(p,r):
        if T[j] <= x:
            i += 1
            T[j],T[i] = T[i],T[j]
    T[i+1],T[r] = T[r],T[i+1]
    
    return i + 1

def quicksort(T,p,r):
    while p < r:
        q = partition(T,p,r)
        if q - p < r - q:
            quicksort(T,p,q-1)
            p = q + 1
        else:
            quicksort(T,q+1,r)
            r = q - 1 
    return T        

def palindrom(str):
    return str == str[::-1]

def odwroc(str):
    return str[::-1]

def strong_string(T):
    n = len(T)
    for i in range(n):
        if not palindrom(T[i]):
            T.append(odwroc(T[i]))
    n = len(T)
    T = quicksort(T,0,n-1)
    strongest = 0
    cnt = 1
    for i in range(1,n):
        prev = T[i-1]
        curr = T[i]
        if T[i-1] == T[i]:
            cnt += 1
        else:
            strongest = max(strongest,cnt)
            cnt = 1
    return strongest
"""

def palindrom(S):
    return S == S[::-1]

def odwroc(S):
    return S[::-1]


def strong_string(T):
    n = len(T)

    new_T = []

    for i in range(n):
        if not palindrom(T[i]):
            new_T.append(T[i])
            new_T.append(odwroc(T[i]))
        else:
            new_T.append(T[i])

    n = len(new_T)
    new_T.sort()
    longest = 0
    cnt = 1
    for i in range(1,n):
        if new_T[i-1] == new_T[i]:
            cnt += 1
        else:
            longest = max(longest,cnt)
            cnt = 1
    return longest


#zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
