from zad9testy import runtests
"""Program przygotowuje dane wstawiając je do jednej tablicy (stops) wypelnionej krotkami (O[i],C[i]).
Następnie program tworzy tablice (dp) wypelinona krotkami (inf,inf), tablica dp bedzie zawierac
informacje o tym ile najmniej mozemy zaplacic za postoje na trasie od 0 do i gdzie w dp[i][0] bez 
wykorzystania wyjatku z 2T a w dp[i][1] z wykorzystaniem. Sam minimalny koszt w dp[i] liczymy przez
znalezienie w poprzednich elementach tablicy (z warunekiem ze postoj jest blizej niz T lub 2T)
minmalnego kosztu."""
# Zlozonosc: O(n^2)
"""from math import inf
def prepare_data(O,C,L):
    n = len(O)
    F = [(0,0) for _ in range(n+1)]
    for i in range(1,n+1):
        F[i-1] = (O[i-1],C[i-1])
    F += [(L,0)]
    F.sort(key=lambda i:i[0])
    return F

def min_cost(O,C,T,L):
    stops = prepare_data(O,C,L)
    n = len(stops)
    dp = [(inf,inf) for _ in range(n)]
    dp[0] = (0,0)
    for i in range(1,n):
        min_y = inf
        min_x = inf
        j = i - 1
        while j >= 0 and abs(stops[j][0]-stops[i][0]) <= T:
            min_x = min(min_x,dp[j][0] + stops[i][1])
            min_y = min(min_y,dp[j][1] + stops[i][1])
            j -= 1

        while j >= 0 and abs(stops[j][0]-stops[i][0]) <= 2*T:
            min_y = min(min_y,dp[j][0] + stops[i][1])
            j -= 1
        dp[i] = (min_x,min_y)

    return min(dp[n-1][0],dp[n-1][1])"""

def prepare_data(O,C,L):
    for i in range(len(O)):
        O[i] = (O[i],C[i])
    
    O.append((0,0))
    O.append((L,0))
    O.sort(key=lambda x: x[0])


    return O

def min_cost(O,C,T,L):
    road = prepare_data(O,C,L)
    n = len(road)

    dp = [(0,0) for _ in range(n)]

    for i in range(1,n):
        
        j = i - 1
        min_without = float('inf')
        min_with = float('inf')
        while j >= 0 and road[i][0] - road[j][0] <= T:
            min_without = min(min_without, dp[j][0] + road[j][1])
            min_with = min(min_with, dp[j][1] + road[j][1])
            j -= 1
        
        j = i - 1
        while j >= 0 and road[i][0] - road[j][0] <= 2*T:
            min_with = min(min_with,dp[j][0] + road[j][1])
            j -= 1

        dp[i] = (min_without,min_with)


    return min(dp[n-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )

