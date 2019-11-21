while(1):
    try:
        n = int(input("Wprowadź n liczb ciągu fibonacciego do wyświetlenia: "))
    except ValueError:
        print("Niepoprawne wprowadzenie")
        continue
    x=0
    y=1
    if(n<=0):
        continue
    print("Kolejne liczby ciągu fibbonachiego ("+str(n)+" kolejnych wyrazów od 0 włącznie).")
    print(x)
    if(n<=1):
        continue
    print(y)
    if(n<=2):
        continue
    for i in range(n-2):
        print(x+y)
        x,y=y,x+y
