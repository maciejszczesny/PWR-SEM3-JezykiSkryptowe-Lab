slownik = { 0:"zero",1:"jeden",2:"dwa",3:"trzy",4:"cztery",5:"pięć", 6:"sześć" }

while(1):
    try:
        liczba = int(input("Podaj cyfrę (od 0 do 6): "))
    except ValueError:
        print("Niepoprawna cyfra!")
    else:
        if(not 0<=liczba<=6):
            print("Cyfra spoza zakresu!")
        else:
            print( "Wprowadzona cyfra to: ",str(slownik.get(liczba) ))
