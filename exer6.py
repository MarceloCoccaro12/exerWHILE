numeros=[10,11,12,13,14,15]

while True:
    num = input("Digite um número entre 10 e 15: ")
    
    if len(numeros):
        num = int(num)

        if (num >= 10) and (num <= 15):
            raiz = num ** (1/2)
            print("A raiz quadrada de", num, "é: {:.1f}".format(raiz))
            
        else:
            print("Entrada inválida. Digite um número válido entre 10 e 15.")