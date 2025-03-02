#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.FAÇA UM PROGRAMA
# QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO
import random
aluno1 = input('Digite o seu nome: ')
aluno2 = input('Digite o seu nome: ')
aluno3 = input('Digite o seu nome: ')
aluno4 = input('Digite o seu nome: ')

alunos = [
    aluno1,aluno2,aluno3,aluno4
]

sorteado = random.choice(alunos)
print(sorteado)