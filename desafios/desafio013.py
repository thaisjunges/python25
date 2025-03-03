#FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO
salario = float(input('Digite o seu salário: '))
aumento = salario * 15/100
total = salario + aumento
print('O salário era R${} e com o aumento de 15% que é o valor de R${} seu novo salário ficou R${}'.format(salario, aumento, total))