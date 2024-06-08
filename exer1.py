C=0

while(C >= -5):
    C=float(input("Temperatura em Celsius:"))

    if(C >= -5):
        F= (C * 9/5) + 32
        K= C + 273
        print(F,"°F")
        print(K,"°K")

print("Programa encerrado")
        