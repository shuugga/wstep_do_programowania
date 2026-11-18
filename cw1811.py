for i in range(1, 11):
    print(i)

suma = 0
for i in range(1, 101):
    suma += i
print(suma)

owoce = ["jablko", "banan", "gruszka", "sliwka", "wisnia"]
for owoc in owoce:
    print(owoc)

slowo = input("Podaj słowo: ")
for litera in slowo:
    print(litera)

for i in range(1, 11):
    print(i ** 2)

liczba = 7
strzal = 0
while strzal != liczba:
    strzal = int(input("zgadnij liczbę od 1 do 10: "))
    if strzal == liczba:
        print("zgadles")
    else:
        print("sprobuj ponownie")

i = 0
while i <= 20:
    print(i)
    i += 2

suma = 0
i = 2
while i <= 100:
    suma += i
    i += 2
print(suma)

lista = []
for i in range(5):
    element = input("podaj element: ")
    lista.append(element)
print("lista przed usunieciem:", lista)
do_usuniecia = input("ktory element usunac")
if do_usuniecia in lista:
    lista.remove(do_usuniecia)
else:
    print("nie ma takiego elementu")
print("lista po usunieciu:", lista)

liczba = int(input("podaj liczbe: "))
while liczba >= 0:
    print(liczba)
    liczba -= 1

suma = 0
liczba = int(input("podaj liczbe: "))
while liczba != 0:
    suma += liczba
    liczba = int(input("podaj kolejna liczbe: "))
print("suma:", suma)


