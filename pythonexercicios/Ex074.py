from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10), randint(1 ,10))
print('Os valores Sorteados foram :', end='')
for n in numeros:
    print(f' {n}', end='')
print(f'\nO Maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')