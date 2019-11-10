while(1):
    try:
        rok = int(input("Wprowadź rok: "))
    except ValueError:
        print("Niepoprawne wprowadzenie!")
        continue
    if(rok%4==0 and not rok%100==0 or rok%400==0):
        print("Ten rok jest przestępny!")
    else:
        print("Ten rok nie jest przestępny.")
