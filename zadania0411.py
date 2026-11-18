moja_lista = [1,2,3, "cztery" ,5.0[6,7], "osiem"]
print(moja_lista[5][0])

moja_lista.append("nowy element") #dodanie elementu na koncu listy
print(moja_lista)

moja_lista.insert(0,"**")
print(moja_lista)

moja_lista.remove("cztery")
print(moja_lista)

element_usuniety = moja_lista.pop(0)
print("usuniety element: ", element_usuniety)
print("lista po usunieciu: ", moja_lista)

print("ostatni element listy: ", moja_lista[-1])
print("elementy od 0 do 4:", moja_lista[:5])

print("ilosc elementow w liscie: ", len(moja_lista))

lista = [1,2,3,-1,-79,80,95]
print("lista przed zmianami: ", lista)
lista.reverse()
print("lista po odwroceniu: ", lista)
lista.sort()
print("lista po sortowaniu: ", lista)

owoce = ['jablko','morela','malina','truskawka']
print("lista owocowa: ", owoce)

owoce[1] = 'ziemniak'
print("lista po zmianie: ", owoce)

idx = owoce.index("wisnia")
print("miejsce szukanego elementu: ", idx)

idx = owoce.index("jablko")
print("miejsce szukanego elementu: ", idx)


moja_krotka = (1,2,3,4,5,0,"szesc")
print("krotka: ", moja_krotka)


print("pierwszy element krotki: ", moja_krotka[0])
print("dlugosc krotki: ", len(moja_krotka))

moja_lista2 = list(moja_krotka)
moja_lista2.append("nowy")
moja_krotka = tuple(moja_lista2)
print("nowa krotka: ", moja_krotka)