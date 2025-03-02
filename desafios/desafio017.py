#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE 
#UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA
import math
cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.sqrt(cat_oposto**2 + cat_adjacente**2)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))
