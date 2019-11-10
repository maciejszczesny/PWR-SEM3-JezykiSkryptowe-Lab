tekst = '''    Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
    Ile cię trzeba cenić, ten tylko się dowie,
    Kto cię stracił. Dziś piękność twą w całej ozdobie
    Widzę i opisuję, bo tęsknię po tobie.

    Panno Święta, co Jasnej bronisz Częstochowy
    I w Ostrej świecisz Bramie! Ty, co gród zamkowy
    Nowogródzki ochraniasz z jego wiernym ludem!
    Jak mnie dziecko do zdrowia powróciłaś cudem 
    (Gdy od płaczącej matki pod Twoję opiekę
    Ofiarowany, martwą podniosłem powiekę
    I zaraz mogłem pieszo do Twych świątyń progu
    Iść za wrócone życie podziękować Bogu),
    Tak nas powrócisz cudem na Ojczyzny łono.
    Tymczasem przenoś moję duszę utęsknioną
    Do tych pagórków leśnych, do tych łąk zielonych,
    Szeroko nad błękitnym Niemnem rozciągnionych;
    Do tych pól malowanych zbożem rozmaitem,
    Wyzłacanych pszenicą, posrebrzanych żytem;
    Gdzie bursztynowy świerzop, gryka jak śnieg biała,
    Gdzie panieńskim rumieńcem dzięcielina pała,
    A wszystko przepasane, jakby wstęgą, miedzą
    Zieloną, na niej z rzadka ciche grusze siedzą.'''

print(tekst)

znaki = 0;
samogloski = 0;
spolgloski = 0;
spacje = 0;
inne = 0;
samogloskiSzablon = "aeyioąęuó"
spolgloskiSzablon = "bcćdfghjklmnprstwyzźż"

for literka in tekst:
    znaki += 1
    for gloska in samogloskiSzablon:
        if (literka == gloska):
            samogloski += 1
            break
    for gloska in spolgloskiSzablon:
        if (literka == gloska):
            spolgloski += 1
            break
    if (literka == ' '):
        spacje += 1;
inne = znaki - samogloski - spolgloski - spacje
print("\n")
print("Tekst składa się ze "+str(znaki)+" znaków, w tym "+str(samogloski)+" samoglosek, "+str(spolgloski)+" spółgłosek, "+ str(spacje)+" spacji oraz "+str(inne)+" innych znaków." )

co2 = ""
co3 = ""
co7 = ""
for x in range(len(tekst)):
    if(x%2==0):
        co2 += tekst[x]
    if(x%3==0):
        co3 += tekst[x]
    if(x%7==0):
        co7 += tekst[x]

print("\n\nco 2 znak: ")
print(co2)
print("\n\nco 3 znak: ")
print(co3)
print("\n\nco 7 znak: ")
print(co7)

linia = ""
for znak in tekst:
    if znak!='\n':
        linia += znak;
    else:
        break
print("\n\n Pierwsza linia:")
print(linia)
linia = linia.upper()
print("\n Pierwsza linia wielkimi literami:")
print(linia)
tekst = tekst.replace("Litwo!","Polsko!")
print("\n\n Tekst po zamianie:")
print(tekst)
