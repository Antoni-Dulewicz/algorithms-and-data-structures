from random import randint
def czy_palindrom(s):
    n = len(s)
    l = n//2
    for i in range(l):
        if s[i] != s[n-i-1]:
            return False
    return True    

def ceasarOn3(s):
    maxi = 1
    n = len(s)
    for d in range(3,n,2):
        for i in range(n-d+1):
            l = d//2
            res = []
            for j in range(l):
                if s[j+i] != s[i+d-j-1]:
                    break
                res += [s[j+i]]
            else:
                maxi = d
                print(res)
                break
        
    return maxi       

def ceasar( s ):
    maxi = 1
    n = len(s)
    for i in range(1,n-1):
        l = s[i]
        p = s[i]
        k = 0
        for j in range(1,i+1):
            if i+j == n:
                break

            l = s[i-j]
            p = s[i+j]

            if l != p:
                break

            k += 1
    
        if k*2+1 > maxi:
            maxi = k*2+1  
  
    return maxi

def mirror(c,i):
    return 2*c-i

def manacher(s):
    n = len(s)*2 + 3
    T = [0]*n
    P = [0]*n
    T[0] = '$'
    j = 0 
    for i in range(1,n-1):
        if i%2==1:
            T[i] = '#'
        else:
            T[i]=s[j]
            j += 1    
    T[n-1] = '@'

    maxi = 0
    c = 0
    r = 0
    for i in range(1,len(T)-1):
        #c = (mirr + i)/2
        mirr = mirror(c,i)

        if (i<r):
            P[i] = min(r-i,P[mirr])
        while T[i+(1+P[i])] == T[i -(1 + P[i])]:
            P[i] += 1

        if i + P[i] > r:
            c = i
            r = i + P[i]        
        if P[i]>maxi and P[i]%2==1:
                maxi = P[i]


    return maxi       

def ceasar( s ):
    maxi = 1
    n = len(s)
    i = 1
    for i in range(1,n-1):
        l = s[i]
        p = s[i]
        k = 0
        for j in range(1,i+1):
            if i+j == n:
                break
            l = s[i-j]
            p = s[i+j]
            if l != p:
                break
            k += 1

        if k*2+1 > maxi:
            maxi = k*2+1  
  
    return maxi




print(ceasar("abababa"))
#print(cesarOn2())
#print(cesarOn2("eqkaitwqkuyxyukqwtiakq"))
