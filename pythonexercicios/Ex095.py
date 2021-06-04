time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na {c + 1}ª partida?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Rsponda apenas S ou N. ')
    if resp == 'N':
        break
print('-' *30)
print('cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-'*30)
while True:
    bus = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if bus == 999:
        break
    if bus >= len(time):
        print(f'Não existe jogador com esse código {bus}:')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[bus]["nome"]}')
        for i, q in enumerate(time[bus]['gols']):
            print(f'   No jogo {i } fez {q} gols.')
        print('-'*40)
print('<<< VOLTE SEMPRE >>>')




