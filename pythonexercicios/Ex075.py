num = (int(input('Digite um numero :')),
      int(input('Digite outro Numero :')),
      int(input('Digite m,ais um numero :')),
      int(input('Digite o ultimo numero : ')))
print(f'Você digitou os valores {num}')
print(f'O Valor 9 apareceu {num.count(9)} vezes')
if 3 in num :
    print(f'O valor 3 apareceu na {num.index(3) +1}ª posição ')
else:
    print('O valor 3 não foi digitado em nem uma posição')
print('Os valores pares  digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
