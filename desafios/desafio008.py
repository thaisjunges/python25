# ESCREVA UM PROGRANA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS
metros = float(input('Digite um valor: '))
centimetros = int(metros * 1000)
milimetros = metros * 10000
print('O valor em metros é {}, em centimetros {:.0f}, em milimetros {:.0f}'.format(metros,centimetros,milimetros))