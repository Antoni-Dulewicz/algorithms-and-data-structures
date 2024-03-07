def ile_zapelnionych(pojemniki,N):
    cnt = 0
    maxy2 = 0
    n = len(pojemniki)
    for i in range(n):
        if pojemniki[i][3] > maxy2:
            maxy2 = pojemniki[i][3]

    e = 0
    mid = maxy2/2
    while e < 100:
        V  = 0

        for i in range(n):
            if mid >= pojemniki[i][3]:
                V += (pojemniki[i][2] - pojemniki[i][0])*(pojemniki[i][3] - pojemniki[i][1])
            elif mid >= pojemniki[i][1] and mid < pojemniki[i][3]:
                V += (pojemniki[i][2] - pojemniki[i][0])*(mid - pojemniki[i][1])

        tmp = round(V,2)
        if tmp == N:
            break
        if V>N:
            mid = mid - ((maxy2-mid)/2)
        elif V<N:   
            mid = ((maxy2-mid)/2) + mid

        e += 1
        

    for i in range(n):
        if mid >= pojemniki[i][3]:        
            cnt += 1

    return cnt        





            

pojemniki = [(1,0.5,3,2.5),(1,4,2,5),(3,4,4,7),(3.5,2,6,3)]
print(ile_zapelnionych(pojemniki,7.3))