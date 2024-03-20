#ANTONI DULEWICZ
from zad7testy import runtests
"""Program iteruje po kolejnych kolumnach od konca i w każdej kolumnie dla kazdego wiersza (jesli
na tej kratce nie stoi "#") znajduje najwieksza odleglosc od punktu (0,0). Robi to najpierw przez
znalezienie najwiekszej odleglosci od pkt (0,0) w pierwszej iteracji a nastepnie znalezienie najwiekszej
odleglosci z wykorzystaniem odleglosci policzonych w poprzedniej kolumnie.
"""
#Zlozonosc: O(n^3)
"""def find_max_for_cell(L,col,i,j):
    n = len(L)
    up = j 
    down = j
    max_length = -1
    
    while up >= 0 and L[up][i] != "#":
        if col[up] != -1:
            new_length = col[up] + (j - up + 1)
            if max_length < new_length:
                max_length = new_length
        up -= 1

    

    while down < n and L[down][i] != '#':
        if col[down] != -1:
            new_length = col[down] + (down - j + 1)
            if max_length < new_length:
                max_length = new_length
        down += 1

    return max_length


def maze(L):
    n = len(L)
    col = [-1 for _ in range(n)]
    col[n-1] = 0
    up = n-2 

    while L[up][n-1] != '#' and up >= 0:
        col[up] = col[up+1] + 1
        up -= 1
    
    for i in range(n-2,-1,-1):
        newCol = [-1 for _ in range(n)]
        
        for j in range(n):
            if L[j][i] != '#':
                newCol[j] = find_max_for_cell(L,col,i,j)
                  
        col = newCol

    return col[0]
"""

def maze(L):
    n = len(L)
    #   [top, left, bottom]
    tab = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if L[i][j] == '#':
                tab[i][j] = [-2, -2, -2]

    for i in range(n):
        for j in range(n):
            if L[j][i] != '#':
                if j-1 >= 0 and tab[j-1][i][0] != -2 and max(tab[j-1][i][0], tab[j-1][i][1]) != -1:
                    tab[j][i][0] = max(tab[j-1][i][0], tab[j-1][i][1]) + 1
                else:
                    if i != 0 or j != 0:
                        tab[j][i][0] = -1

                if i-1 >= 0 and tab[j][i-1][1] != -2 and max(tab[j][i-1]) != -1:
                    tab[j][i][1] = max(tab[j][i-1]) + 1
                else:
                    tab[j][i][1] = -1

        for j in range(n-1, -1, -1):
            if L[j][i] != '#':
                if j+1 < n and (tab[j+1][i][2] >= 0 or tab[j+1][i][1] >= 0) and max(tab[j+1][i][1], tab[j+1][i][2]) != -1:
                    tab[j][i][2] = max(tab[j+1][i][1], tab[j+1][i][2]) + 1
                else:
                    tab[j][i][2] = -1

    return max(tab[n-1][n-1])



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
