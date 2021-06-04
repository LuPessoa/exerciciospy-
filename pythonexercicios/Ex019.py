import random
al1 = input('Primeiro Aluno:')
al2 = input('Segundo Aluno:')
al3 = input('Terceiro Aluno:')
al4 = input('Quarto Aluno:')
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
