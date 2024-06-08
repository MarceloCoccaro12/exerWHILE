numeros=[]

while True:
    num=float(input("Digite um número (0 para terminar):"))
    numeros.append(num)

    if(num == 0):
        print("Programa encerrado.")
        break

    if numeros:

        soma= sum(numeros)
        media= soma / len(numeros)
        print("Soma:", soma)
        print("Média:{:.1f}".format(media))

        