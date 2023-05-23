#FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO 
#E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSIVEIS SOBRE ELE

teclado = input('Digite algo: ')

tipo = type(teclado) 
print("O tipo é: ", tipo)

alfa = teclado.isalpha()
print("Alfabetico: ", alfa)

alfanum = teclado.isalnum()
print("Alfanumérico: ", alfanum)

maius = teclado.isupper()
print("Maiúscula: ", maius)

minus = teclado.islower()
print("Minúscula: ", minus)





