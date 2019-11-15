import pickle

lista_kobiety = list()
lista_mezczyzni = list()
wyjatki = ["Kosma","Barnaba","Bonawentura","Jarema","Kuba"]

def dopisDoListy(imie,plec):
    if plec=="kobieta":
        if not imie in str(lista_kobiety):
            lista_kobiety.append(imie)
            lista_kobiety.sort()
        else:
            print("To imię występuje już na liście imion kobiecych!")
    else:
        if not imie in str(lista_mezczyzni):
            lista_mezczyzni.append(imie)
            lista_mezczyzni.sort()
        else:
            print("To imię występuje już na liście imion męskich!")

def zapisDoPliku():
    try:
        with open("imiona.txt","wt") as plik:
            plik.write("lista_kobiety\n")
            for kobieta in lista_kobiety:
                plik.write(str(kobieta)+"\n")
            plik.write("lista_mezczyzni\n")
            for mezczyzna in lista_mezczyzni:
                plik.write(str(mezczyzna)+"\n")
    except:
        print("Wystąpił błąd związany z zapisem! (to jest problem)")

def odczytZPliku():
    try:
        global lista_kobiety
        global lista_mezczyzni
        kobiety = False
        mezczyzni = False
        with open("imiona.txt","rt") as plik:
            for linia in plik.readlines():
                if linia == "lista_kobiety\n": kobiety=True
                if linia == "lista_mezczyzni\n": mezczyzni=True
                if kobiety == True and mezczyzni == False and not linia == "lista_kobiety\n" and not linia == "lista_mezczyzni\n":
                    lista_kobiety.append( linia.rstrip() )
                elif mezczyzni == True and not linia == "lista_kobiety\n" and not linia == "lista_mezczyzni\n":
                    lista_mezczyzni.append( linia.rstrip() )
                
    except FileNotFoundError:
        print("Nie istnieje jeszcze plik z imionami. (to w sumie nie problem)")
    except:
        print("Wystąpił błąd związany z odczytem! (to jest problem)")

odczytZPliku()
while(1):            
    try:
        imie = str(input("Wprowadź imię (lub koniec aby zakończyć): "))
    except ValueError:
        print("Wprowadzono niepoprawnę imię!")
    else:
        if not imie.isalpha(): print("Wprowadzono niepoprawnę imię!");continue
        imie = imie.lower().capitalize()
        if imie == "Koniec":
            break;
        if imie[-1]=="a" and not imie in str(wyjatki):
            dopisDoListy(imie,"kobieta")
        else:
            dopisDoListy(imie,"mężczyzna")

print("Lista imion kobiecych: ",lista_kobiety)
print("Lista imion męskich: ",lista_mezczyzni)
zapisDoPliku()
