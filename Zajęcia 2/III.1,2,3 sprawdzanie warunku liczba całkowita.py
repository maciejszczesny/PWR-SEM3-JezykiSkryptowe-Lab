def analiza(liczba):
    if(liczba < 0):
        return -1000
    if(liczba == 0):
        return "ZEROOOO!!!!"
    if(liczba > 0 and liczba < 10): #można równie dobrze 0 < liczba < 10, and=& a nie && - oczywiście trzeba być oryginalnym językiem
        return liczba
    if(liczba >= 10 and liczba <= 100):
        return "dużo"
    if(liczba > 100):
        return "bardzo dużo"

while (True):
    try:
        liczba = int(input("Wprowadź liczbę całkowitą: "))
    except ValueError:
        print("Wprowadzono coś co nie jest liczbą całkowitą. Koniec pętli!")
        break
    print(analiza(liczba))
