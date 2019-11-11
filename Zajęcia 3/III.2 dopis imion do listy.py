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
        with open("imiona.bin","wb") as plik:
            pickle.dump(lista_kobiety, plik)
            pickle.dump(lista_mezczyzni, plik)
    except:
        print("Wystąpił błąd związany z zapisem! (to jest problem)")

def odczytZPliku():
    try:
        with open("imiona.bin","rb") as plik:
            global lista_kobiety
            lista_kobiety = pickle.load(plik)
            global lista_mezczyzni
            lista_mezczyzni = pickle.load(plik)
            print("Wczytano dane z pliku.")
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
