listagen = ('Lápis', 1.75, 'Boracha', 2, 'Caderno', 15.90,
            'Estojo', 25, 'Tranferidor', 4.20, 'Copasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' *40)
for pos in range(0, len(listagen)):
    if pos % 2 == 0:
        print(f'{listagen[pos]:.<30}', end='')
    else:
        print(f'R${listagen[pos]:>7.2f}')
print('-' *40)