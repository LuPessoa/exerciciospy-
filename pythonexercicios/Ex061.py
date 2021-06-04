print('Gerador de PA ')
print('-=' *10)
primeiro = int(input('primeiro Termo :'))
razão = int(input('Digite a Razão:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} =>'.format(termo), end='')
    termo = termo + razão
    cont = cont + 1
print('FIM')