num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    res = str(input('Quer continuar ? [S/N]'))
    if res in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' *30)
print(f'A lista completa é {num}')
print(f'A lista dos pares é {pares}')
print(f'A lista completa impares é {impares}')
