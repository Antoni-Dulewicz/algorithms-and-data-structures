from random import randint
def bubble(T):
    n = len(T)
    for i in range(n-1):
        for j in range(n-1-i):
            if T[j]>T[j+1]:
                T[j],T[j+1] = T[j+1],T[j]    
    return T            

""" for i in range(n):
        for j in range(i+1,n):
            if T[i]>T[j]:
                T[i],T[j]=T[j],T[i]"""
    
    
T = [0 for _ in range(1000)]
for i in range(1000):
    T[i] = randint(1,100)


T = bubble(T)
print(T)