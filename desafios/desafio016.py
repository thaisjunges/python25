#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE
#NA TELA A SUA PORÇÃO INTEIRA
#EX: DIGITE UM NÚMERO: 6.127 O NÚMERO 6.127TEM A PARTE INTEIRA 6
import math
num = float(input('Digite um numero: '))
inteiro = math.floor(num)
print(inteiro)