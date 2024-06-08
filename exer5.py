num = 0
while True:
    num = int(input("Digite um número inteiro maior que 2: "))
    
    if (num > 2):
        quadrado = num ** 2
        cubo = num ** 3

    else:
        print("Número incorreto.")
        break

    print(num,"elevado ao quadrado:", quadrado)
    print(num,"elevado ao cubo:", cubo)