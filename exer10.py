lista = []

print("Digite 15 números distintos:")

while len(lista) < 15:
    elemento = int(input(f"Digite o {len(lista) + 1}º número: "))
    if elemento not in lista:
        lista.append(elemento)
        lista.sort()
    else:
        print("Esse número já foi inserido. Por favor, insira um número diferente.")

print("Lista final:", lista)