#DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE A SUA MÉDIA
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2 
print('A sua média entre {} e {:.1f} é {:.1f}'.format(nota1,nota2,media))