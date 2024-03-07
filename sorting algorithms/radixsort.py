def partition(T,p,r):
    n = len(T)
    x = T[r][1]
    i = p - 1
    for j in range(p,r):
        if T[j][1] <= x:
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

def czy_rownow(s1,s2):
    s3 = s2[::-1]
    return s1 == s2 or s1 == s3 



def count_sort(T,curr):
    n = len(T)
    C = [0]*26
    for i in range(n): 
        C[ord(T[i][curr])-97] += 1

    for i in range(1,26):
        C[i] += C[i-1]
    
    O = [0]*n

    for i in range(n-1,-1,-1):
        tmp = ord(T[i][curr]) - 97
        O[C[tmp] - 1] = T[i]
        C[tmp] -= 1
    
    return O



def radix_sort_f(T):
    n = len(T[0])
    for i in range(n-1,-1,-1):
        T = count_sort(T,i)
    return T 

def radix_sort_b(T):
    n = len(T[0])
    for i in range(n):
        T = count_sort(T,i)
    return T 

def longest(T):
    n = len(T)
    wyniki = [[T[0]]]
    for i in range(1,n):
        tmp = T[i]
        for j in range(len(wyniki)):
            if czy_rownow(tmp,wyniki[j][0]):
                wyniki[j].append(tmp)
                break
        else:
            wyniki.append([tmp])
    longest = 0
    for x in wyniki:
        if len(x) > longest:
            longest = len(x)
    
    return longest


def strong_string(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i],len(T[i]))
    quicksort(T,0,n-1)
    print(T)
    curr = [T[0][0]]
    length = T[0][1]
    cnt = 0
    strongest = 0
    cnt = 0
    for i in range(1,n):
        if T[i][1] == length:
            curr += [T[i][0]]
        else:
            if len(curr)<strongest:
                continue
            print(radix_sort_f(curr))
            print(radix_sort_b(curr))
            cnt = longest(curr)
            if cnt > strongest:
                strongest = cnt
            curr = [T[i][0]]
            length = T[i][1]
    if len(curr)>strongest:
        cnt = longest(curr)
        if cnt > strongest:
            strongest = cnt
    return strongest



T =  ["pies", "mysz", "kot", "zsym","rozz","kogut","seip","tok", "seip", "kot"]

print(strong_string(T))    
