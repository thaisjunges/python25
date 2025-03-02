#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO
preco = float(input('Digite o preço do produto: '))
novo_preco = preco - (preco * 5 / 100)
print('O valor preço do produto é {:.2f} e o valor na promoção com 5% de desconto é {:.2f}'.format(preco,novo_preco))