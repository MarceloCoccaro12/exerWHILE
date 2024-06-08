cardapio = {
    100: {"item": "Cachorro quente", "preco": 3.50},
    101: {"item": "Bauru Simples", "preco": 3.80},
    102: {"item": "Bauru c/ovo", "preco": 4.50},
    103: {"item": "Hamburguer", "preco": 4.70},
    104: {"item": "Cheeseburger", "preco": 5.30},
    104: {"item": "Refrigerante", "preco": 4.00}

}

total_a_pagar = 0.0

while True:
    codigo = int(input("Digite o código do item (ou 0 para encerrar): "))
    
    if (codigo == 0):
        break
    
    if (codigo not in cardapio):
        print("Código inválido. Por favor, digite um código válido.")
    
    quantidade = int(input("Digite a quantidade desejada: "))
    preco_unitario = cardapio[codigo]["preco"]
    valor_item = preco_unitario * quantidade
    total_a_pagar += valor_item

    print(f"{quantidade}x {cardapio[codigo]['item']}: R${valor_item:.2f}")

print(f"Total a pagar: R${total_a_pagar:.2f}")