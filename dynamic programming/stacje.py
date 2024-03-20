def stacje_2(L,S):
    poz = 0 
    n = len(S)
    najtansza_stacja = 0 
    paliwo = 0
    koszt = 0 
    while poz < n:
        najtansza_stacja = sorted([x[1] for x in enumerate(S)[poz:poz + L] if x[1]],key=lambda x: x[1])[0] #wyciagamy pare indeks i cena tej najtanszej stacji
        if najtansza_stacja[0] == poz:
            #tankujemy do pelna
            brakuje = min(L - paliwo,n - poz - paliwo)
            koszt += brakuje*najtansza_stacja[1]
            paliwo += brakuje
            poz += min(L,n - poz)
        else:
            #tankujemy tyle zeby dojechac do nastepnej stacji 
            odl = najtansza_stacja[0] - poz
            ile_dotankowac = max(0,odl,odl-paliwo)
            paliwo += ile_dotankowac
            koszt += ile_dotankowac * S[poz]
            poz += odl 
        