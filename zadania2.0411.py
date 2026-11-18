lista = []
for i in range(10):
    elementy = int(input("podaj liczby: "))
    lista.append(elementy)

najwieksza = max(lista)
najmniejsza = min(lista)

print("najwieksza liczba: ", najwieksza)
print("najmniejsza liczba: ", najmniejsza)


lista2 = []
for i in range(10):
    element = input("podaj 10 elementow: ")
    lista.append(element)

print("lista: ", lista2)
szukany_element = input("podaj element do sprawdzenia: ")
szukanie = lista2.count(szukany_element)
print("element", szukany_element, "wystepuje", szukanie, "razy")

indeks = int(input("podaj indeks elementu do usuniecia: "))
usuniety = lista.pop(indeks)
print("usuniety element: ", usuniety)
print("lista po usunieciu: ", lista2)
