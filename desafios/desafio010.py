#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS
#DÓLARES ELA PODE COMPRAR CONSIDERE USS1.00 = R$ 3,27
dinheiro = float(input('Digite o valor que você tem: R$'))
dolar = (dinheiro / 3.27)
print('Com o valor de R${} você pode comprar ${:.2f} dólares'.format(dinheiro,dolar))