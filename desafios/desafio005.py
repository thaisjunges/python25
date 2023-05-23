#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR

num = int(input("Digite um número: "))

n = 1
antecessor = (num) - (n)
sucessor = (num) + (n)

print("O número que você digitou é {}".format(num))
print("O antecessor é {} e o sucessor é {}".format(antecessor, sucessor))