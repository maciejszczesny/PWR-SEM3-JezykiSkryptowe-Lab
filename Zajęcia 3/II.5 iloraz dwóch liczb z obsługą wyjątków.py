try:
    x = int(input('Podaj pierwszą liczbę całkowitą: '))
    y = int(input('Podaj drugą liczbę całkowitą: '))
except ValueError:
    print('To nie jest liczba całkowita!')
else:
    try:
        z = x/y
    except ZeroDivisionError:
        print('Nie można dzielić przez zero!')
    else:
        print('Iloraz tych liczb wynosi ',z)
finally:
    print('Dziękuje!')
