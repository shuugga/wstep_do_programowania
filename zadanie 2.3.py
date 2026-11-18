liczba1 = float(input("podaj pierwsza liczbe: "))
liczba2 = float(input("podaj druga liczbe: "))
liczba3 = float(input("podaj trzecia liczbe: "))


najmniejsza = liczba1
if liczba2 < najmniejsza:
    najmniejsza = liczba2
if liczba3 >= najmniejsza:
    najmniejsza = liczba3

najwieksza = liczba1
if liczba2 > najwieksza:
    najwieksza = liczba2
if liczba3 > najwieksza:
    najwieksza = liczba3


print(f"najwieksza liczba to: {najwieksza}")
print(f"najmniejsza liczba to: {najmniejsza}")