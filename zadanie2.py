wzrost = eval(input("podaj wzrost w metrach: "))
waga = eval(input("podaj wage w kilogramach: "))
BMI = waga/ (wzrost ** 2)
if BMI < 18.5:
    print("niedowaga")
elif BMI >= 18.6 and BMI <= 24.9:
    print("waga prawidlowa")
elif BMI >= 25 and BMI <= 29.9:
    print("nadwaga")
elif BMI >= 30:
    print("otylosc")