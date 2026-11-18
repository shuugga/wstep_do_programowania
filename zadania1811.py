for i in range(10,0,-1):
    print(i, end = " ")

    for i in range(4):
        print("*"*6)
    liczby = [10,20,30,40,50]

for liczba in liczby:
        print(liczba)

tekst = "python"
for litera in tekst:
    print(litera)

owoce = ["banan", "jablko", "malina", "gruszka"]
for owoc in owoce:
    print(f"owoc: {owoc}")

lista = [1,2,3,4,6,7]
for i in lista:
    if i == 4:
        break
    print(i)

for zmienna in range(5):
    if zmienna == 2:
        continue
    print(zmienna)

temp = 0
while temp != -1000:
    temp = eval(input("wprowadz temperature: "))
    print("temp w st fahernheit: ", temp*9/5+32)

while True:
    temp = eval(input("wprowadz temp: "))
    if temp == -1000:
        print("koniec")
        break
    print("temp w st fahrenheit: ", temp*9/5+32)

