w='''To    jest    jakiś
       rozstrzelony tekst!'''

print(w)

temp = w.split()
z = ""
for slowo in temp:
    z += slowo+" ";

print(z)
