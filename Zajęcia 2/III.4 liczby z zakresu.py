while(1):
    try:
        poczatek = int(input("Wprowadź początek zakresu: "))
        koniec = int(input("Wprowadź koniec zakresu: "))
    except ValueError:
        print("Niepoprawne wprowadzenie! (wprowadź liczby całkowite)")
        continue
    if (poczatek > koniec):
        print("Niepoprwany zakres! (początek większy niż koniec)")
        print("Ale spokojnie, zamieniam początek z końcem.")
        poczatek,koniec = koniec,poczatek
    print("Wszystkie liczby od "+str(poczatek)+" do "+str(koniec)+" które spełniają równanie:")
    for liczba in range(poczatek,koniec+1):
        if(liczba%2==1 and liczba%17==0):
            print (liczba)
    break
