numeros=[]
while True:
    num=int(input("Digite um número (0 para terminar):"))

    if(num == 100):
        break
    numeros.append(num)

    if numeros:
        maior=[num for num in numeros if num > 80]
        menor= [num for num in numeros if num < 10]
        media= sum(numeros) / len (numeros)
  
    print("Maiores que 80:",maior)
    print("Menores que 10:",menor)
    print("Média:{:.1f}".format(media))   