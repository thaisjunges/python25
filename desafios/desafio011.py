#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE
#DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M²
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
qtd_tinta = area / 2
print('Você precisa de {} litros de tinta'.format(qtd_tinta)) 