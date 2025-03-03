#CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA
n = int(input("Digite um número: "))
d = n * 2
t = n * 3
rq = n ** (1/ 2)
print('O numero é {} e o seu dobro é {}'.format(n,d))
print('O seu dobro é {}'.format(d))
print('O seu triplo é {}'.format(t))
print('A raiz quadrada é {:.2f}'.format(rq))