lista = []

print("Preencha a lista com 25 valores reais:")

while len(lista) < 25:
    valor = float(input(f"Digite o {len(lista) + 1}º valor: "))
    lista.append(valor)

while True:
    posicao1 = int(input("Digite a posição do primeiro número na lista (entre 1 e 25): "))
    posicao2 = int(input("Digite a posição do segundo número na lista (entre 1 e 25): "))
    
    if 1 <= posicao1 <= 25 and 1 <= posicao2 <= 25:
        soma = lista[posicao1 - 1] + lista[posicao2 - 1]
        print(f"A soma dos elementos das posições {posicao1} e {posicao2} é: {soma}")
        break
    else:
        print("Posições inválidas. Por favor, digite posições válidas.")
