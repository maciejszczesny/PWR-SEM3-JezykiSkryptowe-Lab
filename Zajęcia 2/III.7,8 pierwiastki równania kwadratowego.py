import cmath #bez tego pierwiastek z -4 wychodził dziwny
def funkcjaKwardatowa(a,b,c):
    delta = (b**2) - (4*a*c)
    print("Delta wynosi: "+str(delta)+"")
    print("Pierwiastek z delty: "+str(cmath.sqrt(delta))+"")
    print("\n")
    if(delta == 0):
        print("Podwójne miejsce zerowe w jednym punkcie: ")
        print("X1==X2 = "+str(-(b/2*a))+"")
    if(delta > 0):
        print("Dwa różnie miejsca zerowe w różnych punktach: ")
        print("X1 = "+str(  (-b-delta**0.5)/(2*a)  )+"")
        print("X2 = "+str(  (-b+delta**0.5)/(2*a)  )+"")
    if(delta < 0):
        print("Brak pierwiastków rzeczywistych. Pierwiastki zespolone: ")
        print("X1 = "+str(  (-b-cmath.sqrt(delta))/(2*a) )+"")
        print("X2 = "+str(  (-b+cmath.sqrt(delta))/(2*a) )+"")
while(1):
    try:
        a = float(input("Podaj argument a wyrażenia ax^2+bx+c=0: "))
        b = float(input("Podaj argument b wyrażenia ax^2+bx+c=0: "))
        c = float(input("Podaj argument c wyrażenia ax^2+bx+c=0: "))
    except ValueError:
        print("Niepoprawne wprowadzenie!")
        continue
    funkcjaKwardatowa(a,b,c)
    
