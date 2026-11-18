punkty = 100

if punkty > 80 and punkty <= 100:
    print("ocena 5")
else:
    print("ocena mniejsza niz 4,5")

    czas = 60

    if punkty > 90 or czas < 70:
        print("egzamin zdany")
    else:
        print("egzamin do poprawy")

temperatura = eval(input("podaj temperature w stopniach celsjusza: "))
temp_fahrenheit = 9/5*temperatura+32

if temp_fahrenheit < 32:
    print("woda zamarza")
if temp_fahrenheit > 212:
    print("temperatura wrzenia")
else:
    print("temperatura w normie")

rok = eval(input("podaj rok: "))
if rok%100==0 and rok%400==0:
    print("rok jest przestepny")
elif rok%100 != 0 and rok%400 != 0:
    print("to nie jest rok przestepny")
elif rok%4==0:
    print("jest to rok przestepny")
else:
    print("nie jest to rok przestepny")

from random import randint

liczba = randint(1, 10)
losuj = eval(input("podaj liczbe od 1 do 10: "))
print("wylosowana liczba: ", liczba)
if losuj == liczba:
    print("zgadles")
else:
    print("sprobuj jeszcze raz")