#FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO,
#COSSENO E TANGENTE DESSE ÂNGULO
import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('O valor do cosseno é {:.2f}'.format(cosseno))
print('O valor do seno é {:.2f}'.format(seno))
print('O valor do tangente é {:.2f}'.format(tangente))