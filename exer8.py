lista = []

while True:
    elemento = input("Digite um número inteiro positivo e par (ou 1 para terminar): ")
    
    if (elemento == '1'):
        break
    
    numero = int(elemento)
    
    if (numero % 2 == 0 and numero > 0):
        lista.append(numero)
    else:
        print("Digite um número inteiro positivo e par.")

print("Lista final:", lista)