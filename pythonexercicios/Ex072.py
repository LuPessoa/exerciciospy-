cont = ('ziro', 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen','fourteen', 'fifteen', 'sixteen', 'seventeen',
        'eighteen', 'nineteen','twenty')
while True:
    num = int(input('Digite um numero entre 0 e 20 : '))
    if 0 <= num <=20:
        break
    print('Tente novamanente. ',end='')
print(f'Você digitou o Número {cont[num]}')